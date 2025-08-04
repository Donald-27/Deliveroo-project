import React, { useState } from 'react';
import './TrackParcel.css';
import { QRCodeCanvas } from 'qrcode.react';

const TrackParcel = () => {
  const [trackingID, setTrackingID] = useState('');
  const [parcelDetails, setParcelDetails] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleTrack = async () => {
    setError('');
    setParcelDetails(null);
    setLoading(true);

    if (!trackingID || isNaN(trackingID)) {
      setError('Please enter a valid numeric tracking ID.');
      setLoading(false);
      return;
    }

    try {
      const response = await fetch(`http://localhost:5000/api/parcels/track/${trackingID}`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' },
      });

      if (!response.ok) {
        const errData = await response.json();
        throw new Error(errData.error || 'Failed to fetch parcel details.');
      }

      const data = await response.json();

      const timeline = [
        { status: 'Pending Confirmation', date: data.created_at || 'N/A', done: ['Confirmed', 'Picked Up', 'In Transit', 'Out for Delivery', 'Delivered'].includes(data.status) },
        { status: 'Confirmed', date: data.confirmed_at || 'N/A', done: ['Picked Up', 'In Transit', 'Out for Delivery', 'Delivered'].includes(data.status) },
        { status: 'Picked Up', date: data.picked_up_at || 'N/A', done: ['In Transit', 'Out for Delivery', 'Delivered'].includes(data.status) },
        { status: 'In Transit', date: data.in_transit_at || 'N/A', done: ['Out for Delivery', 'Delivered'].includes(data.status) },
        { status: 'Out for Delivery', date: data.out_for_delivery_at || 'N/A', done: ['Delivered'].includes(data.status) },
        { status: 'Delivered', date: data.delivered_at || 'N/A', done: data.status === 'Delivered' },
      ];

      setParcelDetails({
        tracking_id: trackingID,
        status: data.status || 'Unknown',
        origin: data.pickup_address || 'Unknown Origin',
        destination: data.delivery_address || 'Unknown Destination',
        courier: data.courier_id ? `Courier #${data.courier_id}` : 'Not assigned',
        estimatedDelivery: data.estimated_delivery || 'Not available',
        lastUpdated: new Date().toLocaleString(),
        timeline,
      });
    } catch (err) {
      setError(err.message);
    }
    setLoading(false);
  };

  return (
    <div className="track-parcel">
      <div className="track-header">
        <h1>Track Your Parcel</h1>
        <p>Enter your tracking ID to get real-time updates and QR code.</p>
      </div>

      <div className="tracking-form">
        <input
          type="text"
          placeholder="Enter Tracking ID..."
          value={trackingID}
          onChange={(e) => setTrackingID(e.target.value)}
        />
        <button onClick={handleTrack}>Track</button>
      </div>

      {loading && <div className="loading-bar">Loading parcel details...</div>}

      {error && <div className="error-msg">{error}</div>}

      {parcelDetails && (
        <div className="parcel-info-card">
          <h2>Status: <span>{parcelDetails.status}</span></h2>
          <p><strong>From:</strong> {parcelDetails.origin}</p>
          <p><strong>To:</strong> {parcelDetails.destination}</p>
          <p><strong>Courier:</strong> {parcelDetails.courier}</p>
          <p><strong>Estimated Delivery:</strong> {parcelDetails.estimatedDelivery}</p>
          <p><strong>Last Updated:</strong> {parcelDetails.lastUpdated}</p>

          <div className="timeline">
            <h3>Delivery Progress</h3>
            <ul>
              {parcelDetails.timeline.map(({ status, date, done }, idx) => (
                <li key={idx} className={done ? 'done' : 'pending'}>
                  <span className="status">{status}</span>
                  <span className="date">{date}</span>
                </li>
              ))}
            </ul>
          </div>

          <div className="qr-section">
            <p>Scan this QR to track again:</p>
            <QRCodeCanvas value={trackingID} size={120} />
          </div>
        </div>
      )}
    </div>
  );
};

export default TrackParcel;
