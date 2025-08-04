import React, { useState } from 'react';
import './ScheduleDelivery.css';

function ScheduleDelivery() {
  const [pickupDate, setPickupDate] = useState('');
  const [pickupTime, setPickupTime] = useState('');
  const [deliveryDate, setDeliveryDate] = useState('');
  const [deliveryTime, setDeliveryTime] = useState('');
  const [address, setAddress] = useState('');
  const [notes, setNotes] = useState('');
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();

    const payload = {
      pickupDate,
      pickupTime,
      deliveryDate,
      deliveryTime,
      address,
      notes,
    };

    console.log('Scheduled Delivery:', payload);
    setSubmitted(true);
  };

  return (
    <div className="schedule-delivery-container">
      <div className="schedule-form-wrapper">
        <h1>Schedule a Delivery</h1>
        <p className="subtitle">Choose a pickup and drop-off time that works best for you.</p>

        <form onSubmit={handleSubmit} className="schedule-form">
          <div className="form-group">
            <label htmlFor="pickup-date">Pickup Date</label>
            <input
              type="date"
              id="pickup-date"
              value={pickupDate}
              onChange={(e) => setPickupDate(e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="pickup-time">Pickup Time</label>
            <input
              type="time"
              id="pickup-time"
              value={pickupTime}
              onChange={(e) => setPickupTime(e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="delivery-date">Delivery Date</label>
            <input
              type="date"
              id="delivery-date"
              value={deliveryDate}
              onChange={(e) => setDeliveryDate(e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="delivery-time">Delivery Time</label>
            <input
              type="time"
              id="delivery-time"
              value={deliveryTime}
              onChange={(e) => setDeliveryTime(e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="address">Delivery Address</label>
            <textarea
              id="address"
              rows="3"
              value={address}
              onChange={(e) => setAddress(e.target.value)}
              placeholder="Enter complete delivery address"
              required
            ></textarea>
          </div>

          <div className="form-group">
            <label htmlFor="notes">Special Instructions</label>
            <textarea
              id="notes"
              rows="3"
              value={notes}
              onChange={(e) => setNotes(e.target.value)}
              placeholder="e.g. Leave at reception, fragile item"
            ></textarea>
          </div>

          <button type="submit" className="schedule-button">
            Schedule Delivery
          </button>
        </form>

        {submitted && (
          <div className="confirmation-box">
            <h3>Your delivery has been scheduled!</h3>
            <p>We’ll pick up your parcel as per the time you selected.</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default ScheduleDelivery;
