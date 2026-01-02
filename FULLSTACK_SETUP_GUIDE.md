# 🚀 FULL-STACK SETUP & DEMO GUIDE

**Modern Real-Time Fraud Detection System**  
**Team:** Three Unknowns | **Project:** Mini Project 2026

---

## 🏗️ SYSTEM ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERFACE                           │
│           (Browser - React + Tailwind CSS)                  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     │ HTTP Request (JSON)
                     │ POST /predict
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  FRONTEND (React + Vite)                    │
│  • TransactionForm.jsx - Input collection                  │
│  • ResultCard.jsx - Results display                        │
│  • api.js - Axios HTTP client                              │
│  • Port: 5173                                               │
└────────────────────┬────────────────────────────────────────┘
                     │
                     │ REST API Call
                     │ Axios POST
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  BACKEND (FastAPI)                          │
│  • main.py - API endpoints                                  │
│  • model_loader.py - ML model loading                       │
│  • CORS enabled for cross-origin requests                  │
│  • Port: 8000                                               │
└────────────────────┬────────────────────────────────────────┘
                     │
                     │ Load model
                     │ Scale features
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  ML MODEL (Scikit-learn)                    │
│  • fraud_detector.pkl - Logistic Regression                 │
│  • scaler.pkl - StandardScaler                              │
│  • 92% Recall | 97% ROC-AUC                                 │
└────────────────────┬────────────────────────────────────────┘
                     │
                     │ Return prediction
                     │ + probabilities
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    RESPONSE (JSON)                          │
│  {                                                          │
│    "prediction": "Genuine" / "Fraud",                       │
│    "fraud_probability": 2.34,                               │
│    "risk_level": "VERY LOW",                                │
│    "recommendation": "APPROVE transaction"                  │
│  }                                                          │
└─────────────────────────────────────────────────────────────┘
```

---

## 📦 COMPLETE INSTALLATION GUIDE

### Prerequisites
```bash
# Check installations
python --version    # 3.9+
node --version      # 18+
npm --version       # 9+
```

### Step 1: Backend Setup (5 minutes)

```bash
# Navigate to backend
cd C:\Users\HP\OneDrive\Desktop\mini\backend

# Install Python dependencies
pip install -r requirements.txt

# Verify model files exist
dir models
# Should show: fraud_detector.pkl, scaler.pkl

# Start FastAPI server
python main.py
```

**Expected Output:**
```
INFO:     ✅ Model loaded successfully!
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

**Test Backend:**
Open browser: http://localhost:8000/docs

### Step 2: Frontend Setup (5 minutes)

```bash
# Open NEW terminal (keep backend running)
cd C:\Users\HP\OneDrive\Desktop\mini\frontend

# Install Node dependencies
npm install

# Start React dev server
npm run dev
```

**Expected Output:**
```
  VITE v5.0.11  ready in 1234 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h to show help
```

**Access Application:**
Open browser: http://localhost:5173

---

## 🎬 DEMO SCRIPT FOR VIVA

### Opening Statement (30 seconds)
> "Good morning/afternoon. Our project is an **AI-Based Fraud Detection System** for e-commerce platforms. We've built a **real-time web application** using modern technologies like **React, FastAPI, and Machine Learning** to detect fraudulent transactions instantly."

### Live Demo (2 minutes)

#### Test 1: Genuine Transaction
1. Click **"✓ Genuine"** preset button
2. Show values populated: Amount = $25.50, Time = 1000
3. Click **"🔍 Analyze Transaction"**
4. **Point out:**
   - Loading animation (real-time processing)
   - Green result card appears
   - Fraud probability: ~2-5%
   - Risk level: VERY LOW
   - Recommendation: APPROVE

#### Test 2: Fraudulent Transaction
1. Click **"⚠️ Suspicious"** preset button
2. Show values: Amount = $2,500, Time = 5000
3. Click **"Analyze"**
4. **Point out:**
   - Red result card
   - Fraud probability: ~85-95%
   - Risk level: VERY HIGH
   - Recommendation: REJECT

#### Test 3: Show Architecture
1. Open **browser DevTools** (F12) → Network tab
2. Submit transaction
3. Show **POST request to /predict**
4. Show **JSON response from API**

### Technical Explanation (1 minute)

**Q: How does the system work?**

