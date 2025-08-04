import React from 'react';
import './Dashboard.css';
import { FaBox, FaClock, FaLeaf, FaTachometerAlt } from 'react-icons/fa';

const stats = [
  { label: 'Total Deliveries', value: 128, icon: <FaBox />, color: '#4f46e5' },
  { label: 'On-Time Rate', value: '96%', icon: <FaClock />, color: '#10b981' },
  { label: 'Eco Deliveries', value: 48, icon: <FaLeaf />, color: '#22c55e' },
  { label: 'Avg Delivery Time', value: '1h 24m', icon: <FaTachometerAlt />, color: '#f59e0b' },
];

const Dashboard = () => {
  return (
    <div className="dashboard-container">
      <header className="dashboard-header">
        <h1>Welcome Back, Courier ✨</h1>
        <p>Track your performance and insights below.</p>
      </header>

      <section className="dashboard-stats">
        {stats.map((stat, i) => (
          <div className="dashboard-card" key={i} style={{ borderColor: stat.color }}>
            <div className="icon" style={{ backgroundColor: stat.color }}>
              {stat.icon}
            </div>
            <div className="info">
              <h2>{stat.value}</h2>
              <p>{stat.label}</p>
            </div>
          </div>
        ))}
      </section>

      <section className="dashboard-actions">
        <button className="action-btn">📦 Create New Delivery</button>
        <button className="action-btn">📈 View Performance</button>
        <button className="action-btn">🛡️ Report Incident</button>
      </section>
    </div>
  );
};

export default Dashboard;
