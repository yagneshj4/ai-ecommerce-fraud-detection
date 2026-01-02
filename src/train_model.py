"""
Model Training Module
=====================
Train and save machine learning models for fraud detection.

Author: Team Three Unknowns
Date: January 2026
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import joblib
from pathlib import Path
from datetime import datetime


class FraudModelTrainer:
    """
    Train and manage fraud detection models.
    
    Supports:
    - Logistic Regression (baseline)
    - Random Forest (advanced)
    """
    
    def __init__(self, model_type: str = 'logistic', random_state: int = 42):
        """
        Initialize model trainer.
        
        Args:
            model_type: 'logistic' or 'random_forest'
            random_state: Random seed for reproducibility
        """
        self.model_type = model_type
        self.random_state = random_state
        self.model = None
        self.training_history = {}
        
        # Initialize model
        self._initialize_model()
    
    def _initialize_model(self):
        """Create model based on type."""
        if self.model_type == 'logistic':
            self.model = LogisticRegression(
                random_state=self.random_state,
                max_iter=1000,
                solver='lbfgs',
                class_weight='balanced'  # Handle any remaining imbalance
            )
            print("🤖 Initialized Logistic Regression model")
            
        elif self.model_type == 'random_forest':
            self.model = RandomForestClassifier(
                n_estimators=100,
                random_state=self.random_state,
                max_depth=10,
                min_samples_split=10,
                class_weight='balanced',
                n_jobs=-1  # Use all CPU cores
            )
            print("🌲 Initialized Random Forest model (100 trees)")
            
        else:
            raise ValueError(f"Unknown model type: {self.model_type}")
    
    def train(self, X_train: np.ndarray, y_train: np.ndarray):
        """
        Train the model on provided data.
        
        Args:
            X_train: Training features
            y_train: Training labels
        """
        print("\n" + "=" * 70)
        print("🎯 TRAINING MODEL")
        print("=" * 70)
        
        print(f"\n📊 Training data:")
        print(f"   Samples: {len(X_train):,}")
        print(f"   Features: {X_train.shape[1]}")
        
        # Record training start
        start_time = datetime.now()
        
        # Train model
        print(f"\n⏳ Training {self.model_type} model...")
        self.model.fit(X_train, y_train)
        
        # Record training end
        end_time = datetime.now()
        training_time = (end_time - start_time).total_seconds()
        
        print(f"✅ Training complete in {training_time:.2f} seconds")
        
        # Store training metadata
        self.training_history = {
            'model_type': self.model_type,
            'n_samples': len(X_train),
            'n_features': X_train.shape[1],
            'training_time_seconds': training_time,
            'trained_at': end_time.isoformat()
        }
        
        return self.model
    
    def evaluate(self, X_test: np.ndarray, y_test: np.ndarray) -> dict:
        """
        Evaluate model performance on test data.
        
        Args:
            X_test: Test features
            y_test: Test labels
            
        Returns:
            Dictionary of performance metrics
        """
        print("\n" + "=" * 70)
        print("📊 MODEL EVALUATION")
        print("=" * 70)
        
        # Make predictions
        y_pred = self.model.predict(X_test)
        y_pred_proba = self.model.predict_proba(X_test)[:, 1]
        
        # Calculate metrics
        print("\n📈 Classification Report:")
        print(classification_report(y_test, y_pred, target_names=['Genuine', 'Fraud']))
        
        # Confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        print("\n🔍 Confusion Matrix:")
        print("                Predicted")
        print("              Genuine  Fraud")
        print(f"Actual Genuine  {cm[0][0]:6d}  {cm[0][1]:5d}")
        print(f"       Fraud    {cm[1][0]:6d}  {cm[1][1]:5d}")
        
        # ROC-AUC Score
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        print(f"\n🎯 ROC-AUC Score: {roc_auc:.4f}")
        
        # Calculate key metrics manually
        tn, fp, fn, tp = cm.ravel()
        
        accuracy = (tp + tn) / (tp + tn + fp + fn)
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        
        metrics = {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1,
            'roc_auc': roc_auc,
            'confusion_matrix': cm.tolist(),
            'true_positives': int(tp),
            'true_negatives': int(tn),
            'false_positives': int(fp),
            'false_negatives': int(fn)
        }
        
        print(f"\n✅ Model Performance Summary:")
        print(f"   Accuracy:  {accuracy:.4f}")
        print(f"   Precision: {precision:.4f}")
        print(f"   Recall:    {recall:.4f}")
        print(f"   F1-Score:  {f1:.4f}")
        print(f"   ROC-AUC:   {roc_auc:.4f}")
        
        return metrics
    
    def save_model(self, model_dir: str, feature_names: list = None):
        """
        Save trained model to disk.
        
        Args:
            model_dir: Directory to save model
            feature_names: List of feature names (optional)
        """
        model_dir = Path(model_dir)
        model_dir.mkdir(parents=True, exist_ok=True)
        
        # Save model
        model_path = model_dir / 'fraud_detector.pkl'
        joblib.dump(self.model, model_path)
        print(f"\n💾 Model saved to: {model_path}")
        
        # Save feature names if provided
        if feature_names:
            features_path = model_dir / 'feature_names.pkl'
            joblib.dump(feature_names, features_path)
            print(f"💾 Feature names saved to: {features_path}")
        
        # Save training history
        history_path = model_dir / 'training_history.pkl'
        joblib.dump(self.training_history, history_path)
        print(f"💾 Training history saved to: {history_path}")
    
    def load_model(self, model_path: str):
        """Load trained model from disk."""
        self.model = joblib.load(model_path)
        print(f"📂 Model loaded from: {model_path}")
        return self.model


# Training script
if __name__ == "__main__":
    from data_loader import FraudDataLoader
    from preprocessing import FraudPreprocessor
    
    print("\n" + "=" * 70)
    print("🚀 FRAUD DETECTION MODEL TRAINING")
    print("=" * 70)
    
    # 1. Load data
    print("\n📂 Step 1: Loading data...")
    loader = FraudDataLoader()
    try:
        df = loader.load_creditcard_data()
    except FileNotFoundError:
        print("⚠️  Using sample data for demo")
        df = loader.load_sample_data()
    
    # 2. Preprocess data
    print("\n🔧 Step 2: Preprocessing...")
    preprocessor = FraudPreprocessor(test_size=0.2, random_state=42)
    processed_data = preprocessor.full_preprocessing_pipeline(df, apply_smote=True)
    
    # 3. Train model
    print("\n🎯 Step 3: Training model...")
    trainer = FraudModelTrainer(model_type='logistic', random_state=42)
    trainer.train(processed_data['X_train'], processed_data['y_train'])
    
    # 4. Evaluate model
    print("\n📊 Step 4: Evaluating model...")
    metrics = trainer.evaluate(processed_data['X_test'], processed_data['y_test'])
    
    # 5. Save model and scaler
    print("\n💾 Step 5: Saving model...")
    model_dir = Path(__file__).parent.parent / 'models'
    trainer.save_model(model_dir, feature_names=processed_data['feature_names'])
    preprocessor.save_scaler(model_dir / 'scaler.pkl')
    
    print("\n" + "=" * 70)
    print("✅ TRAINING PIPELINE COMPLETE!")
    print("=" * 70)
    print(f"\n📁 Saved files in: {model_dir}")
    print(f"   - fraud_detector.pkl")
    print(f"   - scaler.pkl")
    print(f"   - feature_names.pkl")
    print(f"   - training_history.pkl")
    print(f"\n🎯 Model is ready for predictions!")
