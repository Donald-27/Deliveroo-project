import React from 'react';
import { Hero } from '../assets/images';
import Button from '../components/common/Button';
import { useNavigate } from 'react-router-dom';

const Home = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-gradient-to-br from-black via-indigo-900 to-black text-white flex flex-col items-center justify-center px-6">
      <img src={Hero} alt="hero" className="w-64 h-64 object-contain mb-8" />
      <h1 className="text-4xl md:text-6xl font-bold text-center bg-gradient-to-r from-purple-400 via-pink-500 to-indigo-400 bg-clip-text text-transparent drop-shadow-xl">
        Deliveroo Courier Services
      </h1>
      <p className="mt-4 text-gray-300 text-lg text-center max-w-xl">
        The most advanced, intelligent, and stunning courier delivery system on Earth.
      </p>
      <div className="mt-6 flex flex-col sm:flex-row gap-4">
        <Button onClick={() => navigate('/login')}>Login / Signup</Button>
        <Button variant="secondary" onClick={() => navigate('/dashboard')}>
          Explore Dashboard
        </Button>
      </div>
    </div>
  );
};

export default Home;
