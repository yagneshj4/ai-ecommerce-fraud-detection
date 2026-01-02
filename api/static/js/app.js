/**
 * AI Fraud Detection System - Frontend JavaScript
 * Team: Three Unknowns | VRSEC
 * 
 * This script handles:
 * - Form submission and validation
 * - API communication
 * - Dynamic UI updates
 * - Preset transaction loading
 */

// ========== Constants ==========
const API_URL = '/predict';
const FEATURE_NAMES = [
    'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
    'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
    'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28'
];

// Preset transactions for demo
const PRESETS = {
    genuine: {
        Time: 1000,
        Amount: 25.50,
        V1: 0.1, V2: -0.2, V3: 0, V4: 0, V5: 0, V6: 0, V7: 0, V8: 0, V9: 0, V10: 0,
        V11: 0, V12: 0, V13: 0, V14: 0, V15: 0, V16: 0, V17: 0, V18: 0, V19: 0, V20: 0,
        V21: 0, V22: 0, V23: 0, V24: 0, V25: 0, V26: 0, V27: 0, V28: 0
    },
    suspicious: {
        Time: 5000,
        Amount: 2500.00,
        V1: 2.5, V2: 3.1, V3: 0, V4: 0, V5: 0, V6: 0, V7: 0, V8: 0, V9: 0, V10: 0,
        V11: 0, V12: 0, V13: 0, V14: 0, V15: 0, V16: 0, V17: 0, V18: 0, V19: 0, V20: 0,
        V21: 0, V22: 0, V23: 0, V24: 0, V25: 0, V26: 0, V27: 0, V28: 0
    },
    medium: {
        Time: 3000,
        Amount: 150.00,
        V1: -0.5, V2: 0.3, V3: 0, V4: 0, V5: 0, V6: 0, V7: 0, V8: 0, V9: 0, V10: 0,
        V11: 0, V12: 0, V13: 0, V14: 0, V15: 0, V16: 0, V17: 0, V18: 0, V19: 0, V20: 0,
        V21: 0, V22: 0, V23: 0, V24: 0, V25: 0, V26: 0, V27: 0, V28: 0
    }
};

// ========== Initialize on Page Load ==========
document.addEventListener('DOMContentLoaded', function() {
    initializeAdvancedFields();
    setupFormSubmission();
    console.log('✅ Fraud Detection System initialized');
});

// ========== Generate Advanced Feature Fields ==========
function initializeAdvancedFields() {
    const container = document.querySelector('.features-grid');
    
    FEATURE_NAMES.forEach(featureName => {
        const div = document.createElement('div');
        div.className = 'feature-input';
        div.innerHTML = `
            <label for="${featureName}">${featureName}</label>
            <input 
                type="number" 
                id="${featureName}" 
                name="${featureName}" 
                value="0" 
                step="0.01"
            >
        `;
        container.appendChild(div);
    });
}

// ========== Toggle Advanced Fields ==========
function toggleAdvanced() {
    const advancedFields = document.getElementById('advancedFields');
    const toggleBtn = document.getElementById('toggleBtn');
    
    advancedFields.classList.toggle('show');
    toggleBtn.classList.toggle('active');
}

// ========== Load Preset Transaction ==========
function loadPreset(presetName) {
    const preset = PRESETS[presetName];
    if (!preset) return;
    
    // Load values into form
    document.getElementById('amount').value = preset.Amount;
    document.getElementById('time').value = preset.Time;
    
    // Load V features
    FEATURE_NAMES.forEach(featureName => {
        const input = document.getElementById(featureName);
        if (input) {
            input.value = preset[featureName];
        }
    });
    
    // Visual feedback
    const btn = event.target;
    const originalText = btn.textContent;
    btn.textContent = '✓ Loaded!';
    setTimeout(() => {
        btn.textContent = originalText;
    }, 1000);
}

// ========== Form Submission ==========
function setupFormSubmission() {
    const form = document.getElementById('fraudForm');
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Collect form data
        const formData = collectFormData();
        
        // Validate
        if (!validateFormData(formData)) {
            showError('Please fill in all required fields');
            return;
        }
        
        // Show loading state
        showLoadingState();
        
        try {
            // Send to API
            const result = await predictFraud(formData);
            
            // Display results
            displayResults(result, formData);
            
        } catch (error) {
            showError(error.message || 'Failed to analyze transaction. Please try again.');
        }
    });
}

// ========== Collect Form Data ==========
function collectFormData() {
    const data = {
        Time: parseFloat(document.getElementById('time').value),
        Amount: parseFloat(document.getElementById('amount').value)
    };
    
    // Add all V features
    FEATURE_NAMES.forEach(featureName => {
        const input = document.getElementById(featureName);
        data[featureName] = parseFloat(input.value) || 0;
    });
    
    return data;
}

