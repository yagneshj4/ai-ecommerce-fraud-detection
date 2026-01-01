"""
Fraud Detection Prediction Script
Team: Three Unknowns (Yagnesh, Bhaskar, Syam) | VRSEC

This script loads the trained model and makes predictions on new transactions.

Usage:
    python predict.py                    # Interactive mode
    python predict.py --batch <file>     # Batch prediction mode
"""

import sys
import argparse
import pandas as pd
import numpy as np
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent))

from utils import (
    load_model,
    load_scaler,
    load_feature_names,
    preprocess_transaction,
    interpret_prediction,
    print_prediction_report,
    save_prediction_log
)


class FraudDetector:
    """
    Fraud Detection System
    
    Loads trained model and makes predictions on new transactions.
    """
    
    def __init__(self, model_dir: str = None):
        """
        Initialize fraud detector by loading model and preprocessing components.
        
        Args:
            model_dir: Directory containing saved model files (defaults to project models/)
        """
        # Use absolute path relative to script location
        if model_dir is None:
            script_dir = Path(__file__).parent
            self.model_dir = script_dir.parent / 'models'
        else:
            self.model_dir = Path(model_dir)
        
        print("🔧 Loading fraud detection system...")
        
        try:
            # Load model components
            self.model = load_model(str(self.model_dir / 'fraud_detector.pkl'))
            self.scaler = load_scaler(str(self.model_dir / 'scaler.pkl'))
            self.feature_names = load_feature_names(str(self.model_dir / 'feature_names.pkl'))
            
            print(f"✅ Model loaded successfully!")
            print(f"📊 Features required: {len(self.feature_names)}")
            
        except FileNotFoundError as e:
            print(f"❌ Error: {e}")
            print("\n💡 Please train the model first:")
            print("   1. Open notebooks/02_Model_Training.ipynb")
            print("   2. Run all cells to train and save the model")
            sys.exit(1)
    
    def predict_single(self, transaction_data: dict, verbose: bool = True) -> dict:
        """
        Predict fraud for a single transaction.
        
        Args:
            transaction_data: Dictionary with transaction features
            verbose: Whether to print detailed report
            
        Returns:
            Dictionary with prediction results
        """
        # Preprocess transaction
        features = preprocess_transaction(
            transaction_data,
            self.scaler,
            self.feature_names
        )
        
        # Make prediction
        prediction = self.model.predict(features)[0]
        probability = self.model.predict_proba(features)[0, 1]
        
        # Interpret results
        result = interpret_prediction(prediction, probability)
        
        # Print report if verbose
        if verbose:
            print_prediction_report(transaction_data, result)
        
        return result
    
    def predict_batch(self, data: pd.DataFrame, output_file: str = None) -> pd.DataFrame:
        """
        Predict fraud for multiple transactions.
        
        Args:
            data: DataFrame with transaction data
            output_file: Optional path to save results
            
        Returns:
            DataFrame with predictions
        """
        print(f"\n🔄 Processing {len(data)} transactions...")
        
        # Preprocess all transactions
        features = preprocess_transaction(
            data,
            self.scaler,
            self.feature_names
        )
        
        # Make predictions
        predictions = self.model.predict(features)
        probabilities = self.model.predict_proba(features)[:, 1]
        
        # Add results to dataframe
        results = data.copy()
        results['Prediction'] = ['FRAUD' if p == 1 else 'GENUINE' for p in predictions]
        results['Fraud_Probability'] = probabilities
        results['Risk_Level'] = pd.cut(
            probabilities,
            bins=[0, 0.3, 0.5, 0.8, 1.0],
            labels=['VERY LOW', 'LOW', 'MEDIUM', 'HIGH']
        )
        
        # Summary
        fraud_count = (predictions == 1).sum()
        print(f"\n✅ Batch prediction completed!")
        print(f"   - Total transactions: {len(data)}")
        print(f"   - Predicted as FRAUD: {fraud_count} ({fraud_count/len(data)*100:.2f}%)")
        print(f"   - Predicted as GENUINE: {len(data) - fraud_count}")
        
        # Save results if output file specified
        if output_file:
            results.to_csv(output_file, index=False)
            print(f"\n💾 Results saved to: {output_file}")
        
        return results


