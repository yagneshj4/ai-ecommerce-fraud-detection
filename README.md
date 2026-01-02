# AI-Based Detection of Fake Orders and User Abuse in E-Commerce Platforms

**Team:** Three Unknowns (Yagnesh, Bhaskar, Syam)  
**Institution:** Velagapudi Ramakrishna Siddhartha Engineering College (VRSEC)  
**Department:** Information Technology (3rd Year)  
**Project Type:** Mini Project  
**Date:** January 2026

---

## 📋 Problem Statement

E-commerce platforms face significant financial losses due to fraudulent activities including fake orders, payment fraud, and user abuse. Traditional rule-based detection systems are inadequate because fraudsters constantly evolve their tactics, making static rules obsolete. Manual review is time-consuming and cannot scale to handle millions of daily transactions. Fraudulent activities include unauthorized credit card usage, fake account creation for promotional abuse, return fraud, and coordinated bot attacks.

This project implements an **AI-based fraud detection system** using machine learning to automatically identify suspicious orders in real-time. Unlike rule-based systems, machine learning models can detect complex patterns, adapt to new fraud tactics, and handle high-volume transactions efficiently. The system analyzes transaction features (order value, payment method, user history, device information) to predict whether an order is genuine or fraudulent, helping businesses reduce losses, protect legitimate customers, and maintain platform integrity.

**Scope:** This mini project focuses on binary classification (Fraud vs. Genuine) using supervised learning with historical transaction data.

---

## 🎯 Project Objectives

1. **Primary Goal:** Build a machine learning model to classify e-commerce transactions as fraudulent or genuine
2. **Secondary Goals:**
   - Perform exploratory data analysis on transaction patterns
   - Handle imbalanced datasets (fraud is typically <5% of transactions)
   - Implement feature engineering for better prediction accuracy
   - Create a simple prediction system for new transactions
   - Document the entire process for academic evaluation

---

## 🏗️ Project Structure

```
mini/
│
├── backend/                       # FastAPI Backend (NEW!)
│   ├── main.py                    # FastAPI application with /predict endpoint
│   ├── model_loader.py            # ML model loading utilities
│   ├── requirements.txt           # Backend dependencies
│   ├── README.md                  # Backend setup guide
│   └── models/
│       ├── fraud_detector.pkl     # Trained Logistic Regression model
│       └── scaler.pkl             # StandardScaler for feature normalization
│
├── frontend/                      # React Frontend (NEW!)
│   ├── package.json               # Node dependencies
│   ├── vite.config.js             # Vite configuration
│   ├── tailwind.config.js         # Tailwind CSS config
│   ├── index.html                 # HTML entry point
│   ├── README.md                  # Frontend setup guide
│   └── src/
│       ├── main.jsx               # React entry point
│       ├── App.jsx                # Main application component
│       ├── index.css              # Global styles + Tailwind
│       ├── components/
│       │   ├── TransactionForm.jsx  # Transaction input form
│       │   └── ResultCard.jsx       # Prediction results display
│       └── services/
│           └── api.js             # Axios API client
│
├── data/                          # Dataset storage
│   ├── raw/                       # Original dataset files
│   │   └── creditcard.csv
│   └── sample_transactions.csv
│
├── notebooks/                     # Jupyter notebooks for analysis
│   ├── 01_EDA.ipynb              # Exploratory Data Analysis
│   └── 02_Model_Training.ipynb    # Model development & evaluation
│
├── src/                           # Python utilities
│   ├── predict.py                 # Prediction script (legacy)
│   └── utils.py                   # Helper functions
│
├── models/                        # Original model location
│   ├── fraud_detector.pkl
│   └── scaler.pkl
│
├── api/                           # Flask API (legacy - replaced by backend/)
│   ├── app.py
│   └── templates/
│
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation (this file)
├── FULLSTACK_SETUP_GUIDE.md      # Complete setup & demo guide (NEW!)
└── PROJECT_PROPOSAL.md            # Initial project proposal
```

### 📂 Folder Descriptions

