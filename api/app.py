"""
Flask REST API for Fraud Detection System
Team: Three Unknowns (Yagnesh, Bhaskar, Syam) | VRSEC

This API exposes the fraud detection model as a REST service.

Endpoints:
    POST /predict          - Predict fraud for a single transaction
    POST /predict/batch    - Predict fraud for multiple transactions
    GET  /health          - Health check
    GET  /                - API documentation

Run:
    python app.py

Access:
    http://localhost:5000
"""

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from utils import (  # type: ignore
    load_model,
    load_scaler,
    load_feature_names,
    preprocess_transaction,
    interpret_prediction
)

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend integration

# Load model at startup
print("🔧 Loading fraud detection model...")
try:
    # Fix path - use models/ from project root
    model_dir = Path(__file__).parent.parent / 'models'
    MODEL = load_model(str(model_dir / 'fraud_detector.pkl'))
    SCALER = load_scaler(str(model_dir / 'scaler.pkl'))
    FEATURE_NAMES = load_feature_names(str(model_dir / 'feature_names.pkl'))
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    print("Please train the model first using notebooks/02_Model_Training.ipynb")
    MODEL = None
    SCALER = None
    FEATURE_NAMES = None


# HTML template for API documentation
API_DOCS = """
<!DOCTYPE html>
<html>
<head>
    <title>Fraud Detection API</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1000px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }
        h2 {
            color: #34495e;
            margin-top: 30px;
        }
        .endpoint {
            background-color: #ecf0f1;
            padding: 15px;
            margin: 15px 0;
            border-left: 4px solid #3498db;
            border-radius: 5px;
        }
        .method {
            display: inline-block;
            padding: 5px 10px;
            border-radius: 3px;
            font-weight: bold;
            color: white;
            margin-right: 10px;
        }
        .get { background-color: #27ae60; }
        .post { background-color: #3498db; }
        code {
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 15px;
            display: block;
            border-radius: 5px;
            overflow-x: auto;
            margin: 10px 0;
        }
        .status {
            color: #27ae60;
            font-weight: bold;
        }
        .footer {
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #bdc3c7;
            text-align: center;
            color: #7f8c8d;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🛡️ Fraud Detection API</h1>
        <p><strong>Team:</strong> Three Unknowns (Yagnesh, Bhaskar, Syam)</p>
        <p><strong>Institution:</strong> VRSEC</p>
        <p><strong>Status:</strong> <span class="status">{{ status }}</span></p>
        
        <h2>📚 API Endpoints</h2>
        
        <div class="endpoint">
            <h3><span class="method get">GET</span> /health</h3>
            <p><strong>Description:</strong> Check API health status</p>
            <p><strong>Response:</strong></p>
            <code>{
  "status": "healthy",
  "model_loaded": true,
  "version": "1.0"
}</code>
        </div>
        
        <div class="endpoint">
            <h3><span class="method post">POST</span> /predict</h3>
            <p><strong>Description:</strong> Predict fraud for a single transaction</p>
            <p><strong>Request Body:</strong></p>
            <code>{
  "Time": 1000,
  "V1": 0.5,
  "V2": -0.3,
  "Amount": 149.99
}</code>
            <p><strong>Response:</strong></p>
            <code>{
  "prediction": "GENUINE",
  "fraud_probability": 0.0234,
  "confidence": 97.66,
  "risk_level": "VERY LOW",
  "recommendation": "APPROVE transaction. Appears genuine."
}</code>
        </div>
        
        <div class="endpoint">
            <h3><span class="method post">POST</span> /predict/batch</h3>
            <p><strong>Description:</strong> Predict fraud for multiple transactions</p>
            <p><strong>Request Body:</strong></p>
            <code>{
  "transactions": [
    {"Time": 1000, "Amount": 50.0, "V1": 0.1},
    {"Time": 2000, "Amount": 500.0, "V1": 2.5}
  ]
}</code>
            <p><strong>Response:</strong></p>
            <code>{
  "predictions": [
    {"prediction": "GENUINE", "fraud_probability": 0.02},
    {"prediction": "FRAUD", "fraud_probability": 0.87}
  ],
  "summary": {
    "total": 2,
    "fraud_count": 1,
    "genuine_count": 1
  }
}</code>
        </div>
        
        <h2>🧪 Test API</h2>
        <p>Use tools like:</p>
        <ul>
            <li><strong>Postman:</strong> https://www.postman.com/</li>
            <li><strong>cURL:</strong> Command line tool</li>
            <li><strong>Python requests:</strong> <code>import requests</code></li>
        </ul>
        
        <p><strong>Example cURL command:</strong></p>
        <code>curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"Time": 1000, "Amount": 149.99, "V1": 0.5}'</code>
        
        <div class="footer">
            <p>Fraud Detection API v1.0 | Mini Project 2026</p>
        </div>
    </div>
</body>
</html>
"""


