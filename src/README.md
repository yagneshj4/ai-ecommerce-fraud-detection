# Source Code Documentation

**Fraud Detection System - Core Modules**

---

## 📦 Module Overview

The `src/` directory contains all production-ready Python code for the fraud detection system. Each module is designed to be:
- **Modular:** Can be imported and used independently
- **Reusable:** Functions and classes can be called from notebooks or scripts
- **Well-documented:** Comprehensive docstrings and comments
- **Tested:** Includes example usage in `if __name__ == "__main__"` blocks

---

## 📁 Files in `src/`

```
src/
├── __init__.py           # Package initialization
├── data_loader.py        # Data loading and validation
├── preprocessing.py      # Feature engineering and scaling
├── train_model.py        # Model training pipeline
├── evaluate_model.py     # Model evaluation and visualization
├── predict.py            # Prediction for new transactions
└── utils.py              # Helper utilities
```

---

## 1️⃣ `__init__.py`

**Purpose:** Makes `src/` a Python package

**Contents:**
```python
__version__ = "1.0.0"
```

**Usage:**
```python
# Allows imports like:
from src.data_loader import FraudDataLoader
from src.preprocessing import FraudPreprocessor
```

**Why needed?**
- Enables package-level imports
- Defines package version
- Can include package-wide configurations

---

## 2️⃣ `data_loader.py`

**Purpose:** Load and validate fraud detection datasets

### Key Class: `FraudDataLoader`

**Capabilities:**
- ✅ Load main Kaggle dataset (`creditcard.csv`)
- ✅ Load sample transaction data
- ✅ Create synthetic data for testing
- ✅ Validate dataset structure
- ✅ Save processed data

### Usage Example:

```python
from src.data_loader import FraudDataLoader

# Initialize loader
loader = FraudDataLoader()

# Load main dataset
df = loader.load_creditcard_data()

# Validate
loader.validate_data(df)

# Output:
# 📂 Loading dataset from: c:\...\data\raw\creditcard.csv
# ✅ Loaded 284,807 transactions
#    - Features: 31
#    - Memory usage: 68.23 MB
```

### Key Methods:

| Method | Description |
|--------|-------------|
| `load_creditcard_data()` | Load main Kaggle dataset |
| `load_sample_data()` | Load sample transactions |
| `validate_data(df)` | Check data structure and quality |
| `save_processed_data(df, filename)` | Save to processed/ |

### Error Handling:

```python
try:
    df = loader.load_creditcard_data()
except FileNotFoundError:
    print("⚠️ Dataset not found. Using sample data.")
    df = loader.load_sample_data()
```

---

## 3️⃣ `preprocessing.py`

**Purpose:** Prepare data for machine learning

### Key Class: `FraudPreprocessor`

**Capabilities:**
- ✅ Split features (X) and target (y)
- ✅ Train-test split with stratification
- ✅ Feature scaling (StandardScaler)
- ✅ Handle class imbalance (SMOTE)
- ✅ Complete preprocessing pipeline

### Usage Example:

```python
from src.preprocessing import FraudPreprocessor

# Initialize preprocessor
preprocessor = FraudPreprocessor(test_size=0.2, random_state=42)

# Run full pipeline
processed_data = preprocessor.full_preprocessing_pipeline(df, apply_smote=True)

# Access processed data
X_train = processed_data['X_train']
X_test = processed_data['X_test']
y_train = processed_data['y_train']
y_test = processed_data['y_test']
scaler = processed_data['scaler']
```

### Pipeline Steps:

```
1. Split Features & Target
   ├─ X: All columns except 'Class'
   └─ y: 'Class' column (0=Genuine, 1=Fraud)

2. Train-Test Split
   ├─ 80% training
   ├─ 20% testing
   └─ Stratified (maintains fraud ratio)

3. Feature Scaling
   ├─ StandardScaler (mean=0, std=1)
   ├─ Fit on training data only
   └─ Transform both train and test

4. Handle Imbalance (SMOTE)
   ├─ Original: 99.8% genuine, 0.2% fraud
   ├─ After SMOTE: 50% genuine, 50% fraud
   └─ Creates synthetic fraud examples
```

### Key Methods:

| Method | Description |
|--------|-------------|
| `split_features_target(df)` | Separate X and y |
| `train_test_split_data(X, y)` | Split into train/test |
| `scale_features(X_train, X_test)` | Standardize features |
| `handle_imbalance(X_train, y_train)` | Apply SMOTE |
| `full_preprocessing_pipeline(df)` | Run complete workflow |

---

## 4️⃣ `train_model.py`

**Purpose:** Train and save ML models

### Key Class: `FraudModelTrainer`

