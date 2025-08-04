import React, { useEffect, useState } from 'react';
import './Alerts.css';

const mockAlerts = [
  { id: 1, type: 'Delay', message: 'Heavy traffic near Mombasa.', time: '14:35' },
  { id: 2, type: 'Weather', message: 'Rain expected tomorrow in Nairobi.', time: '09:00' },
];

const Alerts = () => {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {

    setAlerts(mockAlerts);
  }, []);

  return (
    <div className="alerts-page">
      <h1>Alerts & Notifications</h1>
      <div className="alerts-list">
        {alerts.map((a) => (
          <div className={`alert-card ${a.type.toLowerCase()}`} key={a.id}>
            <div className="alert-header">
              <span className="alert-type">{a.type}</span>
              <span className="alert-time">{a.time}</span>
            </div>
            <p>{a.message}</p>
          </div>
        ))}
        {alerts.length === 0 && <p>No alerts at the moment.</p>}
      </div>
    </div>
  );
};

export default Alerts;
