# 🌐 Web Interface Documentation

## AI Fraud Detection System - Frontend Guide

**Team:** Three Unknowns | **Institution:** VRSEC

---

## 📁 Folder Structure

```
api/
├── app.py                      # Flask backend (updated)
├── templates/
│   └── index.html             # Main web interface
├── static/
│   ├── css/
│   │   └── style.css          # Professional stylesheet
│   └── js/
│       └── app.js             # Frontend logic
```

---

## 🎯 What Each File Does

### 1️⃣ **app.py** (Flask Backend)

**Purpose:** Serves the web interface and handles API requests

**Key Changes Made:**
```python
# Fixed model path issue
model_dir = Path(__file__).parent.parent / 'models'
MODEL = load_model(str(model_dir / 'fraud_detector.pkl'))

# Added routes
@app.route('/')               # Main web interface
@app.route('/docs')           # API documentation
@app.route('/predict')        # Prediction endpoint (POST)
```

**How It Works:**
1. Loads trained ML model on startup
2. Serves HTML template at `/`
3. Accepts POST requests at `/predict`
4. Returns JSON prediction results

---

### 2️⃣ **index.html** (Web Interface)

**Purpose:** Professional, viva-ready user interface

**Sections:**

#### **Header**
- Project title with shield icon
- Team and institution info
- "Model Active" status badge

#### **Project Info Card**
- Project description
- Model performance metrics (92% recall, 97% ROC-AUC)
- Academic context

#### **Input Form (Left Column)**
- **Basic Fields:**
  - Transaction Amount (required)
  - Time since account creation (required)
  
- **Advanced Fields (Collapsible):**
  - V1-V28 PCA features
  - Hidden by default, expandable for testing
  
- **Quick Presets:**
  - Small Genuine Purchase ($25.50)
  - Large Suspicious Order ($2,500)
  - Medium Transaction ($150)

#### **Results Panel (Right Column)**
Shows 4 states:

1. **Placeholder:** "Awaiting Transaction Data"
2. **Loading:** Spinner with "Analyzing..."
3. **Results:** 
   - Green/Red prediction badge
   - Fraud probability meter
   - Risk level indicator
   - Recommendation box
   - Transaction summary
4. **Error:** Error message with retry button

#### **Model Stats Cards**
- 92% Recall
- 97% ROC-AUC
- 30 Features
- 284K Training Data

#### **Footer**
- Team credits
- Links to API docs and GitHub

---

### 3️⃣ **style.css** (Stylesheet)

**Purpose:** Modern, professional design

**Design Features:**

