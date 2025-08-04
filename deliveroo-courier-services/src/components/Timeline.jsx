import React from "react";

const timelineEvents = [
  {
    title: "Parcel Booked",
    description: "The parcel was successfully booked and entered into our system.",
    time: "2025-08-03 10:30 AM",
  },
  {
    title: "Picked Up",
    description: "Our rider picked up the parcel from the sender’s location.",
    time: "2025-08-03 12:00 PM",
  },
  {
    title: "In Transit",
    description: "Parcel is on its way to the destination.",
    time: "2025-08-03 03:15 PM",
  },
  {
    title: "Delivered",
    description: "The parcel was delivered successfully to the recipient.",
    time: "2025-08-03 05:45 PM",
  },
];

const Timeline = () => {
  return (
    <div className="w-full max-w-3xl mx-auto px-4 py-8">
      <h2 className="text-3xl font-bold text-center text-gray-800 dark:text-white mb-10">
        Parcel Delivery Timeline
      </h2>
      <div className="relative border-l-4 border-blue-600 dark:border-blue-400">
        {timelineEvents.map((event, index) => (
          <div key={index} className="mb-10 ml-6">
            <div className="absolute w-4 h-4 bg-blue-600 dark:bg-blue-400 rounded-full -left-2.5 border-4 border-white dark:border-gray-800"></div>
            <h3 className="text-xl font-semibold text-gray-900 dark:text-white">
              {event.title}
            </h3>
            <time className="block text-sm text-gray-500 dark:text-gray-400 mb-2">
              {event.time}
            </time>
            <p className="text-base text-gray-700 dark:text-gray-300">{event.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Timeline;
