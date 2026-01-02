"""
Data Preprocessing Module
==========================
Handles feature engineering, scaling, and data preparation for ML models.

Author: Team Three Unknowns
Date: January 2026
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from typing import Tuple
import joblib
from pathlib import Path


class FraudPreprocessor:
    """
    Preprocess fraud detection data for machine learning.
    
    Includes:
    - Feature scaling
    - Train-test split
    - SMOTE for handling class imbalance
    """
    
    def __init__(self, test_size: float = 0.2, random_state: int = 42):
        """
        Initialize preprocessor.
        
        Args:
            test_size: Proportion of data for testing (0.0-1.0)
            random_state: Random seed for reproducibility
        """
        self.test_size = test_size
        self.random_state = random_state
        self.scaler = StandardScaler()
        self.feature_columns = None
        
    def split_features_target(self, df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
        """
        Separate features (X) from target (y).
        
        Args:
            df: Full dataset with 'Class' column
            
        Returns:
            Tuple of (X, y)
        """
        # Target column
        y = df['Class']
        
        # All columns except 'Class'
        X = df.drop('Class', axis=1)
        
        # Store feature names
        self.feature_columns = X.columns.tolist()
        
        print(f"📊 Features: {len(self.feature_columns)}")
        print(f"   Target distribution: {y.value_counts().to_dict()}")
        
        return X, y
    
    def train_test_split_data(
        self, 
        X: pd.DataFrame, 
        y: pd.Series
    ) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        """
        Split data into training and testing sets.
        
        Args:
            X: Features
            y: Target variable
            
        Returns:
            X_train, X_test, y_train, y_test
        """
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, 
            test_size=self.test_size, 
            random_state=self.random_state,
            stratify=y  # Maintain class distribution
        )
        
        print(f"\n✂️  Train-Test Split:")
        print(f"   Training samples: {len(X_train):,}")
        print(f"   Testing samples: {len(X_test):,}")
        print(f"   Test size: {self.test_size*100:.0f}%")
        
        return X_train, X_test, y_train, y_test
    
    def scale_features(
        self, 
        X_train: pd.DataFrame, 
        X_test: pd.DataFrame
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Scale features using StandardScaler.
        
        Fits on training data, transforms both train and test.
        
        Args:
            X_train: Training features
            X_test: Testing features
            
        Returns:
            Scaled X_train, X_test as numpy arrays
        """
        print("\n⚖️  Scaling features...")
        
        # Fit on training data only
        X_train_scaled = self.scaler.fit_transform(X_train)
        
        # Transform test data using fitted scaler
        X_test_scaled = self.scaler.transform(X_test)
        
        print(f"   ✅ Features scaled (mean=0, std=1)")
        print(f"   Example - Before: {X_train.iloc[0, 0]:.4f}")
        print(f"   Example - After:  {X_train_scaled[0, 0]:.4f}")
        
        return X_train_scaled, X_test_scaled
    
    def handle_imbalance(
        self, 
        X_train: np.ndarray, 
        y_train: pd.Series,
        sampling_strategy: str = 'auto'
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Apply SMOTE to handle class imbalance.
        
        Args:
            X_train: Training features (scaled)
            y_train: Training target
            sampling_strategy: 'auto' for 50-50 balance
            
        Returns:
            X_resampled, y_resampled
        """
        print("\n🔄 Applying SMOTE (Synthetic Minority Over-sampling)...")
        
        # Check original distribution
        original_dist = pd.Series(y_train).value_counts()
        print(f"   Before SMOTE:")
        print(f"      Genuine (0): {original_dist.get(0, 0):,}")
        print(f"      Fraud (1): {original_dist.get(1, 0):,}")
        
        # Apply SMOTE
        smote = SMOTE(random_state=self.random_state, sampling_strategy=sampling_strategy)
        X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
        
        # Check new distribution
        new_dist = pd.Series(y_resampled).value_counts()
        print(f"\n   After SMOTE:")
        print(f"      Genuine (0): {new_dist.get(0, 0):,}")
        print(f"      Fraud (1): {new_dist.get(1, 0):,}")
        print(f"   ✅ Dataset balanced!")
        
        return X_resampled, y_resampled
    
    def full_preprocessing_pipeline(
        self, 
        df: pd.DataFrame,
        apply_smote: bool = True
    ) -> dict:
        """
        Run complete preprocessing pipeline.
        
        Args:
            df: Raw dataset with 'Class' column
            apply_smote: Whether to apply SMOTE for balancing
            
        Returns:
            Dictionary with all processed data
        """
        print("=" * 70)
        print("🔧 STARTING PREPROCESSING PIPELINE")
        print("=" * 70)
        
        # Step 1: Split features and target
        X, y = self.split_features_target(df)
        
        # Step 2: Train-test split
        X_train, X_test, y_train, y_test = self.train_test_split_data(X, y)
        
        # Step 3: Scale features
        X_train_scaled, X_test_scaled = self.scale_features(X_train, X_test)
        
        # Step 4: Handle imbalance (optional)
        if apply_smote:
            X_train_balanced, y_train_balanced = self.handle_imbalance(
                X_train_scaled, y_train
            )
        else:
            X_train_balanced = X_train_scaled
            y_train_balanced = y_train
        
        print("\n" + "=" * 70)
        print("✅ PREPROCESSING COMPLETE")
        print("=" * 70)
        
        return {
            'X_train': X_train_balanced,
            'X_test': X_test_scaled,
            'y_train': y_train_balanced,
            'y_test': y_test,
            'feature_names': self.feature_columns,
            'scaler': self.scaler
        }
    
    def save_scaler(self, filepath: str):
        """Save fitted scaler to disk."""
        joblib.dump(self.scaler, filepath)
        print(f"💾 Scaler saved to: {filepath}")
    
    def load_scaler(self, filepath: str):
        """Load fitted scaler from disk."""
        self.scaler = joblib.load(filepath)
        print(f"📂 Scaler loaded from: {filepath}")


# Quick usage example
if __name__ == "__main__":
    from data_loader import FraudDataLoader
    
    # Load data
    loader = FraudDataLoader()
    try:
        df = loader.load_creditcard_data()
    except FileNotFoundError:
        df = loader.load_sample_data()
    
    # Preprocess
    preprocessor = FraudPreprocessor(test_size=0.2, random_state=42)
    processed_data = preprocessor.full_preprocessing_pipeline(df, apply_smote=True)
    
    print("\n📦 Processed data ready for modeling:")
    print(f"   X_train shape: {processed_data['X_train'].shape}")
    print(f"   X_test shape: {processed_data['X_test'].shape}")
