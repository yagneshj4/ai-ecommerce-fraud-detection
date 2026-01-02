"""
Model Loader Module
===================
Handles loading and using the trained ML model.

Functions:
    - load_models(): Load fraud detection model and scaler
    - make_prediction(): Make fraud prediction for a transaction
"""

import joblib
import numpy as np
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


def load_models():
    """
    Load the trained fraud detection model and scaler.
    
    Returns:
        tuple: (model, scaler)
        
    Raises:
        FileNotFoundError: If model files are not found
        Exception: If model loading fails
    """
    try:
        # Get paths to model files
        base_dir = Path(__file__).parent
        model_path = base_dir / "models" / "fraud_detector.pkl"
        scaler_path = base_dir / "models" / "scaler.pkl"
        
        # Check if files exist
        if not model_path.exists():
            raise FileNotFoundError(f"Model not found at {model_path}")
        if not scaler_path.exists():
            raise FileNotFoundError(f"Scaler not found at {scaler_path}")
        
        # Load model and scaler
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        
        logger.info(f"✅ Model loaded from {model_path}")
        logger.info(f"✅ Scaler loaded from {scaler_path}")
        
        return model, scaler
        
    except FileNotFoundError as e:
        logger.error(f"❌ Model files not found: {e}")
        logger.error("Please ensure fraud_detector.pkl and scaler.pkl are in backend/models/")
        raise
    except Exception as e:
        logger.error(f"❌ Failed to load model: {e}")
        raise


def make_prediction(model, scaler, features):
    """
    Make a fraud prediction for a transaction.
    
    Args:
        model: Trained ML model
        scaler: Fitted StandardScaler
        features (list): Transaction features [Time, V1-V28, Amount]
        
    Returns:
        tuple: (prediction, fraud_probability)
            - prediction (int): 0 = Genuine, 1 = Fraud
            - fraud_probability (float): Probability of fraud (0.0 - 1.0)
            
    Example:
        >>> prediction, prob = make_prediction(model, scaler, [100, 0, 0, ..., 25.50])
        >>> print(f"Prediction: {prediction}, Probability: {prob:.2%}")
    """
    try:
        # Convert to numpy array
        features_array = np.array(features).reshape(1, -1)
        
        # Scale features
        features_scaled = scaler.transform(features_array)
        
        # Make prediction
        prediction = model.predict(features_scaled)[0]
        
        # Get probability (probability of fraud class)
        probabilities = model.predict_proba(features_scaled)[0]
        fraud_probability = probabilities[1]  # Index 1 is fraud class
        
        return int(prediction), float(fraud_probability)
        
    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        raise
