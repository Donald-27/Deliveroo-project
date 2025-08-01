import React from "react";

const steps = ["Dispatched", "In Transit", "Out for Delivery", "Delivered"];

const Timeline = ({ status }) => {
  const currentStep = steps.indexOf(status);

  return (
    <div className="flex justify-between items-center mt-4">
      {steps.map((step, index) => (
        <div key={step} className="flex-1 text-center">
          <div
            className={`w-8 h-8 mx-auto rounded-full border-2 ${
              index <= currentStep ? "bg-blue-600 border-blue-600 text-white" : "border-gray-300"
            } flex items-center justify-center text-sm font-bold`}
          >
            {index + 1}
          </div>
          <p className="text-xs mt-1">{step}</p>
        </div>
      ))}
    </div>
  );
};

export default Timeline;
