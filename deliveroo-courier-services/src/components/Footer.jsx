import React from 'react';
import './Footer.css';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="footer-brand">
          <img src="/logo.svg" alt="Deliveroo Logo" className="footer-logo" />
          <h2>Deliveroo Courier</h2>
          <p>Delivering tomorrow's logistics, today.</p>
        </div>

        <div className="footer-links">
          <div>
            <h4>Company</h4>
            <ul>
              <li><a href="#">About Us</a></li>
              <li><a href="#">Our Services</a></li>
              <li><a href="#">Careers</a></li>
              <li><a href="#">Investors</a></li>
            </ul>
          </div>
          <div>
            <h4>Support</h4>
            <ul>
              <li><a href="#">Help Center</a></li>
              <li><a href="#">Track Your Parcel</a></li>
              <li><a href="#">Smart Assign</a></li>
              <li><a href="#">Book Delivery</a></li>
            </ul>
          </div>
          <div>
            <h4>Connect</h4>
            <ul>
              <li><a href="#">LinkedIn</a></li>
              <li><a href="#">X (Twitter)</a></li>
              <li><a href="#">Pinterest</a></li>
              <li><a href="#">Instagram</a></li>
            </ul>
          </div>
        </div>

        <div className="footer-subscribe">
          <h4>Subscribe to Updates</h4>
          <form>
            <input type="email" placeholder="Your email address" />
            <button type="submit">Subscribe</button>
          </form>
          <p className="footer-copy">© 2025 Deliveroo Courier Services. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
