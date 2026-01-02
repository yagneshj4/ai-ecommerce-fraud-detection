# React Frontend Setup

## 📁 Frontend Structure
```
frontend/
├── package.json          # Dependencies
├── vite.config.js        # Vite configuration
├── tailwind.config.js    # Tailwind CSS config
├── postcss.config.js     # PostCSS config
├── index.html            # HTML entry point
└── src/
    ├── main.jsx          # React entry point
    ├── App.jsx           # Main app component
    ├── index.css         # Global styles
    ├── components/
    │   ├── TransactionForm.jsx
    │   └── ResultCard.jsx
    └── services/
        └── api.js        # API communication
```

## 🚀 Quick Start

### 1. Install Node.js
Ensure Node.js 18+ is installed:
```bash
node --version
npm --version
```

### 2. Install Dependencies
```bash
cd frontend
npm install
```

This installs:
- React 18.2
- Vite 5.0
- Tailwind CSS 3.4
- Axios 1.6

### 3. Run Development Server
```bash
npm run dev
```

Access at: **http://localhost:5173**

### 4. Build for Production
```bash
npm run build
```

Output in `dist/` folder.

## 🎨 Features

### ✅ Real-Time Prediction
- Submit form → API call → Instant results
- No page reloads

### ✅ Loading States
- Animated spinner during prediction
- Disabled buttons to prevent double submission

### ✅ Error Handling
- Connection errors
- Backend errors
- User-friendly error messages

### ✅ Responsive Design
- Mobile-friendly
- Tablet-optimized
- Desktop layout

### ✅ Preset Buttons
- Genuine transaction ($25.50)
- Suspicious transaction ($2,500)
- Medium risk transaction ($150)

## 🔧 Configuration

### API Endpoint
Located in `src/services/api.js`:
```javascript
const API_BASE_URL = '/api';  // Development (uses proxy)
// or
const API_BASE_URL = 'http://localhost:8000';  // Production
```

### Vite Proxy
Configured in `vite.config.js`:
```javascript
proxy: {
  '/api': {
    target: 'http://localhost:8000',
    changeOrigin: true,
    rewrite: (path) => path.replace(/^\/api/, '')
  }
}
```

## 🐛 Troubleshooting

**Error: Cannot GET /api/predict**
```
Solution: Ensure backend is running on port 8000
cd backend
python main.py
```

**Error: npm install fails**
```bash
# Delete node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

**Tailwind styles not loading**
```bash
# Ensure PostCSS and Tailwind are installed
npm install -D tailwindcss postcss autoprefixer
```

## 📱 Mobile Testing

Access from phone on same network:
1. Find your IP: `ipconfig` (Windows) or `ifconfig` (Mac/Linux)
2. Run: `npm run dev -- --host`
3. Visit: `http://YOUR_IP:5173`