> "The frontend is built with **React** and **Vite** for fast development. When a user enters transaction details, the form data is sent via **Axios** to our **FastAPI backend** running on port 8000. The backend loads our trained **Logistic Regression model** using Scikit-learn, scales the features, makes a prediction, and returns the result as JSON. The frontend then displays the prediction in real-time with visual feedback."

**Q: Why React + FastAPI instead of plain HTML + Flask?**

> "We chose modern tools to demonstrate **industry best practices**:
> - **React**: Component-based UI, better state management, faster user experience
> - **Vite**: Lightning-fast hot reload during development
> - **FastAPI**: Automatic API documentation, async support, type validation with Pydantic
> - **Separation of concerns**: Frontend and backend can be deployed independently
> 
> This architecture is used by companies like Netflix, Uber, and Microsoft."

---

## 🎓 VIVA QUESTIONS & ANSWERS

### Technical Questions

**Q1: What is the technology stack?**
```
Frontend: React 18 + Vite + Tailwind CSS + Axios
Backend: FastAPI + Uvicorn + Python 3.9+
ML Model: Logistic Regression (Scikit-learn)
```

**Q2: How do frontend and backend communicate?**
```
• Frontend sends HTTP POST request with JSON data
• Backend receives request at /predict endpoint
• FastAPI validates data using Pydantic schemas
• Backend runs ML prediction and returns JSON response
• Frontend displays result using React state management
```

**Q3: What happens when user clicks "Analyze"?**
```
1. React collects form data
2. Axios sends POST to http://localhost:8000/predict
3. FastAPI receives and validates transaction data
4. Model loader scales features using StandardScaler
5. Logistic Regression model predicts fraud probability
6. Backend calculates risk level and recommendation
7. JSON response sent back to frontend
8. React updates UI with animated result card
```

**Q4: How is CORS handled?**
```
FastAPI middleware configured in main.py:
• allow_origins=["*"] - Allows requests from any origin
• allow_methods=["*"] - Allows POST, GET, etc.
• In production, we would restrict to specific frontend URL
```

**Q5: What are the model performance metrics?**
```
• Recall: 92% (catches 92% of fraud cases)
• Precision: 6% (due to high class imbalance)
• ROC-AUC: 97% (excellent discriminative ability)
• F1-Score: 0.11 (balanced metric)

We prioritize RECALL for fraud detection because:
- Missing fraud is more costly than false alarms
- High recall ensures maximum fraud detection
```

### Architecture Questions

**Q6: Why separate frontend and backend?**
```
Benefits:
• Independent scaling (frontend CDN, backend cloud)
• Technology flexibility (can change React to Vue later)
• Multiple frontends (web, mobile app, admin panel)
• Better security (API can have authentication)
• Team specialization (frontend vs backend developers)
```

**Q7: How would you deploy this in production?**
```
Frontend:
• Build: npm run build
• Deploy to: Vercel, Netlify, Azure Static Web Apps

Backend:
• Containerize with Docker
• Deploy to: Azure App Service, AWS Lambda, Heroku
• Use environment variables for configuration

Database:
• Add PostgreSQL for transaction logs
• Redis for caching predictions
```

**Q8: What are the limitations?**
```
Dataset:
• European credit card data (may not generalize globally)
• Imbalanced (0.17% fraud)
• PCA features are not interpretable

Model:
• Simple Logistic Regression (baseline)
• No real-time retraining
• Cannot explain predictions to users

System:
• No authentication/authorization
• No database for logging
• No fraud pattern analysis dashboard
```

### Academic Safety Questions

**Q9: Is this production-ready?**
```
"This is a DEMONSTRATION PROTOTYPE for academic evaluation.
For production deployment, we would need:
• User authentication (JWT tokens)
• Database for transaction logging
• Model monitoring and retraining pipeline
• Load balancing for high traffic
• Security hardening (rate limiting, input validation)
• Compliance with PCI-DSS for payment data"
```

**Q10: How is this different from your previous Flask version?**
```
Old (Flask + HTML):
• Server-side rendering (slower)
• Page reloads for predictions
• Tightly coupled frontend-backend
• Basic styling with vanilla CSS

New (React + FastAPI):
• Client-side rendering (faster UX)
• Real-time predictions without reload
• Separate deployable services
• Modern UI with Tailwind CSS
• Industry-standard architecture
```

---

## 🐛 COMMON ISSUES & FIXES

### Issue 1: Backend Not Starting
**Error:** `ModuleNotFoundError: No module named 'fastapi'`

**Fix:**
```bash
cd backend
pip install -r requirements.txt
```