@app.route('/')
def home():
    """Main fraud detection web interface"""
    return render_template('index.html')

@app.route('/docs')
def docs():
    """API documentation page"""
    status = "✅ Model Loaded" if MODEL is not None else "❌ Model Not Loaded"
    return render_template_string(API_DOCS, status=status)


@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint
    
    Returns:
        JSON with API status
    """
    return jsonify({
        'status': 'healthy',
        'model_loaded': MODEL is not None,
        'version': '1.0',
        'endpoints': {
            'predict': '/predict (POST)',
            'batch_predict': '/predict/batch (POST)',
            'health': '/health (GET)'
        }
    })


@app.route('/predict', methods=['POST'])
def predict_single():
    """
    Predict fraud for a single transaction
    
    Request JSON:
        {
            "Time": 1000,
            "V1": 0.5,
            "V2": -0.3,
            ...,
            "Amount": 149.99
        }
    
    Returns:
        JSON with prediction results
    """
    # Check if model is loaded
    if MODEL is None:
        return jsonify({
            'error': 'Model not loaded. Please train the model first.'
        }), 500
    
    # Get transaction data from request
    try:
        transaction_data = request.get_json()
        
        if not transaction_data:
            return jsonify({
                'error': 'No transaction data provided'
            }), 400
        
        # Preprocess transaction
        features = preprocess_transaction(
            transaction_data,
            SCALER,
            FEATURE_NAMES
        )
        
        # Make prediction
        prediction = MODEL.predict(features)[0]
        probability = MODEL.predict_proba(features)[0, 1]
        
        # Interpret results
        result = interpret_prediction(prediction, probability)
        
        # Add transaction details to response
        result['transaction'] = transaction_data
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'error': f'Prediction failed: {str(e)}'
        }), 500


@app.route('/predict/batch', methods=['POST'])
def predict_batch():
    """
    Predict fraud for multiple transactions
    
    Request JSON:
        {
            "transactions": [
                {"Time": 1000, "Amount": 50.0, ...},
                {"Time": 2000, "Amount": 500.0, ...}
            ]
        }
    
    Returns:
        JSON with batch prediction results
    """
    # Check if model is loaded
    if MODEL is None:
        return jsonify({
            'error': 'Model not loaded. Please train the model first.'
        }), 500
    
    try:
        # Get transactions from request
        data = request.get_json()
        
        if not data or 'transactions' not in data:
            return jsonify({
                'error': 'No transactions provided. Use format: {"transactions": [...]}'
            }), 400
        
        transactions = data['transactions']
        
        if not isinstance(transactions, list):
            return jsonify({
                'error': 'Transactions must be a list'
            }), 400
        
        # Convert to DataFrame
        df = pd.DataFrame(transactions)
        
        # Preprocess all transactions
        features = preprocess_transaction(df, SCALER, FEATURE_NAMES)
        
        # Make predictions
        predictions = MODEL.predict(features)
        probabilities = MODEL.predict_proba(features)[:, 1]
        
        # Prepare results
        results = []
        for i, (pred, prob) in enumerate(zip(predictions, probabilities)):
            result = interpret_prediction(pred, prob)
            result['transaction_index'] = i
            results.append(result)
        
        # Calculate summary
        fraud_count = int((predictions == 1).sum())
        genuine_count = len(predictions) - fraud_count
        
        return jsonify({
            'predictions': results,
            'summary': {
                'total': len(predictions),
                'fraud_count': fraud_count,
                'genuine_count': genuine_count,
                'fraud_percentage': round((fraud_count / len(predictions)) * 100, 2)
            }
        })
        
    except Exception as e:
        return jsonify({
            'error': f'Batch prediction failed: {str(e)}'
        }), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Endpoint not found',
        'message': 'Please check the API documentation at /'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal server error',
        'message': str(error)
    }), 500


if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("FRAUD DETECTION API SERVER")
    print("=" * 70)
    print("\n🚀 Starting server...")
    print("📍 API URL: http://localhost:5000")
    print("📚 Documentation: http://localhost:5000")
    print("\n💡 Press CTRL+C to stop the server")
    print("=" * 70 + "\n")
    
    # Run Flask app
    app.run(
        host='0.0.0.0',  # Accessible from network
        port=5000,
        debug=True  # Set to False in production
    )
