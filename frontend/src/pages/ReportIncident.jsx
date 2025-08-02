// frontend/src/pages/ReportIncident.jsx
import React, { useState } from "react";

const ReportIncident = () => {
  const [report, setReport] = useState("");

  return (
    <div className="min-h-screen bg-red-50 p-10 flex justify-center items-center">
      <div className="bg-white shadow-xl rounded-2xl p-8 w-full max-w-lg border border-red-200">
        <h1 className="text-3xl font-bold text-red-600 mb-4">Report Incident</h1>
        <textarea
          rows="6"
          className="w-full border border-red-300 rounded-lg p-4 text-gray-700 focus:outline-none focus:ring-2 focus:ring-red-500"
          placeholder="Describe the issue here..."
          value={report}
          onChange={(e) => setReport(e.target.value)}
        />
        <button className="mt-4 bg-red-600 hover:bg-red-700 text-white py-2 px-6 rounded-lg">
          Submit Report
        </button>
      </div>
    </div>
  );
};

export default ReportIncident;
