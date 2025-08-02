// frontend/src/pages/SmartAssign.jsx
import React from "react";
import { GiArtificialHive } from "react-icons/gi";

const SmartAssign = () => {
  return (
    <div className="min-h-screen bg-indigo-50 p-10">
      <div className="bg-white shadow-lg rounded-3xl p-10 max-w-4xl mx-auto text-center">
        <GiArtificialHive className="text-indigo-600 text-6xl mb-4 mx-auto" />
        <h1 className="text-4xl font-bold text-indigo-800 mb-4">Smart Parcel Assignment</h1>
        <p className="text-gray-600 mb-6">
          Our AI-driven algorithm intelligently assigns parcels based on location, courier availability,
          and current delivery load, ensuring maximum efficiency.
        </p>
        <button className="bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-3 rounded-full transition duration-300">
          Optimize Assignments
        </button>
      </div>
    </div>
  );
};

export default SmartAssign;
