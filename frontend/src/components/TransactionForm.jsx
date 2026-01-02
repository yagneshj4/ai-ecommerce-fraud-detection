import { useState } from 'react';

const PRESETS = {
  genuine: {
    Amount: 25.50,
    Time: 1000,
    V1: -0.5,
    V2: 0.3,
    V3: -0.2,
  },
  suspicious: {
    Amount: 2500,
    Time: 5000,
    V1: 2.5,
    V2: -1.8,
    V3: 1.3,
  },
  medium: {
    Amount: 150,
    Time: 3000,
    V1: 0.5,
    V2: -0.5,
    V3: 0.2,
  }
};

function TransactionForm({ onSubmit, loading, onReset }) {
  const [formData, setFormData] = useState({
    Amount: '',
    Time: '',
  });

  const [showAdvanced, setShowAdvanced] = useState(false);
  const [advancedFeatures, setAdvancedFeatures] = useState({});

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleAdvancedChange = (e) => {
    const { name, value } = e.target;
    setAdvancedFeatures(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const loadPreset = (presetType) => {
    const preset = PRESETS[presetType];
    setFormData({
      Amount: preset.Amount,
      Time: preset.Time,
    });
    setAdvancedFeatures({
      V1: preset.V1,
      V2: preset.V2,
      V3: preset.V3,
    });
    if (onReset) onReset();
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Prepare data for API
    const transactionData = {
      Amount: parseFloat(formData.Amount) || 0,
      Time: parseFloat(formData.Time) || 0,
    };

    // Add V1-V28 (default to 0 if not provided)
    for (let i = 1; i <= 28; i++) {
      const key = `V${i}`;
      transactionData[key] = parseFloat(advancedFeatures[key]) || 0;
    }

    onSubmit(transactionData);
  };

  const handleClear = () => {
    setFormData({ Amount: '', Time: '' });
    setAdvancedFeatures({});
    if (onReset) onReset();
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      {/* Preset Buttons */}
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-3">
          Quick Presets
        </label>
        <div className="grid grid-cols-3 gap-3">
          <button
            type="button"
            onClick={() => loadPreset('genuine')}
            className="px-4 py-2 bg-green-50 hover:bg-green-100 text-green-700 rounded-lg border border-green-200 transition-colors text-sm font-medium"
          >
            ✓ Genuine
          </button>
          <button
            type="button"
            onClick={() => loadPreset('suspicious')}
            className="px-4 py-2 bg-red-50 hover:bg-red-100 text-red-700 rounded-lg border border-red-200 transition-colors text-sm font-medium"
          >
            ⚠️ Suspicious
          </button>
          <button
            type="button"
            onClick={() => loadPreset('medium')}
            className="px-4 py-2 bg-yellow-50 hover:bg-yellow-100 text-yellow-700 rounded-lg border border-yellow-200 transition-colors text-sm font-medium"
          >
            → Medium
          </button>
        </div>
      </div>

      {/* Basic Fields */}
      <div className="space-y-4">
        <div>
          <label htmlFor="Amount" className="block text-sm font-medium text-gray-700 mb-2">
            💰 Transaction Amount ($)
          </label>
          <input
            type="number"
            id="Amount"
            name="Amount"
            value={formData.Amount}
            onChange={handleInputChange}
            step="0.01"
            min="0"
            required
            className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
            placeholder="Enter amount (e.g., 25.50)"
          />
        </div>

        <div>
          <label htmlFor="Time" className="block text-sm font-medium text-gray-700 mb-2">
            ⏱️ Time (seconds since account creation)
          </label>
          <input
            type="number"
            id="Time"
            name="Time"
            value={formData.Time}
            onChange={handleInputChange}
            step="1"
            min="0"
            required
            className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
            placeholder="Enter time in seconds (e.g., 1000)"
          />
        </div>
      </div>

      {/* Advanced Features Toggle */}
      <div>
        <button
          type="button"
          onClick={() => setShowAdvanced(!showAdvanced)}
          className="flex items-center gap-2 text-sm text-blue-600 hover:text-blue-700 font-medium"
        >
          <span className={`transform transition-transform ${showAdvanced ? 'rotate-90' : ''}`}>
            ▶
          </span>
          Advanced Features (V1-V28 PCA Components)
        </button>

        {showAdvanced && (
          <div className="mt-4 p-4 bg-gray-50 rounded-lg border border-gray-200">
            <div className="grid grid-cols-2 md:grid-cols-4 gap-3 max-h-64 overflow-y-auto">
              {Array.from({ length: 28 }, (_, i) => {
                const key = `V${i + 1}`;
                return (
                  <div key={key}>
                    <label htmlFor={key} className="block text-xs font-medium text-gray-600 mb-1">
                      {key}
                    </label>
                    <input
                      type="number"
                      id={key}
                      name={key}
                      value={advancedFeatures[key] || ''}
                      onChange={handleAdvancedChange}
                      step="0.1"
                      className="w-full px-2 py-1 text-sm border border-gray-300 rounded focus:ring-1 focus:ring-blue-500 focus:border-transparent"
                      placeholder="0.0"
                    />
                  </div>
                );
              })}
            </div>
            <p className="mt-3 text-xs text-gray-500">
              ℹ️ These are PCA-transformed features. Leave empty to default to 0.
            </p>
          </div>
        )}
      </div>

      {/* Action Buttons */}
      <div className="flex gap-3">
        <button
          type="submit"
          disabled={loading}
          className={`flex-1 py-3 px-6 rounded-lg font-semibold text-white transition-all ${
            loading
              ? 'bg-gray-400 cursor-not-allowed'
              : 'bg-blue-600 hover:bg-blue-700 active:scale-95'
          }`}
        >
          {loading ? (
            <span className="flex items-center justify-center gap-2">
              <svg className="animate-spin h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Analyzing...
            </span>
          ) : (
            '🔍 Analyze Transaction'
          )}
        </button>

        <button
          type="button"
          onClick={handleClear}
          disabled={loading}
          className="px-6 py-3 bg-gray-200 hover:bg-gray-300 text-gray-700 rounded-lg font-semibold transition-all active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          Clear
        </button>
      </div>

      {/* Info Note */}
      <div className="text-xs text-gray-500 bg-blue-50 p-3 rounded-lg border border-blue-100">
        <strong>💡 Tip:</strong> Use preset buttons for quick testing, or manually enter transaction details.
        Advanced features (V1-V28) are optional PCA components from the ML model.
      </div>
    </form>
  );
}

export default TransactionForm;