| Folder | Purpose |
|--------|---------|
| **backend/** | **FastAPI REST API** - Modern Python backend with async support, automatic docs, and type validation |
| **frontend/** | **React Web App** - Modern UI built with Vite + React + Tailwind CSS for real-time predictions |
| **data/** | Stores raw and processed datasets. Raw data is kept separate for reproducibility |
| **notebooks/** | Interactive Jupyter notebooks for analysis, visualization, and model training |
| **src/** | Production-ready Python scripts for predictions and utilities (legacy) |
| **models/** | Stores trained ML models as `.pkl` files for reuse |
| **api/** | Flask API (legacy - use backend/ instead for new development) |

---

## 🔬 Technology Stack

### Core Technologies
- **Language:** Python 3.9+
- **ML Framework:** Scikit-learn
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Model Persistence:** Joblib

### Modern Full-Stack Architecture (NEW!)

**Backend:**
- **Framework:** FastAPI (modern async Python framework)
- **Server:** Uvicorn (ASGI server)
- **Validation:** Pydantic (type validation)
- **API Docs:** Swagger UI (automatic)
- **Port:** 8000

**Frontend:**
- **Framework:** React 18 (component-based UI)
- **Build Tool:** Vite (lightning-fast hot reload)
- **Styling:** Tailwind CSS (utility-first CSS)
- **HTTP Client:** Axios (promise-based requests)
- **Port:** 5173

**Architecture:**
```
React Frontend (5173) → HTTP Request → FastAPI Backend (8000) → ML Model → JSON Response
```

### Why Modern Stack?

| Technology | Why Chosen |
|------------|------------|
| **React** | Component reusability, state management, industry standard |
| **Vite** | 10x faster than Create React App, instant hot reload |
| **FastAPI** | Automatic API docs, async support, type safety, 3x faster than Flask |
| **Tailwind** | Rapid UI development, consistent design, no custom CSS needed |

### Deployment Options
- **Frontend:** Vercel, Netlify, Azure Static Web Apps (free tier)
- **Backend:** Azure App Service, AWS Lambda, Heroku (using Student credits)
- **Cloud Storage:** Azure Blob Storage (for datasets)

---

## 📊 Dataset Information

**Dataset:** [Credit Card Fraud Detection (Kaggle)](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

**Alternative:** E-commerce Transaction Dataset (synthetic or real)

### Features
- **Transaction Amount:** Order value in currency
- **Payment Method:** Credit card, debit card, UPI, COD
- **User History:** Number of previous orders, account age
- **Device Information:** Device type, IP address geolocation
- **Time Features:** Hour of day, day of week
- **Behavioral Features:** Time since last order, cart abandonment rate

### Target Variable
- **Class:** 0 = Genuine, 1 = Fraud

### Data Characteristics
- **Imbalanced:** Fraud cases typically 1-5% of total transactions
- **Size:** 10,000+ transactions (sufficient for mini project)
- **Format:** CSV file

---

## 🚀 Getting Started

### Quick Start (Modern Full-Stack)

#### Option 1: Run Full Application (Recommended)

**Terminal 1 - Backend:**
```bash
cd backend
pip install -r requirements.txt
python main.py
```
Backend runs at: http://localhost:8000

**Terminal 2 - Frontend:**
```bash
cd frontend
npm install
npm run dev
```
Frontend runs at: http://localhost:5173

**Access:** Open browser to http://localhost:5173

---

#### Option 2: Traditional Approach (Notebooks)

### Step 1: Clone/Download Project
```bash
cd c:\Users\HP\OneDrive\Desktop\mini
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Download Dataset
- Go to [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Download `creditcard.csv`
- Place in `data/raw/` folder

### Step 4: Run Exploratory Data Analysis
```bash
# Open Jupyter Notebook
jupyter notebook notebooks/01_EDA.ipynb
```

### Step 5: Train the Model
```bash
# Open training notebook
jupyter notebook notebooks/02_Model_Training.ipynb
```

### Step 6: Test Predictions
```bash
# Run prediction script
python src/predict.py
```

---

## 📖 Complete Setup Guide

For detailed setup instructions, viva preparation, troubleshooting, and demo script:

**👉 See [FULLSTACK_SETUP_GUIDE.md](FULLSTACK_SETUP_GUIDE.md)**

Includes:
- System architecture diagram
- Step-by-step installation
- 10 guaranteed viva questions + answers
- Common issues & fixes
- Demo script (2-minute presentation)
- Submission checklist

---

## 🧠 Machine Learning Approach

### Why Logistic Regression for Mini Project?

**Chosen Algorithm:** Logistic Regression (baseline model)

**Justification:**
1. **Simplicity:** Easy to understand and explain in viva/presentation
2. **Interpretability:** Coefficients show which features contribute to fraud
3. **Fast Training:** Trains in seconds even on large datasets
4. **Good Baseline:** Achieves 85-90% accuracy on balanced fraud datasets
5. **No Hyperparameter Tuning:** Minimal configuration required
6. **Low Resource Usage:** Works on standard laptops without GPU

**For Advanced Version (Major Project):**
- Random Forest (ensemble learning)
- XGBoost (gradient boosting)
- Neural Networks (deep learning)

---

## 📈 Model Evaluation Metrics

| Metric | What it Measures | Why Important for Fraud Detection |
|--------|------------------|-----------------------------------|
| **Accuracy** | Overall correctness | Can be misleading with imbalanced data |
| **Precision** | % of fraud predictions that are correct | Minimizes false alarms |
| **Recall** | % of actual frauds detected | Catches maximum fraud cases |
| **F1-Score** | Balance between precision and recall | Best single metric for imbalanced data |
| **ROC-AUC** | Model's ability to distinguish classes | Measures overall discriminative power |

**Target Performance (Mini Project):**
- Recall (Fraud Detection Rate): >80%
- Precision: >70%
- F1-Score: >0.75

---

## 🎓 Viva/Presentation Guide

### Key Questions & Answers

**Q1: Why did you choose this problem?**  
*A: E-commerce fraud causes billions in losses annually. AI can detect patterns humans miss and scale to millions of transactions. This project demonstrates practical ML application in fintech security.*

**Q2: Why React + FastAPI instead of simple HTML + Flask?**  
*A: Modern industry practices:*
- **React:** Component reusability, better state management, faster UX (no page reloads)
- **FastAPI:** Automatic API documentation, async support, type validation with Pydantic
- **Separation:** Frontend and backend can be deployed independently (microservices architecture)
- **Scalability:** Used by companies like Netflix, Uber, Microsoft

**Q3: How does the full-stack system work?**  
*A: Step-by-step flow:*
1. User enters transaction in React form
2. Axios sends HTTP POST to FastAPI backend (port 8000)
3. FastAPI validates data using Pydantic schemas
4. Backend loads model and scaler, makes prediction
5. Returns JSON response with prediction, probability, risk level
6. React updates UI in real-time with colored result card

**Q4: What is class imbalance?**  
*A: In fraud datasets, genuine transactions (99.83%) far outnumber frauds (0.17%). Models can achieve 99% accuracy by predicting everything as genuine, which is useless. We used SMOTE to oversample fraud cases.*

**Q5: How do you handle imbalanced data?**  
*A: Use techniques like SMOTE (oversampling), undersampling, or class weights. Focus on recall and F1-score instead of accuracy.*

**Q6: Why Logistic Regression?**  
*A: Simple, fast, interpretable. Good baseline for mini project. Coefficients show which features contribute to fraud. Can upgrade to Random Forest or XGBoost for major project.*

**Q7: What features are most important?**  
*A: Transaction amount, time patterns, V1-V28 PCA components (representing behavioral features like device, location, user history).*

**Q8: How would you deploy this in production?**  
*A:*
- **Frontend:** Build with `npm run build`, deploy to Vercel/Azure Static Web Apps
- **Backend:** Containerize with Docker, deploy to Azure App Service with auto-scaling
- **Database:** Add PostgreSQL for transaction logging, Redis for caching
- **Security:** Add JWT authentication, rate limiting, input validation
- **Monitoring:** Track model performance, retrain on new fraud patterns

**Q9: What are the limitations?**  
*A:*
- **Dataset:** European credit card data (may not generalize globally), highly imbalanced
- **Model:** Baseline Logistic Regression (can improve with ensemble methods)
- **System:** No authentication, no database, no real-time retraining
- **Interpretability:** PCA features are not human-readable

**Q10: How is this academically acceptable?**  
*A: This is a DEMONSTRATION PROTOTYPE for academic evaluation. We use modern tools to show real-world applicability while keeping the ML approach simple (Logistic Regression). We clearly state this is not production-ready and would require additional features like authentication, logging, and compliance (PCI-DSS) for real deployment.*

---

### Live Demo Script (2 minutes)

1. **Open both terminals:**
   - Show backend running on port 8000
   - Show frontend running on port 5173

2. **Test Genuine Transaction:**
   - Click "✓ Genuine" preset
   - Click "Analyze Transaction"
   - Show GREEN result with low fraud probability

3. **Test Fraudulent Transaction:**
   - Click "⚠️ Suspicious" preset
   - Click "Analyze"
   - Show RED result with high fraud probability

4. **Show Architecture:**
   - Open DevTools → Network tab
   - Submit transaction, show POST request to /predict
   - Show JSON response

5. **Explain Technologies:**
   - Point to "Technology Stack" section in UI
   - React (frontend), FastAPI (backend), ML (Logistic Regression)

**👉 Full viva guide:** See [FULLSTACK_SETUP_GUIDE.md](FULLSTACK_SETUP_GUIDE.md#-viva-questions--answers)

---

## 📝 Mini Project Report Sections

### Required Sections for Academic Submission

1. **Abstract** (150-200 words)
2. **Introduction**
   - Background on e-commerce fraud
   - Need for AI-based solutions
3. **Literature Survey**
   - Review 3-5 research papers on fraud detection
4. **Problem Definition**
   - Clear problem statement
   - Scope and limitations
5. **System Architecture**
   - Data flow diagram
   - ML pipeline architecture
6. **Methodology**
   - Dataset description
   - Feature engineering
   - Algorithm selection
   - Training process
7. **Implementation**
   - Code snippets (key parts)
   - Libraries used
   - Development environment
8. **Results & Analysis**
   - Confusion matrix
   - Performance metrics
   - Visualizations
9. **Conclusion**
   - Summary of achievements
   - Limitations
10. **Future Scope**
    - Deep learning models
    - Real-time deployment
    - Multi-class fraud detection

---

## 🔮 Future Enhancements (Mini → Major Project)

### Immediate Extensions
1. **Better Models:** Random Forest, XGBoost, Neural Networks
2. **Real-time API:** Deploy on Azure with auto-scaling
3. **Dashboard:** Admin panel to visualize fraud trends
4. **Alert System:** Email/SMS notifications for high-risk orders

### Advanced Features (Major Project)
5. **Deep Learning:** LSTM for sequential transaction patterns
6. **Graph Analysis:** Detect fraud rings (connected fake accounts)
7. **Multi-class Detection:** Classify fraud types (payment fraud, return fraud, promo abuse)
8. **Explainable AI:** SHAP/LIME to explain predictions to auditors
9. **Active Learning:** Model retrains automatically with new fraud patterns
10. **Integration:** Connect with Shopify, WooCommerce, Magento

---

## 📚 References

1. Credit Card Fraud Detection Dataset - Kaggle
2. Scikit-learn Documentation: https://scikit-learn.org/
3. "Machine Learning for Fraud Detection" - Research Papers
4. Azure Machine Learning Documentation

---

## 👥 Team Contributions

| Member | Responsibilities |
|--------|-----------------|
| **Yagnesh** | Data analysis, EDA, visualization |
| **Bhaskar** | Model training, evaluation, optimization |
| **Syam** | Prediction script, API development, documentation |

*Note: All members contribute to all sections collaboratively*

---

## 📞 Contact

**Team:** Three Unknowns  
**College:** VRSEC, Vijayawada  
**Department:** Information Technology  
**Academic Year:** 2025-26

---

## 📄 License

This project is for academic purposes only.

---

**Status:** ✅ Ready for development  
**Last Updated:** January 1, 2026
#   a i - e c o m m e r c e - f r a u d - d e t e c t i o n 
 
 