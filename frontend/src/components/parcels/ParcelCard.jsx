import React from 'react';
import { FaMapMarkerAlt, FaBox, FaClock } from 'react-icons/fa';

const ParcelCard = ({ parcel }) => {
  return (
    <div className="bg-gradient-to-br from-black/60 via-indigo-900/30 to-black/50 rounded-xl p-5 text-white shadow-lg hover:shadow-indigo-500/30 transition-all duration-300">
      <div className="flex justify-between items-center mb-2">
        <h3 className="text-lg font-bold">#{parcel.trackingId}</h3>
        <span className="text-sm text-green-400 font-semibold">
          {parcel.status}
        </span>
      </div>
      <p className="flex items-center gap-2 text-sm text-gray-300">
        <FaMapMarkerAlt /> From: {parcel.origin}
      </p>
      <p className="flex items-center gap-2 text-sm text-gray-300">
        <FaMapMarkerAlt /> To: {parcel.destination}
      </p>
      <p className="flex items-center gap-2 text-sm text-gray-300 mt-2">
        <FaClock /> Scheduled: {parcel.scheduleTime}
      </p>
      <div className="mt-3 text-right">
        <button className="text-indigo-400 hover:underline">Track</button>
      </div>
    </div>
  );
};

export default ParcelCard;