### Issue 2: Model Not Found
**Error:** `FileNotFoundError: Model not found at backend/models/`

**Fix:**
```bash
# Copy models from old location
Copy-Item models\*.pkl backend\models\
```

### Issue 3: Frontend Can't Connect to Backend
**Error:** `Network Error / Cannot connect to API`

**Fix:**
1. Check backend is running: http://localhost:8000
2. Check CORS is enabled in main.py
3. Restart both servers

### Issue 4: Tailwind Styles Not Applying
**Error:** Page looks unstyled

**Fix:**
```bash
cd frontend
npm install -D tailwindcss postcss autoprefixer
npm run dev
```

### Issue 5: Port Already in Use
**Error:** `Port 8000 is already in use`

**Fix:**
```bash
# Find process using port
netstat -ano | findstr :8000

# Kill process (replace PID)
taskkill /PID <PID> /F

# Or change port in main.py
```

---

## 📸 SCREENSHOTS FOR SUBMISSION

Required screenshots:

1. ✅ **Backend API Documentation**
   - http://localhost:8000/docs
   - Shows Swagger UI with /predict endpoint

2. ✅ **Frontend Homepage**
   - http://localhost:5173
   - Shows full interface with form

3. ✅ **Genuine Transaction Result**
   - Green card with low fraud probability

4. ✅ **Fraudulent Transaction Result**
   - Red card with high fraud probability

5. ✅ **Network Tab (DevTools)**
   - Shows API request/response

6. ✅ **Terminal Outputs**
   - Backend running
   - Frontend running

7. ✅ **Project Structure**
   - File explorer showing backend/ and frontend/

---

## 📋 SUBMISSION CHECKLIST

### Files to Submit
- ✅ Complete `backend/` folder
- ✅ Complete `frontend/` folder
- ✅ `README.md` (updated)
- ✅ `models/` folder (fraud_detector.pkl, scaler.pkl)
- ✅ `notebooks/` (EDA and training)
- ✅ Screenshots folder
- ✅ Project report (PDF)

### Files to EXCLUDE
- ❌ `node_modules/` (too large)
- ❌ `__pycache__/`
- ❌ `.git/` (unless submitting as GitHub link)
- ❌ `frontend/dist/` (build output)
- ❌ Virtual environment folders

### Best Practice for Submission
```bash
# Create clean submission folder
mkdir submission
Copy-Item -Recurse backend submission\
Copy-Item -Recurse frontend\src submission\frontend\
Copy-Item frontend\package.json submission\frontend\
Copy-Item frontend\vite.config.js submission\frontend\
Copy-Item -Recurse models submission\
Copy-Item -Recurse notebooks submission\
Copy-Item README.md submission\

# Create ZIP
Compress-Archive -Path submission\* -DestinationPath ThreeUnknowns_FraudDetection.zip
```

---

## 🎯 MINI → MAJOR PROJECT ROADMAP

### Phase 1: Mini Project Extension (1-2 weeks)
- ✅ Add user authentication (login/register)
- ✅ Save predictions to SQLite database
- ✅ Add prediction history page
- ✅ Export results as CSV/PDF

### Phase 2: Major Project (3-4 months)
- ✅ Better models (Random Forest, XGBoost, Neural Networks)
- ✅ Real-time dashboard with charts (D3.js/Chart.js)
- ✅ Admin panel for managing rules
- ✅ Email alerts for high-risk transactions
- ✅ Batch processing (upload CSV of transactions)

### Phase 3: Startup / Imagine Cup (6+ months)
- ✅ Multi-tenant SaaS platform
- ✅ Integration with Shopify, WooCommerce APIs
- ✅ Mobile app (React Native)
- ✅ Advanced fraud detection (Graph Neural Networks)
- ✅ Explainable AI (SHAP values)
- ✅ Deploy on Azure/AWS with auto-scaling

---

## 🏆 KEY POINTS FOR MARKS

### Innovation (25%)
✅ Modern full-stack architecture  
✅ Real-time predictions  
✅ Industry-standard tools  

### Implementation (30%)
✅ Clean, working code  
✅ Proper separation of concerns  
✅ Error handling  

### Documentation (20%)
✅ Clear README files  
✅ Code comments  
✅ Architecture diagrams  

### Demo (25%)
✅ Smooth live demonstration  
✅ Multiple test cases  
✅ Technical explanation  

---

**Good luck with your viva! 🎓**

*This system demonstrates real-world applicability while remaining appropriate for academic evaluation.*