def interactive_mode():
    """
    Interactive mode: User inputs transaction details manually.
    """
    print("\n" + "=" * 70)
    print("INTERACTIVE FRAUD DETECTION")
    print("=" * 70)
    
    # Initialize detector
    detector = FraudDetector()
    
    print("\n📝 Enter transaction details (or type 'quit' to exit):")
    
    while True:
        print("\n" + "-" * 70)
        
        try:
            # Simple input mode (basic features)
            print("\n💡 Simplified Input Mode:")
            print("   Enter key transaction details. Other features will be set to 0.")
            
            # Get transaction amount
            amount_input = input("\n1️⃣ Transaction Amount ($): ").strip()
            if amount_input.lower() == 'quit':
                break
            
            try:
                amount = float(amount_input)
            except ValueError:
                print("❌ Invalid amount. Using $100 as default.")
                amount = 100.0
            
            # Get time (optional)
            time_input = input("2️⃣ Time since account creation (seconds, press Enter to skip): ").strip()
            time = float(time_input) if time_input and time_input != 'quit' else 0.0
            
            if time_input and time_input.lower() == 'quit':
                break
            
            # Create transaction dictionary
            # For demo, we'll use simplified features
            transaction = {
                'Time': time,
                'Amount': amount
            }
            
            # Add V1-V28 features with default values (0)
            # In real scenario, these would come from PCA transformation
            for i in range(1, 29):
                feature_name = f'V{i}'
                if feature_name in detector.feature_names:
                    transaction[feature_name] = 0.0
            
            # Make prediction
            result = detector.predict_single(transaction, verbose=True)
            
            # Ask if user wants to continue
            continue_input = input("\n🔄 Analyze another transaction? (y/n): ").strip().lower()
            if continue_input != 'y':
                break
                
        except KeyboardInterrupt:
            print("\n\n👋 Exiting...")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            continue
    
    print("\n👋 Thank you for using the Fraud Detection System!")


def batch_mode(input_file: str, output_file: str = None):
    """
    Batch mode: Process transactions from CSV file.
    
    Args:
        input_file: Path to CSV file with transactions
        output_file: Path to save results (optional)
    """
    print("\n" + "=" * 70)
    print("BATCH FRAUD DETECTION")
    print("=" * 70)
    
    # Initialize detector
    detector = FraudDetector()
    
    # Load data
    try:
        data = pd.read_csv(input_file)
        print(f"\n✅ Loaded {len(data)} transactions from {input_file}")
    except FileNotFoundError:
        print(f"❌ Error: File not found - {input_file}")
        return
    except Exception as e:
        print(f"❌ Error loading file: {e}")
        return
    
    # Make predictions
    results = detector.predict_batch(data, output_file)
    
    # Show sample results
    print("\n📊 Sample Results (first 10):")
    display_cols = ['Amount', 'Prediction', 'Fraud_Probability', 'Risk_Level']
    available_cols = [col for col in display_cols if col in results.columns]
    print(results[available_cols].head(10).to_string(index=False))


def demo_mode():
    """
    Demo mode: Show example predictions with pre-defined transactions.
    """
    print("\n" + "=" * 70)
    print("DEMO MODE - Example Predictions")
    print("=" * 70)
    
    # Initialize detector
    detector = FraudDetector()
    
    # Create demo transactions
    demo_transactions = [
        {
            'name': 'Small genuine purchase',
            'Time': 1000,
            'Amount': 25.50,
            'V1': 0.1,
            'V2': -0.2
        },
        {
            'name': 'Large suspicious purchase',
            'Time': 5000,
            'Amount': 2500.00,
            'V1': 2.5,
            'V2': 3.1
        },
        {
            'name': 'Medium transaction',
            'Time': 3000,
            'Amount': 150.00,
            'V1': -0.5,
            'V2': 0.3
        }
    ]
    
    # Add missing features
    for trans in demo_transactions:
        for i in range(1, 29):
            feature_name = f'V{i}'
            if feature_name not in trans and feature_name in detector.feature_names:
                trans[feature_name] = 0.0
    
    # Make predictions
    for i, trans in enumerate(demo_transactions, 1):
        trans_name = trans.pop('name')
        print(f"\n{'='*70}")
        print(f"DEMO TRANSACTION {i}: {trans_name}")
        print(f"{'='*70}")
        
        result = detector.predict_single(trans, verbose=True)


def main():
    """
    Main entry point for the prediction script.
    """
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='Fraud Detection Prediction System',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python predict.py                          # Interactive mode
  python predict.py --demo                   # Demo mode with examples
  python predict.py --batch input.csv        # Batch prediction
  python predict.py --batch input.csv --output results.csv
        """
    )
    
    parser.add_argument(
        '--batch',
        type=str,
        help='Batch mode: Path to CSV file with transactions'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        help='Output file for batch predictions (CSV)'
    )
    
    parser.add_argument(
        '--demo',
        action='store_true',
        help='Run demo mode with example transactions'
    )
    
    args = parser.parse_args()
    
    # Determine mode
    if args.demo:
        demo_mode()
    elif args.batch:
        batch_mode(args.batch, args.output)
    else:
        interactive_mode()


if __name__ == '__main__':
    main()
