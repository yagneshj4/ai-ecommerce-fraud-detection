function ResultCard({ result, loading, error }) {
  
  // Loading State
  if (loading) {
    return (
      <div className="bg-white rounded-xl shadow-lg p-8 h-full flex items-center justify-center">
        <div className="text-center">
          <div className="inline-block animate-spin rounded-full h-16 w-16 border-4 border-blue-200 border-t-blue-600 mb-4"></div>
          <h3 className="text-xl font-semibold text-gray-900 mb-2">Analyzing Transaction...</h3>
          <p className="text-gray-600">Running ML model inference</p>
        </div>
      </div>
    );
  }

  // Error State
  if (error) {
    return (
      <div className="bg-white rounded-xl shadow-lg p-8 border-2 border-red-200 animate-slideIn">
        <div className="text-center">
          <div className="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center mx-auto mb-4">
            <span className="text-4xl">⚠️</span>
          </div>
          <h3 className="text-xl font-bold text-red-700 mb-3">Prediction Failed</h3>
          <p className="text-gray-700 mb-4">{error}</p>
          <div className="bg-red-50 border border-red-200 rounded-lg p-4 text-sm text-left">
            <p className="font-semibold text-red-800 mb-2">Common Issues:</p>
            <ul className="list-disc list-inside text-red-700 space-y-1">
              <li>Backend server not running (start with: <code className="bg-red-100 px-1 rounded">python main.py</code>)</li>
              <li>Wrong port (backend should be on port 8000)</li>
              <li>Model files missing in backend/models/</li>
            </ul>
          </div>
        </div>
      </div>
    );
  }

  // Result State
  if (result) {
    const isFraud = result.prediction === 'Fraud';
    const bgColor = isFraud ? 'bg-gradient-danger' : 'bg-gradient-success';
    const textColor = isFraud ? 'text-red-700' : 'text-green-700';
    const borderColor = isFraud ? 'border-red-300' : 'border-green-300';
    const icon = isFraud ? '🚨' : '✅';

    return (
      <div className={`rounded-xl shadow-lg overflow-hidden animate-slideIn`}>
        {/* Header */}
        <div className={`${bgColor} p-6 text-white`}>
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-2xl font-bold flex items-center gap-3">
              <span className="text-4xl">{icon}</span>
              {result.prediction}
            </h3>
            <div className="text-right">
              <div className="text-sm opacity-90">Confidence</div>
              <div className="text-3xl font-bold">{result.confidence}%</div>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <span className="px-3 py-1 bg-white bg-opacity-20 rounded-full text-sm font-medium">
              Risk Level: {result.risk_level}
            </span>
          </div>
        </div>

        {/* Body */}
        <div className="bg-white p-6 space-y-6">
          {/* Probability Meter */}
          <div>
            <div className="flex justify-between text-sm font-medium text-gray-700 mb-2">
              <span>Fraud Probability</span>
              <span>{result.fraud_probability}%</span>
            </div>
            <div className="w-full bg-gray-200 rounded-full h-4 overflow-hidden">
              <div
                className={`h-full ${isFraud ? 'bg-red-500' : 'bg-green-500'} transition-all duration-1000 ease-out`}
                style={{ width: `${result.fraud_probability}%` }}
              ></div>
            </div>
            <div className="flex justify-between text-xs text-gray-500 mt-1">
              <span>0% (Safe)</span>
              <span>100% (Fraudulent)</span>
            </div>
          </div>

          {/* Probabilities */}
          <div className="grid grid-cols-2 gap-4">
            <div className="bg-green-50 rounded-lg p-4 border-2 border-green-200">
              <div className="text-xs text-green-600 font-medium mb-1">Genuine</div>
              <div className="text-2xl font-bold text-green-700">{result.genuine_probability}%</div>
            </div>
            <div className="bg-red-50 rounded-lg p-4 border-2 border-red-200">
              <div className="text-xs text-red-600 font-medium mb-1">Fraud</div>
              <div className="text-2xl font-bold text-red-700">{result.fraud_probability}%</div>
            </div>
          </div>

          {/* Recommendation */}
          <div className={`border-2 ${borderColor} rounded-lg p-4`}>
            <h4 className={`font-bold ${textColor} mb-2 flex items-center gap-2`}>
              💡 Recommendation
            </h4>
            <p className="text-gray-700">{result.recommendation}</p>
          </div>

          {/* Risk Analysis */}
          <div className="bg-gray-50 rounded-lg p-4">
            <h4 className="font-bold text-gray-900 mb-3 flex items-center gap-2">
              📊 Risk Analysis
            </h4>
            <div className="space-y-2 text-sm">
              <div className="flex justify-between">
                <span className="text-gray-600">Risk Level:</span>
                <span className={`font-semibold ${
                  result.risk_level === 'VERY LOW' ? 'text-green-600' :
                  result.risk_level === 'LOW' ? 'text-blue-600' :
                  result.risk_level === 'MEDIUM' ? 'text-yellow-600' :
                  result.risk_level === 'HIGH' ? 'text-orange-600' :
                  'text-red-600'
                }`}>
                  {result.risk_level}
                </span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">Model Confidence:</span>
                <span className="font-semibold text-gray-900">{result.confidence}%</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">Classification:</span>
                <span className={`font-semibold ${textColor}`}>{result.prediction}</span>
              </div>
            </div>
          </div>

          {/* Action Button */}
          <div className="pt-4">
            {isFraud ? (
              <button className="w-full bg-red-600 hover:bg-red-700 text-white font-bold py-3 rounded-lg transition-colors">
                🚫 Block Transaction
              </button>
            ) : (
              <button className="w-full bg-green-600 hover:bg-green-700 text-white font-bold py-3 rounded-lg transition-colors">
                ✓ Approve Transaction
              </button>
            )}
          </div>
        </div>
      </div>
    );
  }

  // Default State (No prediction yet)
  return (
    <div className="bg-white rounded-xl shadow-lg p-8 h-full flex items-center justify-center border-2 border-dashed border-gray-300">
      <div className="text-center">
        <div className="w-20 h-20 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-4">
          <span className="text-5xl">🔍</span>
        </div>
        <h3 className="text-xl font-semibold text-gray-900 mb-2">Awaiting Prediction</h3>
        <p className="text-gray-600 max-w-sm">
          Enter transaction details and click "Analyze Transaction" to get real-time fraud detection results.
        </p>
        <div className="mt-6 flex items-center justify-center gap-2 text-sm text-gray-500">
          <span className="w-2 h-2 bg-blue-500 rounded-full animate-pulse"></span>
          Ready to analyze
        </div>
      </div>
    </div>
  );
}

export default ResultCard;
