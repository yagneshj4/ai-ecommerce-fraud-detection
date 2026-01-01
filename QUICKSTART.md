# Quick Start Guide
## AI-Based Fraud Detection System

**Team:** Three Unknowns | VRSEC

---

## 🚀 Quick Setup (5 Minutes)

### Step 1: Install Dependencies
```bash
cd c:\Users\HP\OneDrive\Desktop\mini
pip install -r requirements.txt
```

### Step 2: Download Dataset
1. Go to [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
2. Download `creditcard.csv`
3. Place in `mini/data/raw/` folder

### Step 3: Train the Model
```bash
# Open Jupyter Notebook
jupyter notebook

# Open and run these notebooks in order:
# 1. notebooks/01_EDA.ipynb (Exploratory Data Analysis)
# 2. notebooks/02_Model_Training.ipynb (Train and save model)
```

### Step 4: Make Predictions
```bash
# Interactive mode
python src/predict.py

# Demo mode
python src/predict.py --demo
```

### Step 5 (Optional): Run API Server
```bash
python api/app.py

# Access at: http://localhost:5000
```

---

## 📁 Project Structure Overview

```
mini/
├── data/                   # Dataset storage
├── notebooks/              # Jupyter notebooks (EDA, training)
├── src/                    # Python scripts (prediction)
├── models/                 # Trained models (generated after training)
├── api/                    # Flask API (optional)
├── requirements.txt        # Dependencies
└── README.md              # Full documentation
```

---

## 🎓 For Viva/Presentation

### Key Points to Remember:

**1. Problem Statement**
> "E-commerce fraud causes billions in losses. Traditional rule-based systems can't adapt to new fraud tactics. We built an AI model that learns fraud patterns automatically."

**2. Why Machine Learning?**
> "Fraudsters constantly change strategies. ML adapts to new patterns. Rule-based systems become outdated quickly."

**3. Algorithm Choice**
> "Logistic Regression - simple, fast, interpretable. Perfect for mini project. Can upgrade to Random Forest/XGBoost later."

**4. Key Challenge**
> "Class imbalance - only 0.17% transactions are fraud. Used SMOTE to create synthetic fraud examples for training."

**5. Performance Metrics**
> "80%+ recall (catches 80% of frauds), 75%+ precision (low false alarms), 0.95 ROC-AUC (excellent discrimination)"

### Common Viva Questions:

**Q: What is SMOTE?**  
*A: Synthetic Minority Over-sampling Technique. Creates artificial fraud examples by interpolating between existing fraud cases.*

**Q: Why not use accuracy?**  
*A: With 99.8% genuine transactions, predicting everything as genuine gives 99.8% accuracy but catches ZERO frauds!*

**Q: What is confusion matrix?**  
*A: Shows TP (frauds caught), FN (frauds missed), FP (false alarms), TN (genuine correctly identified).*

**Q: What features indicate fraud?**  
*A: High transaction amounts, unusual time patterns, new account behavior, PCA-transformed features.*

**Q: How to deploy in production?**  
*A: Create REST API (Flask), deploy on Azure App Service, integrate with e-commerce backend.*

---

## 📊 Expected Results

After training, you should see:

- **Recall (Fraud Detection Rate):** 80-85%
- **Precision:** 75-80%
- **F1-Score:** 0.75-0.80
- **ROC-AUC:** 0.90-0.95

If your results are significantly different:
- Check if SMOTE was applied
- Verify dataset is loaded correctly
- Ensure random_state=42 for reproducibility

---

## 🐛 Troubleshooting

### Issue: Model file not found
**Solution:** Run `notebooks/02_Model_Training.ipynb` first to generate model files

### Issue: Import errors
**Solution:** Install dependencies: `pip install -r requirements.txt`

### Issue: Dataset not found
**Solution:** Download from Kaggle and place in `data/raw/creditcard.csv`

### Issue: Low accuracy
**Solution:** This is normal for imbalanced data. Focus on Recall and F1-score instead.

---

## 📝 Running Commands Cheat Sheet

```bash
# Install packages
pip install -r requirements.txt

# Start Jupyter
jupyter notebook

# Run prediction (interactive)
python src/predict.py

# Run prediction (demo)
python src/predict.py --demo

# Start API server
python api/app.py

# Test API health
curl http://localhost:5000/health
```

---

## ✅ Submission Checklist

- [ ] Dataset downloaded and placed in `data/raw/`
- [ ] All dependencies installed
- [ ] EDA notebook executed successfully
- [ ] Model training completed
- [ ] Model files saved in `models/` folder
- [ ] Prediction script tested
- [ ] API tested (optional)
- [ ] Project report written
- [ ] Code uploaded to repository

---

## 🎯 Next Steps for Major Project

1. Implement Random Forest / XGBoost
2. Add deep learning (LSTM for sequences)
3. Deploy on Azure with CI/CD
4. Build admin dashboard
5. Integrate with real e-commerce platform
6. Add explainable AI (SHAP)
7. Implement real-time streaming

---

## 📞 Support

If you encounter issues:
1. Check the main [README.md](README.md) for detailed documentation
2. Review notebook outputs for error messages
3. Verify all files are in correct directories
4. Ensure Python version is 3.9 or higher

---

**Good luck with your project! 🚀**

---

*Last Updated: January 1, 2026*
