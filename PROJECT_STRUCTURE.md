# 📁 Project Structure Guide

## Complete Folder Layout

```
ai-ecommerce-fraud-detection/
│
├── 📂 data/                          # All dataset files
│   ├── raw/                          # Original, unprocessed data
│   │   └── creditcard.csv            # Kaggle fraud dataset (280+ MB)
│   ├── processed/                    # Cleaned, preprocessed data
│   └── sample_transactions.csv       # Sample data for testing
│
├── 📂 notebooks/                     # Jupyter notebooks for exploration
│   ├── 01_EDA.ipynb                  # Exploratory Data Analysis
│   └── 02_Model_Training.ipynb       # Model training experiments
│
├── 📂 src/                           # Source code (Python modules)
│   ├── __init__.py                   # Package initialization
│   ├── data_loader.py                # Load and validate datasets
│   ├── preprocessing.py              # Feature engineering, scaling, SMOTE
│   ├── train_model.py                # Train and save ML models
│   ├── evaluate_model.py             # Model evaluation with visualizations
│   ├── predict.py                    # Make predictions on new data
│   └── utils.py                      # Helper functions
│
├── 📂 models/                        # Saved ML models
│   ├── fraud_detector.pkl            # Trained model
│   ├── scaler.pkl                    # Feature scaler
│   ├── feature_names.pkl             # List of features
│   └── training_history.pkl          # Training metadata
│
├── 📂 api/                           # REST API (optional)
│   └── app.py                        # Flask API server
│
├── 📂 docs/                          # Documentation
│   ├── ABSTRACT.md                   # Academic abstract
│   ├── PROJECT_PROPOSAL.md           # Project proposal
│   ├── EXECUTION_GUIDE.md            # Complete execution guide
│   ├── QUICKSTART.md                 # Quick setup guide
│   └── DELIVERY_SUMMARY.md           # Submission summary
│
├── 📄 requirements.txt               # Python dependencies
├── 📄 README.md                      # Main project documentation
├── 📄 .gitignore                     # Git ignore rules
└── 📄 PROJECT_STRUCTURE.md           # This file

```

---

## 📂 Folder Explanations

### 1️⃣ `data/` - Dataset Storage

**Purpose:** Store all data files (raw and processed)

**Subfolders:**
- **`raw/`** - Original datasets (never modify these!)
  - `creditcard.csv` - Main Kaggle dataset
  - Downloaded from: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
  - Size: ~150 MB (284,807 transactions)

- **`processed/`** - Cleaned/transformed data
  - Created by preprocessing scripts
  - Split datasets (train/test)
  - Feature-engineered data

- **`sample_transactions.csv`** - Small dataset for testing
  - 30 sample transactions
  - Use when main dataset is unavailable

**Why separate raw and processed?**
- Raw data = source of truth (never modify)
- Processed data = intermediate results (can regenerate)

---

### 2️⃣ `notebooks/` - Interactive Exploration

**Purpose:** Jupyter notebooks for analysis and experimentation

**Files:**
- **`01_EDA.ipynb`** - Exploratory Data Analysis
  - Understand data distribution
  - Visualize fraud vs genuine patterns
  - Identify important features
  - Check for missing values/outliers

- **`02_Model_Training.ipynb`** - Model Development
  - Train different ML models
  - Compare performance
  - Tune hyperparameters
  - Save best model

**How to use:**
```bash
# Start Jupyter
jupyter notebook

# Navigate to notebooks/ and open files
# Run cells with Shift+Enter
```

**Why notebooks?**
- Interactive experimentation
- Visualizations
- Step-by-step execution
- Easy to share insights

---

### 3️⃣ `src/` - Production Code

**Purpose:** Reusable, production-ready Python modules

**Files:**

#### **`__init__.py`**
- Makes `src/` a Python package
- Allows imports: `from src.data_loader import FraudDataLoader`

#### **`data_loader.py`**
- Loads datasets (Kaggle or sample)
- Validates data structure
- Creates synthetic data if needed

**Example:**
```python
from src.data_loader import FraudDataLoader

loader = FraudDataLoader()
df = loader.load_creditcard_data()
```

#### **`preprocessing.py`**
- Feature scaling (StandardScaler)
- Train-test split (80-20)
- SMOTE for class balancing
- Feature engineering

**Example:**
```python
from src.preprocessing import FraudPreprocessor

preprocessor = FraudPreprocessor(test_size=0.2)
data = preprocessor.full_preprocessing_pipeline(df)
```

#### **`train_model.py`**
- Train ML models (Logistic Regression, Random Forest)
- Evaluate performance
- Save trained models

**Usage:**
```bash
python src/train_model.py
```

#### **`evaluate_model.py`**
- Generate classification reports
- Plot confusion matrix
- ROC curve visualization
- Precision-Recall curves

**Usage:**
```bash
python src/evaluate_model.py
```

#### **`predict.py`**
- Make predictions on new transactions
- Interactive mode (user input)
- Batch mode (CSV file)
- API integration

**Usage:**
```bash
python src/predict.py --demo
```

#### **`utils.py`**
- Helper functions
- Logging utilities
- File path management

---

### 4️⃣ `models/` - Saved ML Models

**Purpose:** Store trained models for deployment

