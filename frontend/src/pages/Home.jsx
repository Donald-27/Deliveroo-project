import React from "react";
import { Link } from "react-router-dom";
import Button from "../components/common/Button";

const Home = () => {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-white text-center px-4">
      <img src="/logo.svg" alt="Deliveroo Logo" className="w-24 mb-4" />
      <h1 className="text-4xl font-bold text-blue-800 mb-4">Welcome to Deliveroo</h1>
      <p className="text-gray-600 max-w-xl mb-6">
        Kenya's smartest courier service for businesses, individuals, and e-commerce. Track, send, and receive with proof of delivery, eco mode, and smart assignment system.
      </p>
      <div className="space-x-4">
        <Link to="/login">
          <Button>Login</Button>
        </Link>
        <Link to="/dashboard">
          <Button className="bg-gray-700 hover:bg-gray-800">Dashboard</Button>
        </Link>
      </div>
    </div>
  );
};

export default Home;
