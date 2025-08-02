import React, { useState } from "react";
import Input from "../components/common/Input";
import Button from "../components/common/Button";
import { FaClock } from "react-icons/fa";

const ScheduleDelivery = () => {
  const [formData, setFormData] = useState({
    pickupTime: "",
    deliveryDate: "",
    notes: "",
  });

  return (
    <div className="min-h-screen bg-gradient-to-br from-[#1b1d2a] to-[#262d3f] text-white p-6">
      <div className="max-w-xl mx-auto">
        <h1 className="text-3xl font-bold mb-4">Schedule a Delivery</h1>
        <p className="mb-6 text-gray-400">Plan your delivery ahead of time with precision.</p>

        <form className="space-y-4">
          <Input
            label="Pickup Time"
            type="time"
            value={formData.pickupTime}
            onChange={(e) => setFormData({ ...formData, pickupTime: e.target.value })}
          />
          <Input
            label="Delivery Date"
            type="date"
            value={formData.deliveryDate}
            onChange={(e) => setFormData({ ...formData, deliveryDate: e.target.value })}
          />
          <Input
            label="Notes"
            type="textarea"
            value={formData.notes}
            onChange={(e) => setFormData({ ...formData, notes: e.target.value })}
          />

          <Button icon={<FaClock />} label="Schedule Delivery" className="w-full" />
        </form>
      </div>
    </div>
  );
};

export default ScheduleDelivery;
