// frontend/src/pages/LiveCourier.jsx
import React from "react";
import LiveMap from "../components/map/LiveMap";

const LiveCourier = () => {
  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <h2 className="text-3xl font-bold mb-4 text-center text-purple-800">
        Live Courier Tracking
      </h2>
      <div className="border-4 border-purple-200 rounded-xl shadow-xl overflow-hidden">
        <LiveMap />
      </div>
    </div>
  );
};

export default LiveCourier;