#### **Color Scheme**
- Primary: Blue (#2563eb) - Trust, technology
- Success: Green (#10b981) - Genuine transactions
- Danger: Red (#ef4444) - Fraud alerts
- Grays: Clean, academic look

#### **Layout**
- Responsive grid (2 columns on desktop, 1 on mobile)
- Sticky header and results panel
- Card-based design with shadows

#### **Animations**
- Smooth transitions
- Slide-in results
- Pulsing status dot
- Hover effects on buttons

#### **Responsive Design**
- Desktop: 2-column layout
- Tablet: Single column
- Mobile: Optimized for small screens

---

### 4️⃣ **app.js** (JavaScript Logic)

**Purpose:** Handle user interactions and API communication

**Key Functions:**

#### **initializeAdvancedFields()**
```javascript
// Dynamically creates V1-V28 input fields
```

#### **toggleAdvanced()**
```javascript
// Shows/hides advanced PCA features
```

#### **loadPreset(presetName)**
```javascript
// Loads pre-configured transaction data
// Options: 'genuine', 'suspicious', 'medium'
```

#### **collectFormData()**
```javascript
// Gathers all form inputs into JSON
{
    "Time": 1000,
    "Amount": 149.99,
    "V1": 0.5,
    ...
}
```

#### **predictFraud(data)**
```javascript
// Sends POST request to /predict
// Returns prediction results
```

#### **displayResults(result)**
```javascript
// Updates UI with prediction:
// - Changes badge color (green/red)
// - Updates probability meter
// - Shows risk level
// - Displays recommendation
```

**Flow:**
```
User fills form → Submit → Validate → API Call → Update UI
```

---

## 🔄 Complete Data Flow

### **Frontend → Backend → Model → Frontend**

```
1. User Interface (index.html)
   ↓
   User enters transaction details
   ↓

2. JavaScript (app.js)
   ↓
   Collects form data as JSON
   ↓
   Sends POST to /predict
   ↓

3. Flask Backend (app.py)
   ↓
   Receives JSON request
   ↓
   Preprocesses data (scaling)
   ↓

4. ML Model (fraud_detector.pkl)
   ↓
   Analyzes 30 features
   ↓
   Returns prediction & probability
   ↓

5. Flask Backend (app.py)
   ↓
   Formats response as JSON
   {
     "prediction": "FRAUD",
     "fraud_probability": 0.87,
     "confidence": 87.23,
     "risk_level": "HIGH",
     "recommendation": "BLOCK transaction"
   }
   ↓

6. JavaScript (app.js)
   ↓
   Receives response
   ↓
   Updates UI dynamically
   ↓

7. User Interface (index.html)
   ↓
   Displays results with colors, icons, recommendations
```

---

## 🚀 How to Run

### **Step 1: Start the Server**

```bash
# Navigate to project directory
cd c:\Users\HP\OneDrive\Desktop\mini

# Start Flask server
python api/app.py
```

**Expected Output:**
```
🔧 Loading fraud detection model...
✅ Model loaded successfully!

FRAUD DETECTION API SERVER
======================================
🚀 Starting server...
📍 API URL: http://localhost:5000

* Running on http://127.0.0.1:5000
```

### **Step 2: Open in Browser**

```
http://localhost:5000
```

### **Step 3: Test the System**

**Option A: Use Presets**
1. Click "Small Genuine Purchase"
2. Click "Analyze Transaction"
3. See green "GENUINE" result

**Option B: Manual Entry**
1. Enter Amount: `2500`
2. Enter Time: `5000`
3. Modify V1 and V2 (optional)
4. Click "Analyze Transaction"
5. See red "FRAUD" result

---

## 🎨 UI Components Explained

### **Prediction Badge**

**Green (Genuine):**
```
✓ GENUINE
97.9% confidence
Very Low Risk
```

**Red (Fraud):**
```
✗ FRAUD
87.2% confidence
High Risk
```

### **Probability Meter**
- Visual bar showing 0-100%
- Green → Yellow → Red gradient
- Animates smoothly

### **Risk Levels**
- **VERY LOW:** 0-25% probability
- **LOW:** 25-50%
- **MEDIUM:** 50-75%
- **HIGH:** 75-100%

### **Recommendations**
- **Genuine:** "APPROVE transaction. Appears genuine."
- **Fraud:** "BLOCK transaction immediately. Manual review required."

---

## 🎓 For Viva / Demo

### **What to Show**

1. **Homepage Tour** (30 seconds)
   - Point out project title
   - Mention team and institution
   - Show model stats (92% recall, 97% AUC)

2. **Demo Genuine Transaction** (1 minute)
   - Click "Small Genuine Purchase" preset
   - Click "Analyze Transaction"
   - Show green result
   - Explain low probability meter

3. **Demo Fraud Transaction** (1 minute)
   - Click "Large Suspicious Order" preset
   - Click "Analyze Transaction"
   - Show red result
   - Explain high probability and recommendation

4. **Show Advanced Features** (30 seconds)
   - Click "Advanced Features" to expand
   - Show V1-V28 fields
   - Explain these are PCA components

5. **Explain Technology** (1 minute)
   - HTML/CSS/JavaScript frontend
   - Flask backend
   - Logistic Regression model
   - JSON API communication

---

## 🔧 Customization

### **Change Colors**

In `style.css`:
```css
:root {
    --primary-color: #2563eb;   /* Change to your color */
    --success-color: #10b981;
    --danger-color: #ef4444;
}
```

### **Modify Presets**

In `app.js`:
```javascript
const PRESETS = {
    genuine: {
        Time: 1000,
        Amount: 25.50,
        // ... modify values
    }
};
```

### **Add New Features**

1. Edit `index.html` - Add form field
2. Edit `app.js` - Collect new data
3. Edit `app.py` - Process new feature

---

## 🐛 Troubleshooting

### **Issue 1: Blank Page**

**Cause:** Flask template not found

**Fix:**
```bash
# Verify folder structure
api/
├── templates/
│   └── index.html     # Must be here
```

### **Issue 2: Styles Not Loading**

**Cause:** Static files path incorrect

**Fix:** Check `index.html`:
```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

### **Issue 3: Prediction Fails**

**Cause:** Model not loaded

**Fix:** Check console output:
```
✅ Model loaded successfully!  ← Should see this
```

If not, retrain model:
```bash
python src/train_model.py
```

### **Issue 4: CORS Errors**

**Cause:** Cross-origin request blocked

**Fix:** Already handled in `app.py`:
```python
from flask_cors import CORS
CORS(app)
```

---

## 📊 Technical Architecture

```
┌─────────────────────────────────────────┐
│         USER BROWSER                     │
│                                          │
│  ┌────────────────────────────────┐    │
│  │      index.html                 │    │
│  │  (User Interface)               │    │
│  └───────────┬────────────────────┘    │
│              │                           │
│  ┌───────────▼────────────────────┐    │
│  │      style.css                  │    │
│  │  (Visual Design)                │    │
│  └─────────────────────────────────┘    │
│              │                           │
│  ┌───────────▼────────────────────┐    │
│  │      app.js                     │    │
│  │  (Logic & API Calls)            │    │
│  └───────────┬────────────────────┘    │
└──────────────┼──────────────────────────┘
               │ HTTP POST /predict
               │ JSON: {Time, Amount, V1-V28}
               ▼
┌──────────────────────────────────────────┐
│         FLASK SERVER                      │
│                                           │
│  ┌────────────────────────────────┐     │
│  │      app.py                     │     │
│  │  (Route Handler)                │     │
│  └───────────┬────────────────────┘     │
│              │                            │
│  ┌───────────▼────────────────────┐     │
│  │   Preprocessing                 │     │
│  │   (Scaling, Validation)         │     │
│  └───────────┬────────────────────┘     │
│              │                            │
│  ┌───────────▼────────────────────┐     │
│  │   fraud_detector.pkl            │     │
│  │   (ML Model)                    │     │
│  └───────────┬────────────────────┘     │
│              │                            │
│  ┌───────────▼────────────────────┐     │
│  │   Response Generation           │     │
│  │   {prediction, probability}     │     │
│  └───────────┬────────────────────┘     │
└──────────────┼──────────────────────────┘
               │ HTTP 200 OK
               │ JSON Response
               ▼
┌──────────────────────────────────────────┐
│         USER BROWSER                      │
│                                           │
│  ┌────────────────────────────────┐     │
│  │   Results Display               │     │
│  │   - Prediction Badge            │     │
│  │   - Probability Meter           │     │
│  │   - Recommendation              │     │
│  └─────────────────────────────────┘     │
└───────────────────────────────────────────┘
```

---

## 🏆 Best Practices Followed

### ✅ **Clean Code**
- Commented JavaScript
- Organized CSS with sections
- Semantic HTML

### ✅ **Responsive Design**
- Works on desktop, tablet, mobile
- Sticky navigation
- Adaptive layout

### ✅ **User Experience**
- Clear visual feedback
- Loading states
- Error handling
- Preset buttons for quick testing

### ✅ **Performance**
- Minimal dependencies
- Optimized CSS (no frameworks)
- Vanilla JavaScript (no jQuery)
- Fast load times

### ✅ **Academic Standards**
- Professional appearance
- Clear documentation
- Team credits
- Project context

---

## 📝 Code Statistics

| File | Lines | Purpose |
|------|-------|---------|
| **index.html** | ~330 | User interface structure |
| **style.css** | ~800 | Visual design & layout |
| **app.js** | ~350 | Frontend logic & API calls |
| **Total** | ~1,480 | Complete web interface |

---

## 🎉 Features Summary

✅ **Professional Design** - Clean, modern UI  
✅ **Responsive Layout** - Works on all devices  
✅ **Real-time Predictions** - Instant results  
✅ **Visual Feedback** - Colors, icons, animations  
✅ **Preset Transactions** - Quick testing  
✅ **Advanced Options** - Collapsible V1-V28 fields  
✅ **Error Handling** - Graceful failure states  
✅ **Model Stats Display** - Shows performance metrics  
✅ **Viva-Ready** - Perfect for demonstrations  

---

**Team Three Unknowns - VRSEC**  
*Web Interface v1.0 | January 2026*

---

## 🚀 Quick Test Commands

```bash
# Start server
python api/app.py

# Open browser
start http://localhost:5000

# Test presets
# Click: Small Genuine Purchase → Analyze
# Click: Large Suspicious Order → Analyze

# Done! Ready for presentation.
```
