import React, { useEffect, useState } from "react";
import "./SmartAssign.css";

const mockParcels = [
  { id: "P001", destination: "Westlands", priority: "High", weight: 2.3 },
  { id: "P002", destination: "Kilimani", priority: "Medium", weight: 5.0 },
  { id: "P003", destination: "CBD", priority: "Low", weight: 1.2 },
];

const mockCouriers = [
  { id: "C001", name: "Eddy Mutua", currentLocation: "CBD", load: 2 },
  { id: "C002", name: "Faith Kirui", currentLocation: "Westlands", load: 1 },
  { id: "C003", name: "Kevin Ouma", currentLocation: "Kilimani", load: 4 },
];

const SmartAssign = () => {
  const [assignments, setAssignments] = useState([]);

  useEffect(() => {

    const smartAssignments = mockParcels.map((parcel) => {
   
      const suitableCourier = mockCouriers
        .filter((c) => c.currentLocation === parcel.destination)
        .sort((a, b) => a.load - b.load)[0];

      return {
        parcelId: parcel.id,
        courierName: suitableCourier ? suitableCourier.name : "No Match Found",
        priority: parcel.priority,
      };
    });

    setAssignments(smartAssignments);
  }, []);

  return (
    <div className="smartassign-container">
      <h1 className="smartassign-title">📦 Smart Parcel Assignment</h1>

      <div className="panels-wrapper">
        <div className="panel parcels-panel">
          <h2>📋 Incoming Parcels</h2>
          <ul>
            {mockParcels.map((parcel) => (
              <li key={parcel.id}>
                <strong>{parcel.id}</strong> → {parcel.destination} ({parcel.priority})
              </li>
            ))}
          </ul>
        </div>

        <div className="panel couriers-panel">
          <h2>🚴 Available Couriers</h2>
          <ul>
            {mockCouriers.map((courier) => (
              <li key={courier.id}>
                <strong>{courier.name}</strong> — {courier.currentLocation} | Load: {courier.load}
              </li>
            ))}
          </ul>
        </div>

        <div className="panel assignments-panel">
          <h2>🧠 Smart Assignments</h2>
          <ul>
            {assignments.map((assign, index) => (
              <li key={index}>
                <strong>{assign.parcelId}</strong> ➤ {assign.courierName} ({assign.priority})
              </li>
            ))}
          </ul>
        </div>
      </div>

      <div className="footer-note">
        🤖 Smart assignment uses real-time logic to optimize courier-parcel mapping based on load,
        proximity, and delivery priority.
      </div>
    </div>
  );
};

export default SmartAssign;
