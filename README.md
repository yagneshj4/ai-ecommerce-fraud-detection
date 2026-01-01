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
├── data/                          # Dataset storage
│   ├── raw/                       # Original dataset files
│   └── processed/                 # Cleaned/processed data
│
├── notebooks/                     # Jupyter notebooks for analysis
│   ├── 01_EDA.ipynb              # Exploratory Data Analysis
│   └── 02_Model_Training.ipynb    # Model development & evaluation
│
├── src/                           # Python source code
│   ├── predict.py                 # Prediction script for new orders
│   └── utils.py                   # Helper functions
│
├── models/                        # Trained model files
│   └── fraud_detector.pkl         # Saved model (generated after training)
│
├── api/                           # REST API (optional)
│   └── app.py                     # Flask API for deployment
│
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation (this file)
├── ABSTRACT.md                    # Project abstract for submission
└── PROJECT_PROPOSAL.md            # Initial project proposal
```

### 📂 Folder Descriptions

| Folder | Purpose |
|--------|---------|
| **data/** | Stores raw and processed datasets. Raw data is kept separate for reproducibility |
| **notebooks/** | Interactive Jupyter notebooks for analysis, visualization, and model training |
| **src/** | Production-ready Python scripts for predictions and utilities |
| **models/** | Stores trained ML models as `.pkl` files for reuse |
| **api/** | Flask/FastAPI code for exposing the model as a REST API (bonus feature) |

---

## 🔬 Technology Stack

### Core Technologies
- **Language:** Python 3.9+
- **ML Framework:** Scikit-learn
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Model Persistence:** Joblib

### Optional (Bonus)
- **API Framework:** Flask / FastAPI
- **Deployment:** Azure App Service (using Student credits)
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

### Step 6: Make Predictions
```bash
# Run prediction script
python src/predict.py
```

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
*A: E-commerce fraud causes billions in losses annually. AI can detect patterns humans miss and scale to millions of transactions.*

**Q2: Why machine learning over rule-based systems?**  
*A: Fraudsters constantly change tactics. ML adapts to new patterns automatically. Rules become outdated quickly.*

**Q3: What is class imbalance?**  
*A: In fraud datasets, genuine transactions (99%) far outnumber frauds (1%). Models can achieve 99% accuracy by predicting everything as genuine, which is useless.*

**Q4: How do you handle imbalanced data?**  
*A: Use techniques like SMOTE (oversampling), undersampling, or class weights. Focus on recall and F1-score instead of accuracy.*

**Q5: Why Logistic Regression?**  
*A: Simple, fast, interpretable. Good baseline for mini project. Can upgrade to complex models later.*

**Q6: What features are most important?**  
*A: Transaction amount, user history (account age, previous orders), time patterns, device consistency.*

**Q7: How would you deploy this in production?**  
*A: Create REST API using Flask, deploy on Azure App Service, integrate with e-commerce backend to screen orders in real-time.*

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
#   a i - e c o m m e r c e - f r a u d - d e t e c t i o n  
 