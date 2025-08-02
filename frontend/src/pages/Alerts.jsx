// frontend/src/pages/Alerts.jsx
import React from "react";
import { IoMdAlert } from "react-icons/io";

const alerts = [
  { id: 1, message: "Severe weather warning in Nairobi!", type: "weather" },
  { id: 2, message: "Courier #123 has reported a delay", type: "delay" },
];

const Alerts = () => {
  return (
    <div className="p-8 bg-yellow-50 min-h-screen">
      <h1 className="text-3xl font-bold text-yellow-700 mb-6">System Alerts</h1>
      <div className="space-y-4">
        {alerts.map((alert) => (
          <div key={alert.id} className="bg-white rounded-lg shadow-md p-4 flex items-center gap-4 border-l-4 border-yellow-500">
            <IoMdAlert className="text-yellow-600 text-3xl" />
            <p className="text-gray-800">{alert.message}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Alerts;
