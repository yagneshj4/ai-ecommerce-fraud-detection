# FastAPI Backend Setup

## 📁 Backend Structure
```
backend/
├── main.py              # FastAPI application
├── model_loader.py      # Model loading utilities
├── requirements.txt     # Python dependencies
└── models/
    ├── fraud_detector.pkl
    └── scaler.pkl
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Run Server
```bash
# Method 1: Using uvicorn directly
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Method 2: Using Python
python main.py
```

### 3. Test API
Open browser: http://localhost:8000/docs

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/predict` | POST | Fraud prediction |
| `/docs` | GET | Swagger UI (Interactive API docs) |
| `/redoc` | GET | ReDoc documentation |

## 🧪 Test Prediction

Using cURL:
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d "{\"Amount\": 25.50, \"Time\": 1000}"
```

Expected Response:
```json
{
  "prediction": "Genuine",
  "fraud_probability": 2.34,
  "genuine_probability": 97.66,
  "risk_level": "VERY LOW",
  "recommendation": "APPROVE transaction. Appears genuine.",
  "confidence": 97.66
}
```

## 🔧 Troubleshooting

**Error: Model not found**
```
Solution: Ensure fraud_detector.pkl and scaler.pkl are in backend/models/
```

**Error: Port 8000 already in use**
```bash
# Change port
uvicorn main:app --reload --port 8001
```

**Error: CORS issues**
```
CORS is already configured in main.py for all origins.
In production, update allow_origins to specific frontend URL.
```
