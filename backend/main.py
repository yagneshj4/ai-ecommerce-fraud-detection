"""
FastAPI Backend for AI Fraud Detection System
==============================================
Team: Three Unknowns | VRSEC | Mini Project 2026

This is the main FastAPI application that serves the ML model.
Endpoints:
    - GET /: Health check
    - POST /predict: Fraud prediction endpoint
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import uvicorn
import numpy as np
from typing import List, Optional
import logging
from pathlib import Path

# Import our custom model loader
from model_loader import load_models, make_prediction

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="AI Fraud Detection API",
    description="Real-time fraud detection using Machine Learning",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI at /docs
    redoc_url="/redoc"  # ReDoc at /redoc
)

# CORS Configuration - Allow frontend to communicate
# In production, replace "*" with specific frontend URL
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # React dev server runs on http://localhost:5173
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load ML model on startup
try:
    model, scaler = load_models()
    logger.info("✅ Model loaded successfully!")
except Exception as e:
    logger.error(f"❌ Failed to load model: {e}")
    model, scaler = None, None


# ============================================================================
# REQUEST/RESPONSE SCHEMAS
# ============================================================================

class TransactionRequest(BaseModel):
    """
    Request schema for fraud prediction.
    
    Fields:
        Amount: Transaction amount in dollars
        Time: Seconds elapsed since first transaction
        V1-V28: PCA components (optional, default to 0)
    """
    Amount: float = Field(..., description="Transaction amount", ge=0)
    Time: float = Field(..., description="Time in seconds", ge=0)
    V1: Optional[float] = 0.0
    V2: Optional[float] = 0.0
    V3: Optional[float] = 0.0
    V4: Optional[float] = 0.0
    V5: Optional[float] = 0.0
    V6: Optional[float] = 0.0
    V7: Optional[float] = 0.0
    V8: Optional[float] = 0.0
    V9: Optional[float] = 0.0
    V10: Optional[float] = 0.0
    V11: Optional[float] = 0.0
    V12: Optional[float] = 0.0
    V13: Optional[float] = 0.0
    V14: Optional[float] = 0.0
    V15: Optional[float] = 0.0
    V16: Optional[float] = 0.0
    V17: Optional[float] = 0.0
    V18: Optional[float] = 0.0
    V19: Optional[float] = 0.0
    V20: Optional[float] = 0.0
    V21: Optional[float] = 0.0
    V22: Optional[float] = 0.0
    V23: Optional[float] = 0.0
    V24: Optional[float] = 0.0
    V25: Optional[float] = 0.0
    V26: Optional[float] = 0.0
    V27: Optional[float] = 0.0
    V28: Optional[float] = 0.0

    class Config:
        schema_extra = {
            "example": {
                "Amount": 25.50,
                "Time": 1000,
                "V1": 0.0,
                "V2": 0.0
            }
        }


class PredictionResponse(BaseModel):
    """
    Response schema for fraud prediction.
    
    Returns:
        prediction: "Fraud" or "Genuine"
        fraud_probability: Probability of fraud (0-100%)
        genuine_probability: Probability of genuine transaction
        risk_level: "VERY LOW", "LOW", "MEDIUM", "HIGH", "VERY HIGH"
        recommendation: Action recommendation
        confidence: Model confidence percentage
    """
    prediction: str
    fraud_probability: float
    genuine_probability: float
    risk_level: str
    recommendation: str
    confidence: float


# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.get("/")
async def root():
    """
    Health check endpoint.
    Returns API status and model availability.
    """
    return {
        "status": "active",
        "message": "AI Fraud Detection API is running",
        "model_loaded": model is not None,
        "version": "1.0.0",
        "endpoints": {
            "docs": "/docs",
            "predict": "/predict"
        }
    }


@app.post("/predict", response_model=PredictionResponse)
async def predict_fraud(transaction: TransactionRequest):
    """
    Predict whether a transaction is fraudulent.
    
    Args:
        transaction: Transaction details
        
    Returns:
        Prediction result with probability and recommendation
        
    Raises:
        HTTPException: If model is not loaded or prediction fails
    """
    
    # Check if model is loaded
    if model is None or scaler is None:
        raise HTTPException(
            status_code=503,
            detail="Model not loaded. Please check server logs."
        )
    
    try:
        # Convert request to feature array
        features = [
            transaction.Time,
            transaction.V1, transaction.V2, transaction.V3, transaction.V4,
            transaction.V5, transaction.V6, transaction.V7, transaction.V8,
            transaction.V9, transaction.V10, transaction.V11, transaction.V12,
            transaction.V13, transaction.V14, transaction.V15, transaction.V16,
            transaction.V17, transaction.V18, transaction.V19, transaction.V20,
            transaction.V21, transaction.V22, transaction.V23, transaction.V24,
            transaction.V25, transaction.V26, transaction.V27, transaction.V28,
            transaction.Amount
        ]
        
        # Make prediction
        prediction, fraud_prob = make_prediction(model, scaler, features)
        
        # Calculate metrics
        genuine_prob = (1 - fraud_prob) * 100
        fraud_prob_percent = fraud_prob * 100
        
        # Determine prediction label
        prediction_label = "Fraud" if prediction == 1 else "Genuine"
        
        # Determine risk level
        if fraud_prob_percent < 20:
            risk_level = "VERY LOW"
        elif fraud_prob_percent < 40:
            risk_level = "LOW"
        elif fraud_prob_percent < 60:
            risk_level = "MEDIUM"
        elif fraud_prob_percent < 80:
            risk_level = "HIGH"
        else:
            risk_level = "VERY HIGH"
        
        # Generate recommendation
        if prediction == 1:
            recommendation = "REJECT transaction. High fraud probability detected."
        else:
            if fraud_prob_percent < 20:
                recommendation = "APPROVE transaction. Appears genuine."
            else:
                recommendation = "REVIEW transaction manually before approval."
        
        # Calculate confidence (higher probability = higher confidence)
        confidence = max(fraud_prob_percent, genuine_prob)
        
        logger.info(f"Prediction: {prediction_label}, Fraud Prob: {fraud_prob_percent:.2f}%")
        
        return PredictionResponse(
            prediction=prediction_label,
            fraud_probability=round(fraud_prob_percent, 2),
            genuine_probability=round(genuine_prob, 2),
            risk_level=risk_level,
            recommendation=recommendation,
            confidence=round(confidence, 2)
        )
        
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )


# ============================================================================
# RUN SERVER
# ============================================================================

if __name__ == "__main__":
    """
    Run the FastAPI server using Uvicorn.
    
    Usage:
        python main.py
        
    Or:
        uvicorn main:app --reload --host 0.0.0.0 --port 8000
    """
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Auto-reload on code changes
        log_level="info"
    )
