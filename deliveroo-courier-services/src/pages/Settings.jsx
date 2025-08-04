import React, { useState } from 'react';
import './Settings.css';

const Settings = () => {
  const [darkMode, setDarkMode] = useState(false);
  const [notifications, setNotifications] = useState(true);
  const [email, setEmail] = useState('john.doe@example.com');
  const [phone, setPhone] = useState('+1234567890');

  const toggleDarkMode = () => setDarkMode(!darkMode);
  const toggleNotifications = () => setNotifications(!notifications);

  const handleSubmit = (e) => {
    e.preventDefault();
    alert('Settings updated successfully!');
  };

  return (
    <div className="settings-page">
      <div className="settings-container">
        <h2 className="settings-title">User Settings</h2>

        <form className="settings-form" onSubmit={handleSubmit}>
          <div className="settings-section">
            <h3>Account Info</h3>
            <label>Email Address</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="Enter your email"
              required
            />

            <label>Phone Number</label>
            <input
              type="tel"
              value={phone}
              onChange={(e) => setPhone(e.target.value)}
              placeholder="Enter phone number"
              required
            />
          </div>

          <div className="settings-section">
            <h3>Preferences</h3>
            <div className="toggle-option">
              <label>Dark Mode</label>
              <input type="checkbox" checked={darkMode} onChange={toggleDarkMode} />
            </div>
            <div className="toggle-option">
              <label>Notifications</label>
              <input type="checkbox" checked={notifications} onChange={toggleNotifications} />
            </div>
          </div>

          <div className="settings-section">
            <h3>Security</h3>
            <label>New Password</label>
            <input type="password" placeholder="Enter new password" />
            <label>Confirm Password</label>
            <input type="password" placeholder="Confirm new password" />
          </div>

          <button type="submit" className="save-button">Save Changes</button>
        </form>
      </div>
    </div>
  );
};

export default Settings;
