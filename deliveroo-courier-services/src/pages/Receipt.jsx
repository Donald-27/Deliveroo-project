import React, { useEffect, useState } from 'react';
import './Receipt.css';

const Receipt = () => {
  const [parcel, setParcel] = useState(null);

  useEffect(() => {
    
    setParcel({
      parcelId: 'DR-12345-KE',
      pickup: 'Nairobi',
      destination: 'Mombasa',
      weight: '2.4 kg',
      courier: 'Jane W.',
      deliveredAt: '2025-08-02 14:00',
    });
  }, []);

  const handlePrint = () => window.print();

  return (
    <div className="receipt-page">
      {parcel ? (
        <div className="receipt-card">
          <h1>Delivery Receipt</h1>
          <p><strong>Parcel ID:</strong> {parcel.parcelId}</p>
          <p><strong>From:</strong> {parcel.pickup}</p>
          <p><strong>To:</strong> {parcel.destination}</p>
          <p><strong>Weight:</strong> {parcel.weight}</p>
          <p><strong>Courier:</strong> {parcel.courier}</p>
          <p><strong>Delivered At:</strong> {parcel.deliveredAt}</p>
          <button onClick={handlePrint} className="print-btn">Print Receipt</button>
        </div>
      ) : (
        <p>Loading receipt...</p>
      )}
    </div>
  );
};

export default Receipt;
