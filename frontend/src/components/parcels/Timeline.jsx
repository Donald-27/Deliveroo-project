import React from 'react';
import { FaCheckCircle } from 'react-icons/fa';

const Timeline = ({ steps, current }) => {
  return (
    <ol className="relative border-l border-indigo-400 ml-3 mt-4">
      {steps.map((step, idx) => (
        <li key={idx} className="mb-6 ml-6">
          <span
            className={`absolute -left-3 flex items-center justify-center w-6 h-6 rounded-full ring-4 ${
              idx <= current
                ? 'bg-indigo-500 ring-indigo-300'
                : 'bg-gray-400 ring-gray-300'
            }`}
          >
            <FaCheckCircle className="text-white text-xs" />
          </span>
          <h4 className="font-semibold text-white">{step.title}</h4>
          <p className="text-sm text-gray-400">{step.description}</p>
        </li>
      ))}
    </ol>
  );
};

export default Timeline;
