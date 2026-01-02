# ⚡ Quick Commands Reference

**Fraud Detection Project - Essential Commands**

---

## 🚀 Daily Workflow Commands

### Start Working
```bash
# Navigate to project
cd c:\Users\HP\OneDrive\Desktop\mini

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Pull latest changes
git pull origin main
```

### End Working Session
```bash
# Check what changed
git status

# Add all changes
git add .

# Commit with message
git commit -m "Describe what you did"

# Push to GitHub
git push origin main

# Deactivate virtual environment
deactivate
```

---

## 📦 Installation & Setup

```bash
# Create virtual environment (first time only)
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Install all dependencies
pip install -r requirements.txt

# Verify installation
python -c "import pandas, sklearn; print('✅ Ready!')"
```

---

## 📊 Data & Notebooks

```bash
# Start Jupyter Notebook
jupyter notebook

# Run specific notebook
jupyter notebook notebooks/01_EDA.ipynb

# Convert notebook to Python script
jupyter nbconvert --to script notebooks/01_EDA.ipynb
```

---

## 🤖 Model Training

```bash
# Train model (full pipeline)
python src/train_model.py

# Train with custom parameters
python src/train_model.py --model logistic --test-size 0.3

# Evaluate existing model
python src/evaluate_model.py
```

---

## 🔮 Making Predictions

```bash
# Interactive prediction (manual input)
python src/predict.py

# Demo mode (uses sample data)
python src/predict.py --demo

# Batch prediction from CSV
python src/predict.py --batch data/sample_transactions.csv --output results.csv

# Single prediction with parameters
python src/predict.py --amount 1500 --time 10000
```

---

## 🌐 API Commands

```bash
# Start Flask API server
python api/app.py

# Start on specific port
python api/app.py --port 8080

# Test API health
curl http://localhost:5000/health

# Make prediction via API
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"Time": 1000, "Amount": 149.99, "V1": 0.5, "V2": -0.3}'
```

---

## 🔍 Git Commands

### Basic Operations
```bash
# Check status
git status

# View commit history
git log --oneline

# View changes
git diff

# Add specific file
git add src/predict.py

# Add all Python files
git add *.py

# Commit
git commit -m "Your message here"

# Push
git push origin main
```

### Undo Changes
```bash
# Discard changes in file
git checkout -- filename.py

# Unstage file
git reset HEAD filename.py

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes) ⚠️ DANGEROUS
git reset --hard HEAD~1
```

### Branching
```bash
# Create new branch
git checkout -b feature/new-feature

# Switch branches
git checkout main

# Merge branch
git merge feature/new-feature

# Delete branch
git branch -d feature/new-feature
```

---

## 📁 File Operations

```bash
# List files
ls

# List with details
ls -la

# Create directory
mkdir new_folder

# Create file
New-Item -Path "filename.txt" -ItemType File

# Copy file
Copy-Item source.py destination.py

# Move/rename file
Move-Item old.py new.py

# Delete file
Remove-Item filename.py

# View file content
Get-Content filename.py

# View first 20 lines
Get-Content filename.py -Head 20
```

---

## 🐍 Python Commands

```bash
# Check Python version
python --version

# Install package
pip install package-name

# Install from requirements
pip install -r requirements.txt

# List installed packages
pip list

# Show package info
pip show pandas

# Uninstall package
pip uninstall package-name

# Create requirements file
pip freeze > requirements.txt

# Update pip
python -m pip install --upgrade pip
```

---

## 📊 Data Analysis Quick Commands

```bash
# Load and inspect data (Python one-liner)
python -c "import pandas as pd; df = pd.read_csv('data/sample_transactions.csv'); print(df.head())"

# Check dataset size
python -c "import pandas as pd; df = pd.read_csv('data/raw/creditcard.csv'); print(f'Shape: {df.shape}')"

# Count fraud cases
python -c "import pandas as pd; df = pd.read_csv('data/raw/creditcard.csv'); print(df['Class'].value_counts())"
```

