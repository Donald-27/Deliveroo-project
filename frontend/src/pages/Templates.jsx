import React from "react";
import { FaPlus, FaClipboardList } from "react-icons/fa";
import Button from "../components/common/Button";

const Templates = () => {
  return (
    <div className="p-6 text-white min-h-screen bg-gradient-to-br from-[#191c29] to-[#1f2937]">
      <div className="max-w-5xl mx-auto">
        <h1 className="text-4xl font-bold mb-6">Delivery Templates</h1>
        <p className="mb-4 text-gray-300">Save time by using pre-defined delivery templates for common routes.</p>

        <div className="grid gap-4 grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
          {[1, 2, 3].map((template) => (
            <div
              key={template}
              className="rounded-xl p-5 bg-[#2b2f40] border border-gray-700 hover:border-purple-500 transition-all shadow-lg"
            >
              <div className="flex justify-between items-center mb-3">
                <h2 className="text-lg font-semibold">Template {template}</h2>
                <FaClipboardList className="text-purple-400 text-xl" />
              </div>
              <p className="text-sm text-gray-400">Nairobi → Mombasa</p>
              <p className="text-sm text-gray-400">Pickup: Mon, 10:00 AM</p>
              <Button label="Use Template" className="mt-4 w-full" />
            </div>
          ))}
        </div>

        <div className="mt-8">
          <Button label="Create New Template" icon={<FaPlus />} />
        </div>
      </div>
    </div>
  );
};

export default Templates;
