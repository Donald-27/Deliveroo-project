import React from 'react';

const Input = ({
  label,
  type = 'text',
  value,
  onChange,
  placeholder,
  className = '',
  required = false,
  icon = null,
}) => {
  return (
    <div className="w-full mb-4">
      {label && <label className="block mb-1 text-sm text-gray-300">{label}</label>}
      <div className="relative">
        {icon && (
          <span className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400">
            {icon}
          </span>
        )}
        <input
          type={type}
          value={value}
          onChange={onChange}
          placeholder={placeholder}
          required={required}
          className={`w-full px-4 py-2 bg-black/40 text-white border border-gray-700 rounded-xl backdrop-blur-md focus:outline-none focus:ring-2 focus:ring-indigo-500 ${icon ? 'pl-10' : ''} ${className}`}
        />
      </div>
    </div>
  );
};

export default Input;
