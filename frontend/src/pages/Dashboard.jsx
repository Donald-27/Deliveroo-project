import React from 'react';
import ParcelCard from '../components/parcels/ParcelCard';
import { useSelector } from 'react-redux';

const Dashboard = () => {
  const parcels = useSelector((state) => state.parcel.myParcels || []);

  return (
    <div className="p-6 text-white">
      <h2 className="text-2xl font-bold mb-4">My Deliveries</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6">
        {parcels.length > 0 ? (
          parcels.map((p) => <ParcelCard key={p.id} parcel={p} />)
        ) : (
          <p className="text-gray-400">No deliveries yet.</p>
        )}
      </div>
    </div>
  );
};

export default Dashboard;