**Files:**
- **`fraud_detector.pkl`** - Main trained model
- **`scaler.pkl`** - Feature scaler (fit on training data)
- **`feature_names.pkl`** - List of feature names (order matters!)
- **`training_history.pkl`** - Training metadata (date, metrics, etc.)

**Why save models?**
- No need to retrain every time
- Fast predictions
- Version control for models

**How to use:**
```python
import joblib

# Load model
model = joblib.load('models/fraud_detector.pkl')
scaler = joblib.load('models/scaler.pkl')

# Make prediction
prediction = model.predict(scaled_features)
```

---

### 5️⃣ `api/` - REST API (Optional)

**Purpose:** Expose model as web service

**Files:**
- **`app.py`** - Flask REST API

**Endpoints:**
- `GET /` - API documentation
- `GET /health` - Health check
- `POST /predict` - Make prediction
- `POST /predict/batch` - Batch predictions

**Usage:**
```bash
python api/app.py

# API runs on http://localhost:5000
```

**Why API?**
- Real-world integration
- Microservice architecture
- Remote predictions
- Platform-independent

---

### 6️⃣ `docs/` - Documentation

**Purpose:** All project documentation

**Files:**
- **`ABSTRACT.md`** - Academic abstract (IEEE format)
- **`PROJECT_PROPOSAL.md`** - Initial project proposal
- **`EXECUTION_GUIDE.md`** - Complete step-by-step guide
- **`QUICKSTART.md`** - Quick setup (5 minutes)
- **`DELIVERY_SUMMARY.md`** - Submission checklist

---

## 📄 Root Files

### **`requirements.txt`**
Lists all Python dependencies

```txt
pandas>=1.5.0
numpy>=1.23.0
scikit-learn>=1.2.0
imbalanced-learn>=0.10.0
matplotlib>=3.6.0
seaborn>=0.12.0
jupyter>=1.0.0
flask>=2.3.0
joblib>=1.2.0
```

**Install:**
```bash
pip install -r requirements.txt
```

---

### **`README.md`**
Main project documentation

**Sections:**
- Project overview
- Installation instructions
- Usage examples
- Tech stack
- Team information

---

### **`.gitignore`**
Tells Git which files NOT to track

**Ignores:**
- Large datasets (`*.csv`, `data/raw/`)
- Trained models (`*.pkl`)
- Python cache (`__pycache__/`, `*.pyc`)
- Virtual environments (`.venv/`, `venv/`)
- Jupyter checkpoints (`.ipynb_checkpoints/`)
- IDE files (`.vscode/`, `.idea/`)

**Why?**
- Keep repository small
- Avoid committing sensitive data
- Don't track generated files

---

## 🔄 Typical Workflow

### Step 1: Setup
```bash
# Clone repository
git clone https://github.com/yagneshj4/ai-ecommerce-fraud-detection.git
cd ai-ecommerce-fraud-detection

# Install dependencies
pip install -r requirements.txt

# Download dataset to data/raw/
```

### Step 2: Exploration
```bash
# Open Jupyter
jupyter notebook

# Run 01_EDA.ipynb
# Understand data patterns
```

### Step 3: Training
```bash
# Train model
python src/train_model.py

# Models saved to models/
```

### Step 4: Evaluation
```bash
# Evaluate model
python src/evaluate_model.py

# Generates plots and metrics
```

### Step 5: Prediction
```bash
# Interactive mode
python src/predict.py

# Or batch mode
python src/predict.py --batch data/sample_transactions.csv
```

### Step 6: API (Optional)
```bash
# Start API server
python api/app.py

# Test at http://localhost:5000
```

---

## 🎯 Best Practices

### 1. **Never modify `data/raw/`**
- Raw data = source of truth
- Always work with copies

### 2. **Use meaningful file names**
- ✅ `fraud_detector_v2.pkl`
- ❌ `model.pkl`

### 3. **Comment your code**
```python
# Good comment - explains WHY
# Using SMOTE because dataset is imbalanced (0.17% fraud)
smote = SMOTE()
```

### 4. **Version control your code, not data**
- Commit: `.py`, `.ipynb`, `.md`
- Don't commit: `.csv`, `.pkl`, `__pycache__/`

### 5. **Test before pushing**
```bash
# Run tests
python src/train_model.py

# Check for errors
# Then push to GitHub
git push
```

---

## 📊 File Size Guide

| Folder | Typical Size | In Git? |
|--------|--------------|---------|
| `data/raw/` | 150 MB | ❌ No |
| `data/processed/` | 50 MB | ❌ No |
| `models/` | 10 MB | ❌ No |
| `notebooks/` | 5 MB | ✅ Yes |
| `src/` | 100 KB | ✅ Yes |
| `api/` | 20 KB | ✅ Yes |
| `docs/` | 200 KB | ✅ Yes |

**Total Git Repo:** ~5-10 MB  
**Total Project (with data):** ~200+ MB

---

## 🚀 Quick Commands

```bash
# Setup
pip install -r requirements.txt

# Train model
python src/train_model.py

# Make predictions
python src/predict.py --demo

# Start API
python api/app.py

# Open notebooks
jupyter notebook

# Run evaluation
python src/evaluate_model.py
```

---

**Team Three Unknowns - VRSEC**  
*Last Updated: January 2, 2026*
