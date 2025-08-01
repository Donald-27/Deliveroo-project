import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "../services/api";
import Loader from "../components/common/Loader";
import Timeline from "../components/parcels/Timeline";
import LiveMap from "../components/map/LiveMap";
import { QRCode } from "qrcode.react";
import Button from "../components/common/Button";

const TrackParcel = () => {
  const { trackingId } = useParams();
  const [parcel, setParcel] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      try {
        const { data } = await axios.get(`/tracking/${trackingId}`);
        setParcel(data);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    }
    fetchData();
  }, [trackingId]);

  if (loading) return <Loader />;

  if (!parcel) return <p className="text-center text-red-500">Parcel not found</p>;

  return (
    <div className="max-w-4xl mx-auto p-6 space-y-6">
      <h2 className="text-2xl font-bold text-primary">Track Parcel #{parcel.id}</h2>

      <div className="bg-white shadow rounded p-4">
        <p><span className="font-semibold">Status:</span> {parcel.status}</p>
        <p><span className="font-semibold">Estimated Delivery:</span> {new Date(parcel.eta).toLocaleString()}</p>
      </div>

      <div className="bg-white shadow rounded p-4">
        <h3 className="font-semibold mb-2">Delivery Timeline</h3>
        <Timeline status={parcel.status} />
      </div>

      <div className="bg-white shadow rounded p-4">
        <h3 className="font-semibold mb-2">Courier Location</h3>
        <LiveMap courier={parcel.courier} />
      </div>

      <div className="bg-white shadow rounded p-4 flex flex-col md:flex-row items-center md:justify-between">
        <div className="mb-4 md:mb-0">
          <h3 className="font-semibold mb-2">Download Receipt</h3>
          <QRCode value={parcel.id} size={128} />
        </div>
        <Button onClick={() => window.print()}>Print Receipt</Button>
      </div>
    </div>
  );
};

export default TrackParcel;
