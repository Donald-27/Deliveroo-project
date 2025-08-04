import React, { useState } from 'react';
import './QuoteCalculator.css';

const QuoteCalculator = () => {
  const [weight, setWeight] = useState('');
  const [distance, setDistance] = useState('');
  const [speed, setSpeed] = useState('normal');
  const [quote, setQuote] = useState(null);

  const calculateQuote = () => {
    const baseRate = 10;
    const weightFactor = parseFloat(weight) * 0.5;
    const distanceFactor = parseFloat(distance) * 1.2;
    const speedMultiplier = speed === 'express' ? 1.75 : 1.0;

    const total = (baseRate + weightFactor + distanceFactor) * speedMultiplier;
    setQuote(total.toFixed(2));
  };

  return (
    <div className="quote-container">
      <h2>Instant Quote Calculator</h2>
      <p>Get a real-time estimate for your delivery below.</p>

      <div className="quote-form">
        <div className="input-group">
          <label>Parcel Weight (kg)</label>
          <input
            type="number"
            placeholder="e.g. 2.5"
            value={weight}
            onChange={(e) => setWeight(e.target.value)}
          />
        </div>

        <div className="input-group">
          <label>Distance (km)</label>
          <input
            type="number"
            placeholder="e.g. 30"
            value={distance}
            onChange={(e) => setDistance(e.target.value)}
          />
        </div>

        <div className="input-group">
          <label>Delivery Speed</label>
          <select value={speed} onChange={(e) => setSpeed(e.target.value)}>
            <option value="normal">Normal</option>
            <option value="express">Express</option>
          </select>
        </div>

        <button className="calculate-btn" onClick={calculateQuote}>
          Calculate Quote
        </button>

        {quote && (
          <div className="quote-result">
            <h3>Your Estimated Cost:</h3>
            <div className="quote-price">Ksh {quote}</div>
          </div>
        )}
      </div>
    </div>
  );
};

export default QuoteCalculator;
