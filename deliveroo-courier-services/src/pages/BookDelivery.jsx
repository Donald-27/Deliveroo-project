import React, { useState } from 'react';
import './BookDelivery.css';

const BookDelivery = () => {
  const [formData, setFormData] = useState({
    senderName: '',
    senderPhone: '',
    pickupAddress: '',
    receiverName: '',
    receiverPhone: '',
    deliveryAddress: '',
    parcelWeight: '',
    parcelDescription: '',
    deliveryType: 'standard',
  });

  const [status, setStatus] = useState('');
  const [error, setError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus('');
    setError('');

    try {
      const response = await fetch('http://localhost:5000/api/parcels/book', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });

      const result = await response.json();
      if (!response.ok) throw new Error(result.message || 'Failed to book delivery.');

      setStatus(`Success! Tracking ID: ${result.trackingId || result.parcelId || 'N/A'}`);

      setFormData({
        senderName: '',
        senderPhone: '',
        pickupAddress: '',
        receiverName: '',
        receiverPhone: '',
        deliveryAddress: '',
        parcelWeight: '',
        parcelDescription: '',
        deliveryType: 'standard',
      });
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="book-delivery-page">
      <div className="form-container">
        <h1 className="form-title">📦 Book a New Delivery</h1>
        <p className="form-subtitle">Fast. Secure. Reliable. Deliver anywhere in minutes.</p>

        <form onSubmit={handleSubmit} className="delivery-form">
          <div className="form-section">
            <h3>Sender Information</h3>
            <input type="text" name="senderName" placeholder="Sender Name" value={formData.senderName} onChange={handleChange} required />
            <input type="tel" name="senderPhone" placeholder="Sender Phone" value={formData.senderPhone} onChange={handleChange} required />
            <textarea name="pickupAddress" placeholder="Pickup Address" value={formData.pickupAddress} onChange={handleChange} required></textarea>
          </div>

          <div className="form-section">
            <h3>Receiver Information</h3>
            <input type="text" name="receiverName" placeholder="Receiver Name" value={formData.receiverName} onChange={handleChange} required />
            <input type="tel" name="receiverPhone" placeholder="Receiver Phone" value={formData.receiverPhone} onChange={handleChange} required />
            <textarea name="deliveryAddress" placeholder="Delivery Address" value={formData.deliveryAddress} onChange={handleChange} required></textarea>
          </div>

          <div className="form-section">
            <h3>Parcel Details</h3>
            <input type="text" name="parcelWeight" placeholder="Weight (e.g. 2kg)" value={formData.parcelWeight} onChange={handleChange} required />
            <input type="text" name="parcelDescription" placeholder="Item Description" value={formData.parcelDescription} onChange={handleChange} required />
            <select name="deliveryType" value={formData.deliveryType} onChange={handleChange}>
              <option value="standard">Standard</option>
              <option value="express">Express</option>
              <option value="eco">Eco Mode</option>
            </select>
          </div>

          <button type="submit" className="submit-button">Submit Booking</button>
        </form>

        {status && <div className="success-message">{status}</div>}
        {error && <div className="error-message">{error}</div>}
      </div>
    </div>
  );
};

export default BookDelivery;
