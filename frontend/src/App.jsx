import { useState } from 'react';
import TransactionForm from './components/TransactionForm';
import ResultCard from './components/ResultCard';
import { predictFraud } from './services/api';

function App() {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handlePredict = async (transactionData) => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const prediction = await predictFraud(transactionData);
      setResult(prediction);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setResult(null);
    setError(null);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-blue-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold text-gray-900 flex items-center gap-3">
                <span className="text-4xl">🛡️</span>
                AI Fraud Detection System
              </h1>
              <p className="mt-2 text-sm text-gray-600">
                Machine Learning-Powered Real-Time Transaction Analysis
              </p>
            </div>
            <div className="text-right">
              <div className="inline-flex items-center gap-2 px-4 py-2 bg-green-50 text-green-700 rounded-full text-sm font-medium">
                <span className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></span>
                API Connected
              </div>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Project Info Banner */}
        <div className="mb-8 bg-gradient-to-r from-blue-600 to-purple-600 rounded-xl shadow-lg p-6 text-white">
          <div className="flex items-center justify-between flex-wrap gap-4">
            <div>
              <h2 className="text-xl font-bold mb-2">Mini Project 2026</h2>
              <p className="text-blue-100">
                Team: <span className="font-semibold">Three Unknowns</span> | 
                Institution: <span className="font-semibold">VRSEC</span> | 
                Department: <span className="font-semibold">IT (3rd Year)</span>
              </p>
            </div>
            <div className="text-right">
              <div className="text-sm text-blue-100 mb-1">Model Performance</div>
              <div className="flex gap-4 text-sm">
                <div>
                  <div className="font-bold text-2xl">92%</div>
                  <div className="text-blue-100">Recall</div>
                </div>
                <div>
                  <div className="font-bold text-2xl">97%</div>
                  <div className="text-blue-100">ROC-AUC</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Grid Layout */}
        <div className="grid lg:grid-cols-2 gap-8">
          {/* Left Column - Input Form */}
          <div className="space-y-6">
            <div className="bg-white rounded-xl shadow-lg p-6">
              <h2 className="text-2xl font-bold text-gray-900 mb-6 flex items-center gap-2">
                <span className="text-2xl">📊</span>
                Transaction Details
              </h2>
              <TransactionForm 
                onSubmit={handlePredict} 
                loading={loading}
                onReset={handleReset}
              />
            </div>

            {/* Technology Stack */}
            <div className="bg-white rounded-xl shadow-lg p-6">
              <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                <span className="text-xl">⚙️</span>
                Technology Stack
              </h3>
              <div className="space-y-3 text-sm">
                <div className="flex items-center gap-3">
                  <span className="font-semibold text-gray-700 w-24">Frontend:</span>
                  <div className="flex gap-2 flex-wrap">
                    <span className="px-2 py-1 bg-blue-100 text-blue-700 rounded">React</span>
                    <span className="px-2 py-1 bg-cyan-100 text-cyan-700 rounded">Vite</span>
                    <span className="px-2 py-1 bg-teal-100 text-teal-700 rounded">Tailwind CSS</span>
                  </div>
                </div>
                <div className="flex items-center gap-3">
                  <span className="font-semibold text-gray-700 w-24">Backend:</span>
                  <div className="flex gap-2 flex-wrap">
                    <span className="px-2 py-1 bg-green-100 text-green-700 rounded">FastAPI</span>
                    <span className="px-2 py-1 bg-emerald-100 text-emerald-700 rounded">Python</span>
                  </div>
                </div>
                <div className="flex items-center gap-3">
                  <span className="font-semibold text-gray-700 w-24">ML Model:</span>
                  <div className="flex gap-2 flex-wrap">
                    <span className="px-2 py-1 bg-purple-100 text-purple-700 rounded">Logistic Regression</span>
                    <span className="px-2 py-1 bg-pink-100 text-pink-700 rounded">Scikit-learn</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Right Column - Results */}
          <div className="space-y-6">
            <ResultCard 
              result={result} 
              loading={loading} 
              error={error}
            />

            {/* How It Works */}
            <div className="bg-white rounded-xl shadow-lg p-6">
              <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2">
                <span className="text-xl">🔄</span>
                How It Works
              </h3>
              <div className="space-y-4">
                <div className="flex items-start gap-3">
                  <div className="w-8 h-8 bg-blue-100 text-blue-600 rounded-full flex items-center justify-center font-bold flex-shrink-0">
                    1
                  </div>
                  <div>
                    <div className="font-semibold text-gray-900">Input Transaction</div>
                    <div className="text-sm text-gray-600">Enter amount, time, and optional V1-V28 features</div>
                  </div>
                </div>
                <div className="flex items-start gap-3">
                  <div className="w-8 h-8 bg-purple-100 text-purple-600 rounded-full flex items-center justify-center font-bold flex-shrink-0">
                    2
                  </div>
                  <div>
                    <div className="font-semibold text-gray-900">API Request</div>
                    <div className="text-sm text-gray-600">React sends data to FastAPI backend</div>
                  </div>
                </div>
                <div className="flex items-start gap-3">
                  <div className="w-8 h-8 bg-green-100 text-green-600 rounded-full flex items-center justify-center font-bold flex-shrink-0">
                    3
                  </div>
                  <div>
                    <div className="font-semibold text-gray-900">ML Prediction</div>
                    <div className="text-sm text-gray-600">Model analyzes features and calculates fraud probability</div>
                  </div>
                </div>
                <div className="flex items-start gap-3">
                  <div className="w-8 h-8 bg-orange-100 text-orange-600 rounded-full flex items-center justify-center font-bold flex-shrink-0">
                    4
                  </div>
                  <div>
                    <div className="font-semibold text-gray-900">Display Results</div>
                    <div className="text-sm text-gray-600">Real-time prediction with risk level and recommendation</div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="mt-16 bg-white border-t border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="text-center text-sm text-gray-600">
            <p className="mb-2">
              <strong>AI-Based Detection of Fake Orders and User Abuse in E-Commerce Platforms</strong>
            </p>
            <p>
              Developed by <span className="font-semibold text-blue-600">Team Three Unknowns</span> | 
              Velagapudi Ramakrishna Siddhartha Engineering College (VRSEC) | 
              Mini Project 2026
            </p>
            <p className="mt-2 text-xs text-gray-500">
              This is a demonstration prototype for academic evaluation purposes.
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
