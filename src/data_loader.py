"""
Data Loader Module
==================
Handles loading and initial validation of fraud detection datasets.

Author: Team Three Unknowns
Date: January 2026
"""

import pandas as pd
import numpy as np
import os
from pathlib import Path


class FraudDataLoader:
    """
    Load and validate fraud detection datasets.
    
    Supports both raw Kaggle data and sample transaction files.
    """
    
    def __init__(self, data_dir: str = None):
        """
        Initialize data loader.
        
        Args:
            data_dir: Path to data directory. Defaults to '../data'
        """
        if data_dir is None:
            # Auto-detect data directory
            current_dir = Path(__file__).parent
            self.data_dir = current_dir.parent / 'data'
        else:
            self.data_dir = Path(data_dir)
        
        self.raw_dir = self.data_dir / 'raw'
        self.processed_dir = self.data_dir / 'processed'
        
        # Create directories if they don't exist
        self.processed_dir.mkdir(parents=True, exist_ok=True)
    
    def load_creditcard_data(self) -> pd.DataFrame:
        """
        Load the main Kaggle credit card fraud dataset.
        
        Returns:
            pd.DataFrame: Loaded dataset with all features
            
        Raises:
            FileNotFoundError: If creditcard.csv is not found
        """
        filepath = self.raw_dir / 'creditcard.csv'
        
        if not filepath.exists():
            raise FileNotFoundError(
                f"Dataset not found at {filepath}\n"
                "Please download from: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud"
            )
        
        print(f"📂 Loading dataset from: {filepath}")
        df = pd.read_csv(filepath)
        
        print(f"✅ Loaded {len(df):,} transactions")
        print(f"   - Features: {df.shape[1]}")
        print(f"   - Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
        
        return df
    
    def load_sample_data(self) -> pd.DataFrame:
        """
        Load sample transactions for testing.
        
        Returns:
            pd.DataFrame: Sample transaction data
        """
        filepath = self.data_dir / 'sample_transactions.csv'
        
        if not filepath.exists():
            print("⚠️  Sample data not found. Creating synthetic data...")
            return self._create_synthetic_data()
        
        print(f"📂 Loading sample data from: {filepath}")
        df = pd.read_csv(filepath)
        print(f"✅ Loaded {len(df)} sample transactions")
        
        return df
    
    def _create_synthetic_data(self, n_samples: int = 100) -> pd.DataFrame:
        """
        Create synthetic transaction data for testing.
        
        Args:
            n_samples: Number of synthetic transactions to generate
            
        Returns:
            pd.DataFrame: Synthetic transaction data
        """
        np.random.seed(42)
        
        # Generate synthetic features
        data = {
            'Time': np.random.randint(0, 172800, n_samples),  # 48 hours in seconds
            'Amount': np.random.exponential(100, n_samples),
        }
        
        # Add V1-V28 (PCA components)
        for i in range(1, 29):
            data[f'V{i}'] = np.random.randn(n_samples)
        
        # Generate fraud labels (10% fraud rate)
        data['Class'] = np.random.choice([0, 1], n_samples, p=[0.9, 0.1])
        
        df = pd.DataFrame(data)
        print(f"✅ Created {n_samples} synthetic transactions")
        
        return df
    
    def validate_data(self, df: pd.DataFrame) -> bool:
        """
        Validate dataset structure and quality.
        
        Args:
            df: DataFrame to validate
            
        Returns:
            bool: True if valid, raises exception otherwise
        """
        required_columns = ['Time', 'Amount', 'Class'] + [f'V{i}' for i in range(1, 29)]
        
        # Check required columns
        missing_cols = set(required_columns) - set(df.columns)
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
        
        # Check for null values
        null_counts = df.isnull().sum()
        if null_counts.any():
            print(f"⚠️  Warning: Found null values:\n{null_counts[null_counts > 0]}")
        
        # Check class distribution
        class_dist = df['Class'].value_counts()
        fraud_pct = (class_dist.get(1, 0) / len(df)) * 100
        
        print(f"\n📊 Data Validation Summary:")
        print(f"   ✅ All required columns present")
        print(f"   ✅ Shape: {df.shape}")
        print(f"   ✅ Class distribution:")
        print(f"      - Genuine (0): {class_dist.get(0, 0):,} ({100-fraud_pct:.2f}%)")
        print(f"      - Fraud (1): {class_dist.get(1, 0):,} ({fraud_pct:.2f}%)")
        
        return True
    
    def save_processed_data(self, df: pd.DataFrame, filename: str):
        """
        Save processed data to processed directory.
        
        Args:
            df: DataFrame to save
            filename: Name of output file (e.g., 'train.csv')
        """
        filepath = self.processed_dir / filename
        df.to_csv(filepath, index=False)
        print(f"💾 Saved processed data to: {filepath}")


# Quick usage example
if __name__ == "__main__":
    # Initialize loader
    loader = FraudDataLoader()
    
    # Try loading main dataset
    try:
        df = loader.load_creditcard_data()
        loader.validate_data(df)
    except FileNotFoundError:
        print("\n⚠️  Main dataset not found. Using sample data instead.")
        df = loader.load_sample_data()
        loader.validate_data(df)
    
    print("\n✅ Data loading successful!")
