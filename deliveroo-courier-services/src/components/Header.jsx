import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './Header.css';

const Header = () => {
  const [time, setTime] = useState(new Date());
  const [menuOpen, setMenuOpen] = useState(false);
  const [showLogin, setShowLogin] = useState(false);
  const [showSignup, setShowSignup] = useState(false);
  const [authData, setAuthData] = useState({ email: '', password: '', full_name: '' });
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [user, setUser] = useState(null);
  const [error, setError] = useState('');
  const [stats, setStats] = useState({ total: 0, inTransit: 0, delivered: 0, pending: 0 });
  const navigate = useNavigate();

  useEffect(() => {
    const interval = setInterval(() => setTime(new Date()), 1000);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const res = await fetch('http://localhost:5000/api/parcels/');
        const parcels = await res.json();
        const total = parcels.length;
        const inTransit = parcels.filter(p => p.status.toLowerCase() === 'in transit').length;
        const delivered = parcels.filter(p => p.status.toLowerCase() === 'delivered').length;
        const pending = parcels.filter(p => p.status.toLowerCase() === 'pending').length;
        setStats({ total, inTransit, delivered, pending });
      } catch (err) {
        console.error('Error fetching stats:', err);
      }
    };
    fetchStats();
  }, []);

  const toggleMenu = () => setMenuOpen(!menuOpen);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setAuthData((prev) => ({ ...prev, [name]: value }));
  };

  const handleAuth = async (e, isLogin) => {
    e.preventDefault();
    setError('');
    const endpoint = isLogin ? 'login' : 'register';
    const payload = isLogin ? {
      email: authData.email,
      password: authData.password,
    } : authData;

    try {
      const res = await fetch(`http://localhost:5000/api/auth/${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      const data = await res.json();
      if (res.ok) {
        localStorage.setItem('token', data.token);
        setUser(data.user);
        setIsAuthenticated(true);
        setShowLogin(false);
        setShowSignup(false);
        setAuthData({ email: '', password: '', full_name: '' });
      } else {
        setError(data.message || `${isLogin ? 'Login' : 'Signup'} failed`);
      }
    } catch (err) {
      setError('Network error');
    }
  };

  const logout = () => {
    localStorage.removeItem('token');
    setIsAuthenticated(false);
    setUser(null);
  };

  const handleRestrictedClick = (e) => {
    if (!isAuthenticated) {
      e.preventDefault();
      alert('Please log in or sign up to access this feature.');
    }
  };

  return (
    <>
      <header className={`deliveroo-header-v2 ${showLogin || showSignup ? 'blurred-bg' : ''}`}>
        <div className="top-bar">
          <div className="logo-area">
            <div className="main-logo">🚚 Deliveroo</div>
            <div className="tagline">Speed. Precision. Simplicity.</div>
          </div>

          <div className="status-bar">
            <div className="date-time">
              <div>{time.toLocaleDateString()}</div>
              <div>{time.toLocaleTimeString()}</div>
            </div>

            <div className="notifications">
              <span className="dot" />🔔
            </div>

            {isAuthenticated ? (
              <div className="profile-box">
                <img src="https://i.pravatar.cc/40" alt="User" />
                <div className="user-info">
                  <span>{user?.name || 'User'}</span>
                  <span className="role">Courier</span>
                </div>
                <button onClick={logout} className="logout-btn">Logout</button>
              </div>
            ) : (
              <div className="auth-buttons">
                <button className="btn-login" onClick={() => setShowLogin(true)}>Login</button>
                <button className="btn-signup" onClick={() => setShowSignup(true)}>Sign Up</button>
              </div>
            )}

            <div className="hamburger" onClick={toggleMenu}>☰</div>
          </div>
        </div>

        <nav className={`main-nav ${menuOpen ? 'show' : ''}`}>
          <Link to="/">🏠 Home</Link>
          <Link to="/book" onClick={handleRestrictedClick}>📦 Book Delivery</Link>
          <Link to="/track" onClick={handleRestrictedClick}>🛰️ Track Parcel</Link>
          <Link to="/smart-assign" onClick={handleRestrictedClick}>🤖 Smart Assign</Link>
          <Link to="/dashboard" onClick={handleRestrictedClick}>📊 Dashboard</Link>
        </nav>

        <div className="stats-banner">
          <div className="stat-item"><span className="label">Parcels Today</span><span className="value">{stats.total}</span></div>
          <div className="stat-item"><span className="label">In Transit</span><span className="value">{stats.inTransit}</span></div>
          <div className="stat-item"><span className="label">Delivered</span><span className="value">{stats.delivered}</span></div>
          <div className="stat-item"><span className="label">Pending</span><span className="value">{stats.pending}</span></div>
        </div>
      </header>

      {(showLogin || showSignup) && (
        <div className="auth-modal">
          <div className="auth-form">
            <h2>{showLogin ? 'Login' : 'Sign Up'}</h2>
            <form onSubmit={(e) => handleAuth(e, showLogin)}>
              {!showLogin && (
                <input
                  type="text"
                  name="full_name"
                  placeholder="Full Name"
                  value={authData.full_name}
                  onChange={handleInputChange}
                  required
                />
              )}
              <input
                type="email"
                name="email"
                placeholder="Email"
                value={authData.email}
                onChange={handleInputChange}
                required
              />
              <input
                type="password"
                name="password"
                placeholder="Password"
                value={authData.password}
                onChange={handleInputChange}
                required
              />
              {error && <p className="error-text">{error}</p>}
              <button type="submit" className="submit-btn">{showLogin ? 'Login' : 'Sign Up'}</button>
              <button type="button" className="close-btn" onClick={() => { setShowLogin(false); setShowSignup(false); }}>Cancel</button>
            </form>
          </div>
        </div>
      )}
    </>
  );
};

export default Header;