// ========== Validate Form Data ==========
function validateFormData(data) {
    if (!data.Time || data.Time < 0) return false;
    if (!data.Amount || data.Amount < 0) return false;
    return true;
}

// ========== API Call: Predict Fraud ==========
async function predictFraud(transactionData) {
    const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(transactionData)
    });
    
    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.error || 'Prediction failed');
    }
    
    return await response.json();
}

// ========== Display Results ==========
function displayResults(result, transactionData) {
    // Hide other states
    hideAllStates();
    
    // Show results card
    const resultsCard = document.getElementById('resultsCard');
    resultsCard.style.display = 'block';
    
    // Update prediction badge
    const predictionBadge = document.getElementById('predictionBadge');
    const predictionText = document.getElementById('predictionText');
    const confidenceText = document.getElementById('confidenceText');
    const resultIcon = document.getElementById('resultIcon');
    
    const isFraud = result.prediction === 'FRAUD';
    predictionBadge.className = isFraud ? 'prediction-badge fraud' : 'prediction-badge genuine';
    predictionText.textContent = result.prediction;
    confidenceText.textContent = `${result.confidence}% confidence`;
    
    // Update icon
    if (isFraud) {
        resultIcon.innerHTML = `
            <path d="M12 2L2 7v6.5C2 17.43 5.84 21.74 12 23c6.16-1.26 10-5.57 10-9.5V7l-10-5z" 
                  fill="currentColor"/>
            <path d="M9 12l2 2 4-4" stroke="white" stroke-width="2" stroke-linecap="round" 
                  stroke-linejoin="round" fill="none"/>
        `;
        resultIcon.innerHTML = `
            <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2" fill="none"/>
            <path d="M15 9l-6 6M9 9l6 6" stroke="currentColor" stroke-width="2" 
                  stroke-linecap="round"/>
        `;
    } else {
        resultIcon.innerHTML = `
            <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2" fill="none"/>
            <path d="M8 12l3 3 5-5" stroke="currentColor" stroke-width="2" 
                  stroke-linecap="round" stroke-linejoin="round"/>
        `;
    }
    
    // Update probability meter
    const probabilityValue = document.getElementById('probabilityValue');
    const probabilityFill = document.getElementById('probabilityFill');
    const probability = result.fraud_probability * 100;
    
    probabilityValue.textContent = `${probability.toFixed(1)}%`;
    probabilityFill.style.width = `${probability}%`;
    
    // Update risk level
    const riskLevel = document.getElementById('riskLevel');
    const riskText = result.risk_level || 'UNKNOWN';
    riskLevel.textContent = riskText;
    riskLevel.className = 'risk-badge ' + riskText.toLowerCase().replace(' ', '-');
    
    // Update recommendation
    const recommendationText = document.getElementById('recommendationText');
    recommendationText.textContent = result.recommendation || 'Please review transaction manually.';
    
    // Update transaction details
    document.getElementById('displayAmount').textContent = `$${transactionData.Amount.toFixed(2)}`;
    document.getElementById('displayTime').textContent = `${transactionData.Time} seconds`;
    
    // Scroll to results (on mobile)
    if (window.innerWidth < 968) {
        resultsCard.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
}

// ========== Show Loading State ==========
function showLoadingState() {
    hideAllStates();
    document.getElementById('loadingState').style.display = 'block';
}

// ========== Show Error ==========
function showError(message) {
    hideAllStates();
    const errorState = document.getElementById('errorState');
    const errorMessage = document.getElementById('errorMessage');
    
    errorMessage.textContent = message;
    errorState.style.display = 'block';
}

// ========== Hide All States ==========
function hideAllStates() {
    document.getElementById('placeholderState').style.display = 'none';
    document.getElementById('resultsCard').style.display = 'none';
    document.getElementById('loadingState').style.display = 'none';
    document.getElementById('errorState').style.display = 'none';
}

// ========== Clear Results ==========
function clearResults() {
    hideAllStates();
    document.getElementById('placeholderState').style.display = 'block';
}

// ========== Utility: Format Currency ==========
function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(amount);
}

// ========== Utility: Format Time ==========
function formatTime(seconds) {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    
    if (hours > 0) {
        return `${hours}h ${minutes}m ${secs}s`;
    } else if (minutes > 0) {
        return `${minutes}m ${secs}s`;
    } else {
        return `${secs}s`;
    }
}

// ========== Console Welcome Message ==========
console.log(`
%c🛡️ AI Fraud Detection System
%cTeam: Three Unknowns | VRSEC
%cModel: Logistic Regression | Accuracy: 92%
`,
'color: #2563eb; font-size: 20px; font-weight: bold;',
'color: #6b7280; font-size: 12px;',
'color: #10b981; font-size: 12px;'
);
