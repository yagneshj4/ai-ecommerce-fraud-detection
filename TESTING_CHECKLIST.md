# ✅ PRE-VIVA TESTING CHECKLIST

**Complete this checklist 24 hours before your viva/demo**

---

## 🔧 ENVIRONMENT CHECK

### Python Environment
```bash
python --version
# Expected: Python 3.9 or higher

pip list | findstr "fastapi scikit-learn pandas"
# Expected: All packages installed
```
- [ ] Python 3.9+ installed
- [ ] All backend dependencies installed

### Node.js Environment
```bash
node --version
# Expected: v18.0.0 or higher

npm --version
# Expected: 9.0.0 or higher
```
- [ ] Node.js 18+ installed
- [ ] npm installed

---

## 📁 FILE INTEGRITY CHECK

### Backend Files
- [ ] `backend/main.py` exists and is readable
- [ ] `backend/model_loader.py` exists
- [ ] `backend/requirements.txt` exists
- [ ] `backend/models/fraud_detector.pkl` exists (file size ~1-5 MB)
- [ ] `backend/models/scaler.pkl` exists (file size ~1-5 KB)

### Frontend Files
- [ ] `frontend/package.json` exists
- [ ] `frontend/src/App.jsx` exists
- [ ] `frontend/src/components/TransactionForm.jsx` exists
- [ ] `frontend/src/components/ResultCard.jsx` exists
- [ ] `frontend/src/services/api.js` exists
- [ ] `frontend/vite.config.js` exists

### Documentation Files
- [ ] `README.md` updated with new architecture
- [ ] `FULLSTACK_SETUP_GUIDE.md` exists
- [ ] `QUICK_START.md` exists
- [ ] `ACADEMIC_JUSTIFICATION.md` exists

---

## 🚀 BACKEND TESTING

### Step 1: Start Backend
```bash
cd backend
python main.py
```

**Expected Output:**
```
INFO:     ✅ Model loaded successfully!
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

- [ ] No error messages
- [ ] "Model loaded successfully" appears
- [ ] Server running on port 8000

### Step 2: Test Health Endpoint
Open browser: http://localhost:8000

**Expected Response:**
```json
{
  "status": "active",
  "message": "AI Fraud Detection API is running",
  "model_loaded": true,
  "version": "1.0.0"
}
```

- [ ] Page loads without errors
- [ ] `"model_loaded": true` is present
- [ ] JSON is properly formatted

### Step 3: Test API Documentation
Open browser: http://localhost:8000/docs

- [ ] Swagger UI loads
- [ ] `/predict` endpoint is visible
- [ ] Can expand `/predict` and see request schema

### Step 4: Test Prediction (Using Swagger)
1. Click on `/predict` → "Try it out"
2. Enter test data:
```json
{
  "Amount": 25.50,
  "Time": 1000
}
```
3. Click "Execute"

**Expected Response:**
```json
{
  "prediction": "Genuine",
  "fraud_probability": <some number>,
  "genuine_probability": <some number>,
  "risk_level": "VERY LOW" or "LOW",
  "recommendation": "APPROVE transaction...",
  "confidence": <some number>
}
```

- [ ] Response code: 200
- [ ] Prediction is either "Genuine" or "Fraud"
- [ ] All fields present
- [ ] No error messages

---

## 🎨 FRONTEND TESTING

### Step 1: Install Dependencies
```bash
cd frontend
npm install
```

**Expected Output:**
```
added XXX packages in XXs
```

- [ ] No error messages
- [ ] `node_modules/` folder created
- [ ] `package-lock.json` created

### Step 2: Start Frontend
```bash
npm run dev
```

**Expected Output:**
```
  VITE v5.0.11  ready in 1234 ms

  ➜  Local:   http://localhost:5173/