---

## 🧹 Cleanup Commands

```bash
# Remove Python cache
Remove-Item -Recurse -Force __pycache__

# Remove all .pyc files
Get-ChildItem -Recurse -Filter "*.pyc" | Remove-Item

# Remove Jupyter checkpoints
Remove-Item -Recurse -Force .ipynb_checkpoints

# Clean all cache and temp files
Remove-Item -Recurse -Force __pycache__, .ipynb_checkpoints, *.pyc
```

---

## 📈 Model Testing

```bash
# Quick test with sample data
python -c "from src.data_loader import FraudDataLoader; loader = FraudDataLoader(); df = loader.load_sample_data(); print(df.head())"

# Test model loading
python -c "import joblib; model = joblib.load('models/fraud_detector.pkl'); print('✅ Model loaded')"

# Test prediction pipeline
python -c "from src.predict import FraudPredictor; predictor = FraudPredictor(); print('✅ Predictor ready')"
```

---

## 🔧 Troubleshooting

```bash
# Check if port is in use
netstat -ano | findstr :5000

# Kill process on port (replace PID)
taskkill /PID 12345 /F

# Reinstall corrupted package
pip uninstall pandas
pip install pandas

# Fix permissions (run as admin)
python -m pip install --user package-name

# Check disk space
Get-PSDrive C
```

---

## 📝 Useful One-Liners

```bash
# Count Python files
(Get-ChildItem -Recurse -Filter "*.py").Count

# Find files modified today
Get-ChildItem -Recurse | Where-Object {$_.LastWriteTime -gt (Get-Date).Date}

# Check project size
Get-ChildItem -Recurse | Measure-Object -Property Length -Sum

# Search for text in files
Get-ChildItem -Recurse -Filter "*.py" | Select-String "TODO"

# Count lines of code
(Get-Content (Get-ChildItem -Recurse -Filter "*.py")).Count
```

---

## 🎯 Pre-Presentation Checklist

```bash
# 1. Update repository
git pull origin main

# 2. Activate environment
.\.venv\Scripts\Activate.ps1

# 3. Test notebooks
jupyter notebook notebooks/01_EDA.ipynb

# 4. Train model
python src/train_model.py

# 5. Test predictions
python src/predict.py --demo

# 6. Start API
python api/app.py

# 7. Commit everything
git add .
git commit -m "Final preparation for presentation"
git push origin main
```

---

## 🆘 Emergency Commands

```bash
# Forgot to activate venv and installed globally?
pip list  # See what's installed globally
deactivate  # Make sure venv is off
pip uninstall package-name  # Remove from global

# Accidentally committed large file?
git rm --cached data/raw/creditcard.csv
git commit -m "Remove large file"
git push origin main

# Code stopped working?
git log --oneline  # Find last working commit
git checkout abc123 -- src/predict.py  # Restore specific file

# Lost work before commit?
git reflog  # Shows all actions
git checkout HEAD@{1}  # Go back in time
```

---

## 🎓 Command Aliases (Optional)

Add to your PowerShell profile for shortcuts:

```powershell
# Edit profile
notepad $PROFILE

# Add these aliases:
function gst { git status }
function gaa { git add . }
function gcm { git commit -m $args }
function gp { git push origin main }
function jn { jupyter notebook }
function av { .\.venv\Scripts\Activate.ps1 }
function train { python src/train_model.py }
function pred { python src/predict.py --demo }
```

Then use:
```bash
gst     # Instead of: git status
gaa     # Instead of: git add .
gcm "message"  # Instead of: git commit -m "message"
```

---

## 📚 Learn More

- Git: https://git-scm.com/docs
- Python: https://docs.python.org/3/
- Pandas: https://pandas.pydata.org/docs/
- Scikit-learn: https://scikit-learn.org/stable/
- Flask: https://flask.palletsprojects.com/

---

**Team Three Unknowns - VRSEC**

*Quick Reference - Keep this handy!*

*Last Updated: January 2, 2026*
