import React from "react";
import { Routes, Route } from "react-router-dom";
import AppRoutes from "./routes/AppRoutes";
import "./App.css"; // Optional for custom styles
import "tailwindcss/tailwind.css";

const App = () => {
  return (
    <div className="min-h-screen w-full bg-gradient-to-br from-[#0f172a] via-[#1e293b] to-[#0f172a] text-white font-sans">
      <div className="relative z-10">
        <AppRoutes />
      </div>

      {/* Background visual effect */}
      <div
        className="fixed top-0 left-0 w-full h-full z-0"
        style={{
          background: "radial-gradient(circle at 20% 40%, rgba(255,255,255,0.04), transparent 70%)",
          maskImage: "radial-gradient(ellipse at center, black 40%, transparent 100%)",
          WebkitMaskImage: "radial-gradient(ellipse at center, black 40%, transparent 100%)"
        }}
      />
    </div>
  );
};

export default App;