```

- [ ] No error messages
- [ ] Server running on port 5173
- [ ] Terminal shows "ready" message

### Step 3: Open Application
Open browser: http://localhost:5173

- [ ] Page loads completely
- [ ] No console errors (press F12 → Console tab)
- [ ] Header displays "🛡️ AI Fraud Detection System"
- [ ] Blue banner shows "Team: Three Unknowns"
- [ ] Left side: Transaction form visible
- [ ] Right side: "Awaiting Prediction" card visible

### Step 4: Test Preset Buttons
Click each preset button:

**Genuine Preset:**
- [ ] Amount field shows "25.50"
- [ ] Time field shows "1000"

**Suspicious Preset:**
- [ ] Amount field shows "2500"
- [ ] Time field shows "5000"

**Medium Preset:**
- [ ] Amount field shows "150"
- [ ] Time field shows "3000"

### Step 5: Test Form Validation
1. Clear all fields
2. Click "🔍 Analyze Transaction"

- [ ] Form prevents submission (required fields)
- [ ] Browser shows validation message

### Step 6: Test Real Prediction

**Test A: Genuine Transaction**
1. Click "✓ Genuine" preset
2. Click "🔍 Analyze Transaction"
3. Wait for response

**Expected Result:**
- [ ] Loading spinner appears
- [ ] "Analyzing Transaction..." message shows
- [ ] After 1-3 seconds, result card appears
- [ ] Result card is GREEN
- [ ] Shows "Genuine" or "✅"
- [ ] Fraud probability is LOW (< 20%)
- [ ] Risk level: "VERY LOW" or "LOW"
- [ ] Recommendation: "APPROVE transaction"
- [ ] Probability meter shows green bar (small)

**Test B: Fraudulent Transaction**
1. Click "⚠️ Suspicious" preset
2. Click "🔍 Analyze Transaction"

**Expected Result:**
- [ ] Loading spinner appears
- [ ] Result card appears after 1-3 seconds
- [ ] Result card is RED
- [ ] Shows "Fraud" or "🚨"
- [ ] Fraud probability is HIGH (> 80%)
- [ ] Risk level: "HIGH" or "VERY HIGH"
- [ ] Recommendation: "REJECT transaction"
- [ ] Probability meter shows red bar (large)

### Step 7: Test Clear Button
- [ ] Click "Clear" button
- [ ] All fields reset to empty
- [ ] Result card resets to "Awaiting Prediction"

---

## 🔍 ADVANCED TESTING

### Test Advanced Features
1. Click "▶ Advanced Features (V1-V28 PCA Components)"
- [ ] Section expands
- [ ] Shows grid of V1-V28 input fields
- [ ] All fields accept numbers
- [ ] Can enter values like "0.5", "-1.2"

### Test Error Handling

**Test: Backend Offline**
1. Stop backend server (Ctrl+C in backend terminal)
2. In frontend, try to submit transaction

**Expected:**
- [ ] Error card appears (red border)
- [ ] Shows "Prediction Failed"
- [ ] Error message mentions "Cannot connect to API"
- [ ] Suggests checking if backend is running

### Test Network Tab (DevTools)
1. Open DevTools (F12) → Network tab
2. Submit a transaction
3. Look for request to `/api/predict` or `localhost:8000/predict`

**Expected:**
- [ ] Request appears in network tab
- [ ] Request method: POST
- [ ] Request payload shows transaction data
- [ ] Response status: 200 OK
- [ ] Response shows prediction JSON

---

## 📱 RESPONSIVE DESIGN TESTING

### Desktop (Current Window)
- [ ] Layout looks good
- [ ] Two-column grid (form | results)
- [ ] No horizontal scrolling

### Tablet Simulation
1. Press F12 → Toggle device toolbar (Ctrl+Shift+M)
2. Select "iPad" or set width to 768px

- [ ] Layout adjusts appropriately
- [ ] Elements stack vertically if needed
- [ ] Text is readable

### Mobile Simulation
Set width to 375px (iPhone size)

- [ ] Single column layout
- [ ] Form fills width
- [ ] Buttons stack or resize
- [ ] Text is readable (not cut off)

---

## 🎬 DEMO REHEARSAL

### Practice Full Demo (2 minutes)

**Script:**
1. Open application → 10 seconds
2. Explain interface → 20 seconds
3. Test genuine transaction → 20 seconds
4. Test fraudulent transaction → 20 seconds
5. Show architecture (DevTools) → 20 seconds
6. Explain tech stack → 30 seconds

**Checklist:**
- [ ] Can complete demo in under 2 minutes
- [ ] No stuttering or confusion
- [ ] Both transactions work correctly
- [ ] Can explain each component

### Answer Practice Questions

Test yourself (without looking):
- [ ] Can explain how React communicates with FastAPI
- [ ] Can describe the data flow (user input → API → model → response)
- [ ] Can justify why React instead of HTML
- [ ] Can explain CORS and why it's needed
- [ ] Can list all technologies used

---

## 📸 SCREENSHOT PREPARATION

### Required Screenshots

**1. Backend API Docs**
- URL: http://localhost:8000/docs
- [ ] Screenshot saved as `screenshots/1_backend_swagger.png`

**2. Backend Health Check**
- URL: http://localhost:8000
- [ ] Screenshot saved as `screenshots/2_backend_health.png`

**3. Frontend Homepage**
- URL: http://localhost:5173
- [ ] Screenshot saved as `screenshots/3_frontend_home.png`

**4. Genuine Transaction Result**
- [ ] Screenshot saved as `screenshots/4_genuine_result.png`

**5. Fraudulent Transaction Result**
- [ ] Screenshot saved as `screenshots/5_fraud_result.png`

**6. Network Tab (DevTools)**
- [ ] Screenshot saved as `screenshots/6_network_request.png`

**7. Terminal Outputs**
- [ ] Screenshot showing both terminals running
- [ ] Saved as `screenshots/7_terminals.png`

---

## 🐛 COMMON ISSUES - QUICK FIXES

### Backend Issues

**Issue: "Model not found"**
```bash
# Fix: Copy models
Copy-Item models\*.pkl backend\models\
```

**Issue: "Port 8000 already in use"**
```bash
# Fix: Kill process
netstat -ano | findstr :8000
taskkill /PID <number> /F
```

**Issue: "Module not found"**
```bash
# Fix: Reinstall dependencies
cd backend
pip install -r requirements.txt
```

### Frontend Issues

**Issue: "npm: command not found"**
- Install Node.js from https://nodejs.org

**Issue: "Cannot find module 'react'"**
```bash
# Fix: Reinstall
cd frontend
rm -rf node_modules package-lock.json
npm install
```

**Issue: "Tailwind styles not loading"**
```bash
# Fix: Clear cache and rebuild
npm run dev
```

---

## ✅ FINAL GO/NO-GO DECISION

### All Green? You're Ready!

- [ ] Backend starts without errors ✅
- [ ] Frontend starts without errors ✅
- [ ] API docs accessible ✅
- [ ] Genuine transaction works ✅
- [ ] Fraudulent transaction works ✅
- [ ] UI looks professional ✅
- [ ] Can demo in under 2 minutes ✅
- [ ] Can answer all viva questions ✅
- [ ] Screenshots prepared ✅
- [ ] Documentation complete ✅

### If ANY item is unchecked:
1. Fix the issue using troubleshooting guides
2. Re-test that specific item
3. Continue until ALL items are checked

---

## 🎓 DAY-OF-VIVA CHECKLIST

### 30 Minutes Before:
- [ ] Restart computer (fresh start)
- [ ] Close all unnecessary applications
- [ ] Test internet connection (if needed)
- [ ] Charge laptop fully
- [ ] Bring backup USB with project files

### 10 Minutes Before:
- [ ] Start backend server
- [ ] Start frontend server
- [ ] Test one prediction (gentle or suspicious)
- [ ] Open QUICK_START.md for reference
- [ ] Open ACADEMIC_JUSTIFICATION.md for tough questions

### During Demo:
- [ ] Speak clearly and confidently
- [ ] Let application load fully before clicking
- [ ] If something breaks, explain calmly (have fixes ready)
- [ ] Reference documentation when needed

---

## 📞 EMERGENCY CONTACTS

**If system fails during demo:**
- Have backup video recording ready
- Show screenshots as fallback
- Explain what SHOULD happen
- Offer to fix and re-demo

---

**Good luck! You've got this! 🚀**

*Complete this checklist and sign below:*

Tested by: ________________  
Date: ________________  
Time: ________________  
Status: ✅ READY / ⚠️ NEEDS FIXES
