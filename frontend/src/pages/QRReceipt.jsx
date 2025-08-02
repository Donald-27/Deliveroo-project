import React from "react";
import QRCode from "react-qr-code";

const QRReceipt = () => {
  const data = "https://deliveroo.app/track/parcel/1234567890";

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-[#0f172a] text-white">
      <h1 className="text-4xl font-bold mb-6">QR Code Receipt</h1>
      <p className="text-gray-300 mb-4">Scan this QR code to track your parcel.</p>
      <div className="bg-white p-4 rounded-lg shadow-lg">
        <QRCode value={data} size={256} />
      </div>
      <p className="text-sm mt-4 text-purple-400">Scan to track your delivery</p>
    </div>
  );
};

export default QRReceipt;
