/**
 * API Service for communicating with FastAPI backend
 * Handles all HTTP requests to the fraud detection API
 */

import axios from 'axios';

// Base URL for API - uses proxy in development, direct URL in production
const API_BASE_URL = import.meta.env.PROD 
  ? 'http://localhost:8000' 
  : '/api';

// Create axios instance with default config
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000, // 10 seconds timeout
});

/**
 * Check if API is running
 * @returns {Promise} API health status
 */
export const checkHealth = async () => {
  try {
    const response = await api.get('/');
    return response.data;
  } catch (error) {
    console.error('Health check failed:', error);
    throw error;
  }
};

/**
 * Predict fraud for a transaction
 * @param {Object} transactionData - Transaction details
 * @returns {Promise} Prediction result
 */
export const predictFraud = async (transactionData) => {
  try {
    const response = await api.post('/predict', transactionData);
    return response.data;
  } catch (error) {
    console.error('Prediction failed:', error);
    
    // Handle different error types
    if (error.response) {
      // Server responded with error
      throw new Error(error.response.data.detail || 'Prediction failed');
    } else if (error.request) {
      // Request made but no response
      throw new Error('Cannot connect to API. Please ensure backend is running on port 8000.');
    } else {
      // Something else happened
      throw new Error('An unexpected error occurred');
    }
  }
};

export default api;