**Capabilities:**
- ✅ Train Logistic Regression
- ✅ Train Random Forest
- ✅ Evaluate model performance
- ✅ Save trained model to disk
- ✅ Track training history

### Usage Example:

```python
from src.train_model import FraudModelTrainer

# Initialize trainer
trainer = FraudModelTrainer(model_type='logistic', random_state=42)

# Train
trainer.train(X_train, y_train)

# Evaluate
metrics = trainer.evaluate(X_test, y_test)

# Save
trainer.save_model('models/', feature_names=feature_list)
```

### Supported Models:

| Model | Algorithm | Best For |
|-------|-----------|----------|
| `logistic` | Logistic Regression | Speed, interpretability |
| `random_forest` | Random Forest | Accuracy, robustness |

### Training Output:

```
🎯 TRAINING MODEL
===========================================

📊 Training data:
   Samples: 227,845
   Features: 30

⏳ Training logistic model...
✅ Training complete in 3.42 seconds

📊 MODEL EVALUATION
===========================================

              precision    recall  f1-score   support

    Genuine       1.00      0.99      1.00     56726
       Fraud       0.75      0.80      0.77        50

    accuracy                           0.99     56776
```

### Saved Files:

```
models/
├── fraud_detector.pkl      # Trained model
├── feature_names.pkl       # Feature list
└── training_history.pkl    # Metadata
```

---

## 5️⃣ `evaluate_model.py`

**Purpose:** Comprehensive model evaluation

### Key Class: `FraudModelEvaluator`

**Capabilities:**
- ✅ Classification report
- ✅ Confusion matrix visualization
- ✅ ROC curve plot
- ✅ Precision-Recall curve
- ✅ Threshold analysis

### Usage Example:

```python
from src.evaluate_model import FraudModelEvaluator

# Load model
evaluator = FraudModelEvaluator(model_path='models/')

# Run comprehensive evaluation
evaluator.comprehensive_evaluation(
    X_test, 
    y_test, 
    output_dir='evaluation_results'
)
```

### Generated Visualizations:

1. **Confusion Matrix** (`confusion_matrix.png`)
   ```
                Predicted
            Genuine  Fraud
   Actual
   Genuine   56,626    100
   Fraud         10     40
   ```

2. **ROC Curve** (`roc_curve.png`)
   - Shows True Positive Rate vs False Positive Rate
   - AUC = 0.95 (excellent!)

3. **Precision-Recall Curve** (`precision_recall_curve.png`)
   - Important for imbalanced datasets
   - Shows trade-off between precision and recall

### Threshold Analysis:

```python
# Evaluate at different probability thresholds
df_thresholds = evaluator.evaluate_at_different_thresholds(y_test, y_pred_proba)

# Output:
#  Threshold  Precision  Recall  F1-Score  False Positives  False Negatives
#       0.3       0.65    0.90      0.76              150               5
#       0.5       0.75    0.80      0.77              100              10
#       0.7       0.85    0.70      0.77               50              15
```

---

## 6️⃣ `predict.py`

**Purpose:** Make predictions on new transactions

### Key Class: `FraudPredictor`

**Capabilities:**
- ✅ Load trained model and scaler
- ✅ Interactive prediction (user input)
- ✅ Batch prediction (CSV file)
- ✅ Single transaction prediction
- ✅ Detailed fraud reports

### Usage Examples:

#### Interactive Mode:
```bash
python src/predict.py

# User enters transaction details
# System predicts fraud probability
```

#### Demo Mode:
```bash
python src/predict.py --demo

# Uses pre-defined sample transactions
```

#### Batch Mode:
```bash
python src/predict.py --batch data/sample_transactions.csv --output results.csv

# Processes entire CSV file
# Saves predictions to results.csv
```

#### Programmatic Use:
```python
from src.predict import FraudPredictor

# Initialize
predictor = FraudPredictor()

# Predict single transaction
result = predictor.predict_single({
    'Time': 10000,
    'Amount': 1500,
    'V1': 0.5,
    # ... other features
})

print(result['prediction'])  # 'FRAUD' or 'GENUINE'
print(result['probability'])  # 0.8723
```

### Output Format:

```
======================================
FRAUD DETECTION REPORT
======================================

📊 Transaction Details:
   Amount: $1,500.00
   Time: 10000

🤖 Model Prediction:
   Result: FRAUD ⚠️
   Fraud Probability: 0.8723 (87.23%)
   Confidence: 87.23%
   Risk Level: HIGH

💡 Recommendation:
   FLAG for manual review before processing.
```

---

## 7️⃣ `utils.py`

**Purpose:** Helper functions used across modules

### Key Functions:

