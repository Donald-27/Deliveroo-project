import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchPerformance } from "../redux/slices/adminSlice";
import { fetchParcels } from "../redux/slices/parcelSlice";
import Loader from "../components/common/Loader";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";
import ParcelCard from "../components/parcels/ParcelCard";

const AdminPanel = () => {
  const dispatch = useDispatch();
  const { performance, loading: perfLoading } = useSelector((state) => state.admin);
  const { parcels, loading: parcLoading } = useSelector((state) => state.parcel);

  useEffect(() => {
    dispatch(fetchPerformance());
    dispatch(fetchParcels());
  }, [dispatch]);

  if (perfLoading || parcLoading) return <Loader />;

  return (
    <div className="p-6 space-y-6">
      <h2 className="text-2xl font-bold text-primary">Admin Dashboard</h2>

      <div className="bg-white shadow rounded p-4">
        <h3 className="font-semibold mb-2">Courier Performance</h3>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={performance}>
            <XAxis dataKey="courierName" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="deliveriesCompleted" fill="#3B82F6" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      <div className="bg-white shadow rounded p-4">
        <h3 className="font-semibold mb-2">Active Parcels</h3>
        {parcels.map((p) => (
          <ParcelCard key={p.id} parcel={p} onTrack={() => {}} />
        ))}
      </div>
    </div>
  );
};

export default AdminPanel;
