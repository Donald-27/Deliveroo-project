import React from "react";
import Button from "../components/common/Button";
import { FaUpload } from "react-icons/fa";

const BulkBooking = () => {
  return (
    <div className="min-h-screen bg-[#1a1f2e] text-white p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold mb-6">Bulk Booking</h1>
        <p className="text-gray-400 mb-4">Upload a spreadsheet with parcel data to book multiple deliveries at once.</p>

        <div className="p-6 border border-gray-700 rounded-lg bg-[#222939]">
          <input type="file" accept=".csv, .xlsx" className="mb-4 w-full p-2 bg-[#1e2333] border border-gray-600 rounded" />
          <Button label="Upload & Process" icon={<FaUpload />} className="w-full" />
        </div>
      </div>
    </div>
  );
};

export default BulkBooking;
