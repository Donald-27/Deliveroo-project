import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchParcels } from "../redux/slices/parcelSlice";
import ParcelCard from "../components/parcels/ParcelCard";
import Loader from "../components/common/Loader";
import { Link } from "react-router-dom";

const Dashboard = () => {
  const dispatch = useDispatch();
  const { parcels, loading } = useSelector((state) => state.parcel);

  useEffect(() => {
    dispatch(fetchParcels());
  }, [dispatch]);

  return (
    <div className="p-6 max-w-5xl mx-auto">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-3xl font-bold text-blue-700">My Dashboard</h2>
        <Link to="/create-delivery" className="text-sm text-blue-500 hover:underline">+ Create New Delivery</Link>
      </div>

      {loading ? (
        <Loader />
      ) : parcels.length > 0 ? (
        parcels.map((parcel) => (
          <ParcelCard key={parcel.trackingId} parcel={parcel} onTrack={() => {}} />
        ))
      ) : (
        <p className="text-gray-600 text-center">No parcels assigned yet.</p>
      )}
    </div>
  );
};

export default Dashboard;
