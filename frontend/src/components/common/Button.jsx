import React from 'react';

const Button = ({
  children,
  type = 'button',
  variant = 'primary',
  onClick,
  className = '',
  ...props
}) => {
  const baseStyles = {
    primary:
      'bg-gradient-to-r from-purple-500 to-indigo-600 text-white shadow-lg hover:scale-105',
    secondary:
      'bg-white text-indigo-600 border border-indigo-600 hover:bg-indigo-50',
    ghost:
      'bg-transparent text-indigo-600 hover:text-purple-600 underline',
  };

  return (
    <button
      type={type}
      onClick={onClick}
      className={`px-6 py-2 rounded-full font-medium transition-all duration-300 ${baseStyles[variant]} ${className}`}
      {...props}
    >
      {children}
    </button>
  );
};

export default Button;
