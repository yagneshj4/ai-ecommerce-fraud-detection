# ⚡ QUICK START CARD

**AI Fraud Detection System - Full Stack**  
**Copy this to your desktop for quick reference!**

---

## 🚀 START THE APPLICATION

### Terminal 1: Backend (FastAPI)
```bash
cd C:\Users\HP\OneDrive\Desktop\mini\backend
python main.py
```
✅ Backend ready at: **http://localhost:8000**

---

### Terminal 2: Frontend (React)
```bash
cd C:\Users\HP\OneDrive\Desktop\mini\frontend
npm run dev
```
✅ Frontend ready at: **http://localhost:5173**

---

## 🌐 ACCESS POINTS

| What | URL |
|------|-----|
| **Web App (use this!)** | http://localhost:5173 |
| **API Documentation** | http://localhost:8000/docs |
| **Backend Health Check** | http://localhost:8000 |

---

## 🎬 DEMO STEPS (30 SECONDS)

1. Open http://localhost:5173
2. Click **"✓ Genuine"** → **"Analyze"**
3. See GREEN result (low fraud)
4. Click **"⚠️ Suspicious"** → **"Analyze"**
5. See RED result (high fraud)

---

## 🐛 IF SOMETHING BREAKS

**Backend won't start?**
```bash
cd backend
pip install -r requirements.txt
```

**Frontend won't start?**
```bash
cd frontend
npm install
```

**Can't connect to API?**
- Make sure BOTH terminals are running
- Backend must be on port 8000
- Frontend must be on port 5173

**Port already in use?**
```bash
# Kill process on port 8000
netstat -ano | findstr :8000
taskkill /PID <number> /F
```

---

## 📊 TECH STACK (FOR VIVA)

**Frontend:** React + Vite + Tailwind CSS  
**Backend:** FastAPI + Python  
**ML Model:** Logistic Regression (Scikit-learn)  
**Performance:** 92% Recall | 97% ROC-AUC

---

## 🎓 KEY VIVA POINTS

**Q: Why React + FastAPI?**  
A: Modern industry stack, faster development, better UX, microservices architecture

**Q: How does it work?**  
A: React → HTTP POST → FastAPI → ML Model → JSON response → Update UI

**Q: Production deployment?**  
A: Frontend → Vercel/Azure, Backend → Docker → Azure App Service

---

## 📁 PROJECT STRUCTURE

```
mini/
├── backend/          # FastAPI (port 8000)
│   ├── main.py       # API server
│   └── models/       # ML models
├── frontend/         # React (port 5173)
│   └── src/          # React components
└── notebooks/        # Jupyter (training)
```

---

## 🏆 SUBMISSION CHECKLIST

- ✅ Backend folder (with models/)
- ✅ Frontend folder (NO node_modules!)
- ✅ notebooks/ (EDA + training)
- ✅ README.md
- ✅ FULLSTACK_SETUP_GUIDE.md
- ✅ Screenshots (7 total)
- ✅ Report PDF

---

**Good luck! 🎉**

*Print this and keep it handy during demo/viva*
