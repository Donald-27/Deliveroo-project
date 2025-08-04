import React from 'react';
import './LiveMap.css';

const mockCouriers = [
  { id: 1, name: 'Courier A', coords: [1, 1] },
  { id: 2, name: 'Courier B', coords: [2, 3] },
  { id: 3, name: 'Courier C', coords: [4, 2] },
];

const LiveMap = () => {
  return (
    <div className="live-map-page">
      <div className="map-header">
        <h1>Live Courier Map</h1>
        <p>Track courier locations across the fleet in real time.</p>
      </div>
      <div className="map-container">
        <div className="map-grid">
          {mockCouriers.map((c) => (
            <div key={c.id} className="map-marker" style={{ top: `${c.coords[0] * 20}%`, left: `${c.coords[1] * 20}%` }}>
              <div className="marker-dot"></div>
              <span className="marker-label">{c.name}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default LiveMap;
