import React from 'react';

const Loader = ({ size = 24 }) => {
  return (
    <div className="flex justify-center items-center py-4">
      <div
        style={{ width: size, height: size }}
        className="border-4 border-t-indigo-500 border-gray-300 rounded-full animate-spin"
      ></div>
    </div>
  );
};

export default Loader;
