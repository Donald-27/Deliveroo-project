import React from "react";
import Timeline from "./Timeline";
import Button from "../common/Button";

const ParcelCard = ({ parcel, onTrack, showTimeline = false }) => {
  return (
    <div className="bg-white p-6 shadow-md rounded-md mb-4 border border-gray-200">
      <h3 className="text-xl font-semibold text-gray-800 mb-2">Parcel ID: {parcel.trackingId}</h3>
      <p className="text-gray-600">Sender: {parcel.senderName}</p>
      <p className="text-gray-600">Receiver: {parcel.receiverName}</p>
      <p className="text-gray-600">Status: <span className="font-medium text-blue-700">{parcel.status}</span></p>
      {showTimeline && <Timeline status={parcel.status} />}
      <div className="mt-4">
        <Button onClick={() => onTrack(parcel.trackingId)}>Track</Button>
      </div>
    </div>
  );
};

export default ParcelCard;
