"""
Model Evaluation Module
========================
Comprehensive evaluation and visualization of trained models.

Author: Team Three Unknowns
Date: January 2026
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    classification_report, 
    confusion_matrix, 
    roc_curve, 
    roc_auc_score,
    precision_recall_curve,
    average_precision_score
)
import joblib
from pathlib import Path


class FraudModelEvaluator:
    """
    Evaluate and visualize fraud detection model performance.
    """
    
    def __init__(self, model_path: str = None):
        """
        Initialize evaluator.
        
        Args:
            model_path: Path to saved model (optional)
        """
        self.model = None
        self.scaler = None
        
        if model_path:
            self.load_model(model_path)
    
    def load_model(self, model_dir: str):
        """
        Load model and associated artifacts.
        
        Args:
            model_dir: Directory containing model files
        """
        model_dir = Path(model_dir)
        
        # Load model
        model_path = model_dir / 'fraud_detector.pkl'
        self.model = joblib.load(model_path)
        print(f"✅ Model loaded from: {model_path}")
        
        # Load scaler
        scaler_path = model_dir / 'scaler.pkl'
        if scaler_path.exists():
            self.scaler = joblib.load(scaler_path)
            print(f"✅ Scaler loaded from: {scaler_path}")
    
    def generate_classification_report(self, y_true, y_pred) -> pd.DataFrame:
        """
        Generate detailed classification report.
        
        Args:
            y_true: True labels
            y_pred: Predicted labels
            
        Returns:
            DataFrame with metrics
        """
        print("\n" + "=" * 70)
        print("📊 CLASSIFICATION REPORT")
        print("=" * 70)
        
        report = classification_report(
            y_true, y_pred, 
            target_names=['Genuine', 'Fraud'],
            output_dict=True
        )
        
        df_report = pd.DataFrame(report).transpose()
        print(df_report)
        
        return df_report
    
    def plot_confusion_matrix(self, y_true, y_pred, save_path: str = None):
        """
        Plot and optionally save confusion matrix.
        
        Args:
            y_true: True labels
            y_pred: Predicted labels
            save_path: Path to save figure (optional)
        """
        cm = confusion_matrix(y_true, y_pred)
        
        plt.figure(figsize=(8, 6))
        sns.heatmap(
            cm, 
            annot=True, 
            fmt='d', 
            cmap='Blues',
            xticklabels=['Genuine', 'Fraud'],
            yticklabels=['Genuine', 'Fraud']
        )
        plt.title('Confusion Matrix - Fraud Detection', fontsize=14, fontweight='bold')
        plt.ylabel('Actual', fontsize=12)
        plt.xlabel('Predicted', fontsize=12)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"💾 Confusion matrix saved to: {save_path}")
        
        plt.show()
    
    def plot_roc_curve(self, y_true, y_pred_proba, save_path: str = None):
        """
        Plot ROC curve.
        
        Args:
            y_true: True labels
            y_pred_proba: Predicted probabilities for positive class
            save_path: Path to save figure (optional)
        """
        # Calculate ROC curve
        fpr, tpr, thresholds = roc_curve(y_true, y_pred_proba)
        roc_auc = roc_auc_score(y_true, y_pred_proba)
        
        # Plot
        plt.figure(figsize=(10, 6))
        plt.plot(fpr, tpr, color='darkblue', lw=2, label=f'ROC Curve (AUC = {roc_auc:.4f})')
        plt.plot([0, 1], [0, 1], color='gray', lw=1, linestyle='--', label='Random Classifier')
        
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate', fontsize=12)
        plt.ylabel('True Positive Rate (Recall)', fontsize=12)
        plt.title('ROC Curve - Fraud Detection Model', fontsize=14, fontweight='bold')
        plt.legend(loc='lower right', fontsize=11)
        plt.grid(alpha=0.3)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"💾 ROC curve saved to: {save_path}")
        
        plt.show()
    
    def plot_precision_recall_curve(self, y_true, y_pred_proba, save_path: str = None):
        """
        Plot Precision-Recall curve.
        
        Args:
            y_true: True labels
            y_pred_proba: Predicted probabilities
            save_path: Path to save figure (optional)
        """
        precision, recall, thresholds = precision_recall_curve(y_true, y_pred_proba)
        avg_precision = average_precision_score(y_true, y_pred_proba)
        
        plt.figure(figsize=(10, 6))
        plt.plot(recall, precision, color='darkgreen', lw=2, 
                label=f'PR Curve (AP = {avg_precision:.4f})')
        
        plt.xlabel('Recall', fontsize=12)
        plt.ylabel('Precision', fontsize=12)
        plt.title('Precision-Recall Curve', fontsize=14, fontweight='bold')
        plt.legend(loc='upper right', fontsize=11)
        plt.grid(alpha=0.3)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"💾 PR curve saved to: {save_path}")
        
        plt.show()
    
    def evaluate_at_different_thresholds(self, y_true, y_pred_proba):
        """
        Evaluate model performance at different probability thresholds.
        
        Args:
            y_true: True labels
            y_pred_proba: Predicted probabilities
            
        Returns:
            DataFrame with metrics at different thresholds
        """
        thresholds = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
        results = []
        
        for threshold in thresholds:
            y_pred_threshold = (y_pred_proba >= threshold).astype(int)
            cm = confusion_matrix(y_true, y_pred_threshold)
            tn, fp, fn, tp = cm.ravel()
            
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            recall = tp / (tp + fn) if (tp + fn) > 0 else 0
            f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
            
            results.append({
                'Threshold': threshold,
                'Precision': precision,
                'Recall': recall,
                'F1-Score': f1,
                'False Positives': fp,
                'False Negatives': fn
            })
        
        df_results = pd.DataFrame(results)
        
        print("\n📊 Performance at Different Thresholds:")
        print(df_results.to_string(index=False))
        
        return df_results
    
    def comprehensive_evaluation(self, X_test, y_test, output_dir: str = None):
        """
        Run complete evaluation pipeline with visualizations.
        
        Args:
            X_test: Test features
            y_test: Test labels
            output_dir: Directory to save plots (optional)
        """
        if self.model is None:
            raise ValueError("Model not loaded. Use load_model() first.")
        
        print("\n" + "=" * 70)
        print("🔍 COMPREHENSIVE MODEL EVALUATION")
        print("=" * 70)
        
        # Make predictions
        y_pred = self.model.predict(X_test)
        y_pred_proba = self.model.predict_proba(X_test)[:, 1]
        
        # 1. Classification Report
        self.generate_classification_report(y_test, y_pred)
        
        # 2. Confusion Matrix
        if output_dir:
            output_dir = Path(output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
            cm_path = output_dir / 'confusion_matrix.png'
        else:
            cm_path = None
        self.plot_confusion_matrix(y_test, y_pred, save_path=cm_path)
        
        # 3. ROC Curve
        if output_dir:
            roc_path = output_dir / 'roc_curve.png'
        else:
            roc_path = None
        self.plot_roc_curve(y_test, y_pred_proba, save_path=roc_path)
        
        # 4. Precision-Recall Curve
        if output_dir:
            pr_path = output_dir / 'precision_recall_curve.png'
        else:
            pr_path = None
        self.plot_precision_recall_curve(y_test, y_pred_proba, save_path=pr_path)
        
        # 5. Threshold Analysis
        self.evaluate_at_different_thresholds(y_test, y_pred_proba)
        
        print("\n✅ Evaluation complete!")


# Evaluation script
if __name__ == "__main__":
    from data_loader import FraudDataLoader
    from preprocessing import FraudPreprocessor
    
    print("\n🔍 Loading test data and model...")
    
    # Load and prepare test data
    loader = FraudDataLoader()
    try:
        df = loader.load_creditcard_data()
    except FileNotFoundError:
        df = loader.load_sample_data()
    
    # Preprocess
    preprocessor = FraudPreprocessor(test_size=0.2, random_state=42)
    processed_data = preprocessor.full_preprocessing_pipeline(df, apply_smote=False)
    
    # Evaluate
    model_dir = Path(__file__).parent.parent / 'models'
    evaluator = FraudModelEvaluator(model_path=model_dir)
    
    # Run comprehensive evaluation
    evaluator.comprehensive_evaluation(
        processed_data['X_test'], 
        processed_data['y_test'],
        output_dir='evaluation_results'
    )