```python
# File path management
def get_project_root() -> Path:
    """Get absolute path to project root."""
    return Path(__file__).parent.parent

# Logging
def setup_logger(name: str, log_file: str = None) -> logging.Logger:
    """Configure logging for modules."""
    
# Data validation
def validate_transaction_features(transaction: dict) -> bool:
    """Check if transaction has all required features."""

# Model versioning
def get_latest_model(model_dir: str) -> Path:
    """Find most recent model file."""
```

### Usage:

```python
from src.utils import get_project_root, setup_logger

# Get paths
root = get_project_root()
data_path = root / 'data' / 'raw' / 'creditcard.csv'

# Setup logging
logger = setup_logger('fraud_detection', 'logs/training.log')
logger.info('Starting training...')
```

---

## 🔄 Module Dependencies

```
data_loader.py
    ↓
preprocessing.py
    ↓
train_model.py
    ↓
evaluate_model.py

predict.py (standalone, loads saved models)
utils.py (used by all modules)
```

---

## 🎯 Complete Workflow Example

```python
# 1. Load Data
from src.data_loader import FraudDataLoader

loader = FraudDataLoader()
df = loader.load_creditcard_data()

# 2. Preprocess
from src.preprocessing import FraudPreprocessor

preprocessor = FraudPreprocessor()
data = preprocessor.full_preprocessing_pipeline(df)

# 3. Train Model
from src.train_model import FraudModelTrainer

trainer = FraudModelTrainer(model_type='logistic')
trainer.train(data['X_train'], data['y_train'])

# 4. Evaluate
metrics = trainer.evaluate(data['X_test'], data['y_test'])

# 5. Save
trainer.save_model('models/', feature_names=data['feature_names'])
preprocessor.save_scaler('models/scaler.pkl')

# 6. Make Predictions
from src.predict import FraudPredictor

predictor = FraudPredictor()
result = predictor.predict_single(new_transaction)
```

---

## 🧪 Testing Modules

Each module includes test code in `if __name__ == "__main__"` block:

```bash
# Test data loader
python src/data_loader.py

# Test preprocessing
python src/preprocessing.py

# Test training
python src/train_model.py

# Test evaluation
python src/evaluate_model.py

# Test prediction
python src/predict.py --demo
```

---

## 📚 Import Cheat Sheet

```python
# Data Loading
from src.data_loader import FraudDataLoader

# Preprocessing
from src.preprocessing import FraudPreprocessor

# Training
from src.train_model import FraudModelTrainer

# Evaluation
from src.evaluate_model import FraudModelEvaluator

# Prediction
from src.predict import FraudPredictor

# Utilities
from src.utils import get_project_root, setup_logger
```

---

## 🔧 Customization

### Change Model Type:
```python
# Use Random Forest instead of Logistic Regression
trainer = FraudModelTrainer(model_type='random_forest')
```

### Adjust Train-Test Split:
```python
# 70-30 split instead of 80-20
preprocessor = FraudPreprocessor(test_size=0.3)
```

### Disable SMOTE:
```python
# Don't balance classes (use original imbalanced data)
data = preprocessor.full_preprocessing_pipeline(df, apply_smote=False)
```

### Change Prediction Threshold:
```python
# More conservative (fewer false positives)
predictor = FraudPredictor(threshold=0.7)
```

---

## 🐛 Common Issues

### Import Error:
```python
# ❌ ModuleNotFoundError: No module named 'src'
# Solution: Run from project root, not from src/ folder
cd c:\Users\HP\OneDrive\Desktop\mini
python src/train_model.py
```

### Model Not Found:
```python
# ❌ FileNotFoundError: fraud_detector.pkl not found
# Solution: Train model first
python src/train_model.py
```

### Feature Mismatch:
```python
# ❌ ValueError: X has 29 features but model expects 30
# Solution: Ensure prediction data has same features as training
```

---

## 📖 Code Style Guide

**Follow these conventions:**

1. **Classes:** PascalCase
   ```python
   class FraudDataLoader:
   ```

2. **Functions:** snake_case
   ```python
   def load_creditcard_data():
   ```

3. **Constants:** UPPER_CASE
   ```python
   DEFAULT_THRESHOLD = 0.5
   ```

4. **Private methods:** Leading underscore
   ```python
   def _create_synthetic_data():
   ```

5. **Docstrings:** Use Google style
   ```python
   def train(self, X_train, y_train):
       """
       Train the model.
       
       Args:
           X_train: Training features
           y_train: Training labels
           
       Returns:
           Trained model object
       """
   ```

---

**Team Three Unknowns - VRSEC**

*Source Code Documentation - v1.0*

*Last Updated: January 2, 2026*
