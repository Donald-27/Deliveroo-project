import React, { useState } from 'react';
import QRCode from 'qrcode.react';
import './QRGenerator.css';

const QRGenerator = () => {
  const [trackingID, setTrackingID] = useState('');
  const [showQR, setShowQR] = useState(false);

  const handleGenerate = () => {
    if (trackingID.trim() !== '') {
      setShowQR(true);
    }
  };

  return (
    <div className="qrgen-container">
      <div className="qrgen-box">
        <h2 className="qrgen-title">Generate QR Code</h2>
        <p className="qrgen-subtext">Enter a tracking ID or custom code to generate a shareable QR</p>

        <input
          className="qrgen-input"
          type="text"
          placeholder="e.g., DR-1247-KG78"
          value={trackingID}
          onChange={(e) => {
            setTrackingID(e.target.value);
            setShowQR(false);
          }}
        />

        <button className="qrgen-button" onClick={handleGenerate}>
          Generate
        </button>

        {showQR && (
          <div className="qrgen-output">
            <QRCode value={trackingID} size={200} bgColor="#ffffff" fgColor="#222831" />
            <p className="qrgen-code">Code: <strong>{trackingID}</strong></p>
          </div>
        )}
      </div>
    </div>
  );
};

export default QRGenerator;
