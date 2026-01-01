"""
Utility Functions for Fraud Detection System
Team: Three Unknowns | VRSEC

This module contains helper functions used across the project.
"""

import pandas as pd
import numpy as np
import joblib
from pathlib import Path
from typing import Dict, List, Union, Tuple


def load_model(model_path: str = '../models/fraud_detector.pkl'):
    """
    Load the trained fraud detection model.
    
    Args:
        model_path: Path to the saved model file
        
    Returns:
        Loaded model object
        
    Raises:
        FileNotFoundError: If model file doesn't exist
    """
    try:
        model = joblib.load(model_path)
        return model
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Model file not found at {model_path}. "
            "Please train the model first using 02_Model_Training.ipynb"
        )


def load_scaler(scaler_path: str = '../models/scaler.pkl'):
    """
    Load the feature scaler used during training.
    
    Args:
        scaler_path: Path to the saved scaler file
        
    Returns:
        Loaded scaler object
    """
    try:
        scaler = joblib.load(scaler_path)
        return scaler
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Scaler file not found at {scaler_path}. "
            "Please train the model first."
        )


def load_feature_names(feature_path: str = '../models/feature_names.pkl'):
    """
    Load the list of feature names used during training.
    
    Args:
        feature_path: Path to the saved feature names file
        
    Returns:
        List of feature names
    """
    try:
        features = joblib.load(feature_path)
        return features
    except FileNotFoundError:
        # Return default feature names if file doesn't exist
        print("Warning: Feature names file not found. Using default names.")
        return ['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 'Amount']


def preprocess_transaction(
    transaction_data: Union[Dict, pd.DataFrame],
    scaler,
    feature_names: List[str]
) -> np.ndarray:
    """
    Preprocess a transaction for prediction.
    
    Args:
        transaction_data: Dictionary or DataFrame with transaction features
        scaler: Fitted StandardScaler object
        feature_names: List of feature names in correct order
        
    Returns:
        Preprocessed feature array ready for prediction
    """
    # Convert dict to DataFrame if needed
    if isinstance(transaction_data, dict):
        df = pd.DataFrame([transaction_data])
    else:
        df = transaction_data.copy()
    
    # Ensure all required features are present
    for feature in feature_names:
        if feature not in df.columns:
            df[feature] = 0  # Fill missing features with 0
    
    # Select features in correct order
    df = df[feature_names]
    
    # Scale features
    scaled_features = scaler.transform(df)
    
    return scaled_features


def interpret_prediction(
    prediction: int,
    probability: float,
    threshold: float = 0.5
) -> Dict[str, Union[str, float, bool]]:
    """
    Interpret model prediction and provide human-readable output.
    
    Args:
        prediction: Model prediction (0 or 1)
        probability: Fraud probability (0.0 to 1.0)
        threshold: Decision threshold
        
    Returns:
        Dictionary with interpretation details
    """
    is_fraud = prediction == 1
    confidence = probability if is_fraud else (1 - probability)
    
    # Risk level based on probability
    if probability >= 0.8:
        risk_level = "HIGH"
    elif probability >= 0.5:
        risk_level = "MEDIUM"
    elif probability >= 0.3:
        risk_level = "LOW"
    else:
        risk_level = "VERY LOW"
    
    # Recommendation
    if is_fraud:
        if probability >= 0.9:
            recommendation = "BLOCK transaction immediately. Manual review required."
        elif probability >= 0.7:
            recommendation = "FLAG for manual review before processing."
        else:
            recommendation = "Monitor transaction. Consider additional verification."
    else:
        recommendation = "APPROVE transaction. Appears genuine."
    
    return {
        'prediction': 'FRAUD' if is_fraud else 'GENUINE',
        'fraud_probability': round(probability, 4),
        'confidence': round(confidence * 100, 2),
        'risk_level': risk_level,
        'recommendation': recommendation,
        'threshold': threshold
    }


def calculate_transaction_risk_score(
    amount: float,
    time_hour: int,
    previous_orders: int = 5
) -> float:
    """
    Calculate a simple risk score based on transaction characteristics.
    (Simplified version for demonstration)
    
    Args:
        amount: Transaction amount
        time_hour: Hour of day (0-23)
        previous_orders: Number of previous orders from this user
        
    Returns:
        Risk score (0.0 to 1.0)
    """
    risk_score = 0.0
    
    # High amount increases risk
    if amount > 1000:
        risk_score += 0.3
    elif amount > 500:
        risk_score += 0.2
    
    # Late night transactions are riskier
    if time_hour >= 22 or time_hour <= 5:
        risk_score += 0.2
    
    # New users are riskier
    if previous_orders < 3:
        risk_score += 0.3
    elif previous_orders < 10:
        risk_score += 0.1
    
    return min(risk_score, 1.0)


def format_currency(amount: float) -> str:
    """
    Format amount as currency string.
    
    Args:
        amount: Numerical amount
        
    Returns:
        Formatted currency string
    """
    return f"${amount:,.2f}"


def print_prediction_report(
    transaction_data: Dict,
    result: Dict
) -> None:
    """
    Print a formatted prediction report.
    
    Args:
        transaction_data: Original transaction data
        result: Prediction result dictionary
    """
    print("\n" + "=" * 70)
    print("FRAUD DETECTION REPORT")
    print("=" * 70)
    
    print("\n📊 Transaction Details:")
    for key, value in transaction_data.items():
        if key == 'Amount':
            print(f"   {key}: {format_currency(value)}")
        else:
            print(f"   {key}: {value}")
    
    print("\n🤖 Model Prediction:")
    print(f"   Result: {result['prediction']}")
    print(f"   Fraud Probability: {result['fraud_probability']} ({result['fraud_probability'] * 100:.2f}%)")
    print(f"   Confidence: {result['confidence']}%")
    print(f"   Risk Level: {result['risk_level']}")
    
    print(f"\n💡 Recommendation:")
    print(f"   {result['recommendation']}")
    
    print("\n" + "=" * 70)


def save_prediction_log(
    transaction_data: Dict,
    result: Dict,
    log_file: str = '../data/predictions_log.csv'
) -> None:
    """
    Save prediction to log file for tracking.
    
    Args:
        transaction_data: Original transaction data
        result: Prediction result
        log_file: Path to log file
    """
    import datetime
    
    log_entry = {
        'timestamp': datetime.datetime.now().isoformat(),
        **transaction_data,
        'prediction': result['prediction'],
        'fraud_probability': result['fraud_probability'],
        'risk_level': result['risk_level']
    }
    
    log_df = pd.DataFrame([log_entry])
    
    # Append to existing log or create new
    log_path = Path(log_file)
    if log_path.exists():
        log_df.to_csv(log_file, mode='a', header=False, index=False)
    else:
        log_df.to_csv(log_file, mode='w', header=True, index=False)


if __name__ == '__main__':
    # Test utility functions
    print("Testing utility functions...")
    
    # Test risk score calculation
    risk = calculate_transaction_risk_score(amount=1500, time_hour=23, previous_orders=2)
    print(f"\nRisk Score: {risk}")
    
    # Test currency formatting
    print(f"Formatted amount: {format_currency(1234.56)}")
    
    print("\n✅ Utility functions working correctly!")
