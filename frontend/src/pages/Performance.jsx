// frontend/src/pages/Performance.jsx
import React from "react";

const Performance = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-white p-10">
      <h1 className="text-4xl font-bold text-blue-900 mb-8 text-center">Courier Performance</h1>
      <div className="bg-white rounded-xl shadow-xl p-8 max-w-4xl mx-auto">
        <div className="flex justify-between mb-6">
          <div>
            <p className="text-gray-600">On-time Deliveries</p>
            <h2 className="text-2xl text-green-600 font-bold">92%</h2>
          </div>
          <div>
            <p className="text-gray-600">Customer Rating</p>
            <h2 className="text-2xl text-yellow-500 font-bold">4.7 ★</h2>
          </div>
          <div>
            <p className="text-gray-600">Deliveries Completed</p>
            <h2 className="text-2xl text-purple-700 font-bold">1,230</h2>
          </div>
        </div>
        <p className="text-sm text-gray-500 mt-4">
          Performance is calculated based on the last 30 days of courier activity.
        </p>
      </div>
    </div>
  );
};

export default Performance;
