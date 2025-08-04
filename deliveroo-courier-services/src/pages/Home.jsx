// Home.jsx
import React, { useState, useEffect } from 'react';
import './Home.css';
import Header from '../components/Header';
import Footer from '../components/Footer';
import QuoteCalculator from '../components/QuoteCalculator';
import Timeline from '../components/Timeline';

const Home = () => {
  const [stats, setStats] = useState({
    deliveries: 0,
    onTimeRate: 0,
    satisfaction: 0,
    activeCouriers: 0,
  });
  const [showScrollTop, setShowScrollTop] = useState(false);

  useEffect(() => {
   
    setTimeout(() => {
      setStats({
        deliveries: 102345,
        onTimeRate: 99.7,
        satisfaction: 4.9,
        activeCouriers: 158,
      });
    }, 500);
  
    const handleScroll = () => setShowScrollTop(window.pageYOffset > 500);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const timelineSteps = [
    { title: 'Order Received', desc: 'We got your request!', time: '08:00', done: true },
    { title: 'Courier Allocated', desc: 'Allocated to nearest courier', time: '08:10', done: true },
    { title: 'Pickup', desc: 'Courier picked up your parcel', time: '08:30', done: true },
    { title: 'In Transit', desc: 'On the way', time: '09:00', done: false },
    { title: 'Delivery', desc: 'Delivered successfully', time: '09:45', done: false },
  ];

  return (
    <>
     

      <div className="home-wrap">
        {}
        <section className="hero-section">
          <div className="hero-overlay" />
          <div className="hero-content">
            <h1>Deliveroo Courier Services</h1>
            <p>From local errands to global shipments—speed, safety, and style combined.</p>
            <button className="btn-hero">Start Your Delivery</button>
          </div>
        </section>

        {}
        <section className="announcement-marquee">
          <div className="marquee-text">
            🚀 Express 1-Hour Delivery &nbsp;&bull;&nbsp; 📦 Free Packaging &nbsp;&bull;&nbsp; 🌍 Global Coverage &nbsp;&bull;&nbsp; 🛡️ Full Insurance
          </div>
        </section>

        {}
        <section className="stats-section">
          <div className="stat-card">
            <h2>{stats.deliveries.toLocaleString()}</h2>
            <p>Deliveries Completed</p>
          </div>
          <div className="stat-card">
            <h2>{stats.onTimeRate}%</h2>
            <p>On-Time Rate</p>
          </div>
          <div className="stat-card">
            <h2>{stats.satisfaction}★</h2>
            <p>Customer Satisfaction</p>
          </div>
          <div className="stat-card">
            <h2>{stats.activeCouriers}</h2>
            <p>Active Couriers</p>
          </div>
        </section>

        {}
        <section className="quote-section">
          <h2>Get an Instant Quote</h2>
          <QuoteCalculator />
        </section>

        {}
        <section className="features-showcase">
          <div className="feature-block">
            <h3>AI Route Optimization</h3>
            <p>Our AI selects the fastest, most fuel-efficient routes automatically.</p>
          </div>
          <div className="feature-block glass">
            <h3>Secure Doorstep</h3>
            <p>QR-code verification at pickup and drop-off—no room for error.</p>
          </div>
          <div className="feature-block neon">
            <h3>Bulk & Scheduled</h3>
            <p>Upload CSVs or schedule recurring deliveries with ease.</p>
          </div>
          <div className="feature-block eco">
            <h3>Eco-Friendly Fleet</h3>
            <p>Electric bikes and low-emission vehicles available.</p>
          </div>
        </section>

        {}
        <section className="split-section">
          <div className="split-text">
            <h2>Nationwide Network</h2>
            <p>We cover every corner of Kenya—from Nairobi to remote towns—with our vast courier network.</p>
            <ul>
              <li>• Drone-enabled zones</li>
              <li>• Boda-boda express</li>
              <li>• Cargo vans & trucks</li>
            </ul>
          </div>
          <div className="split-image" />
        </section>

        {}
        <section className="timeline-section">
          <h2>Your Delivery Journey</h2>
          <Timeline steps={timelineSteps} />
        </section>

        {}
       <section className="courier-month">
  <div className="courier-header">
    <h2>🚴 Courier of the Month</h2>
    <p>Celebrating exceptional performance, dedication, and reliability.</p>
  </div>

  <div className="courier-card">
    <img src="/images/courier-of-month.jpg" alt="Top Courier" className="courier-image" />
    <div className="courier-info">
      <h3>James Otieno</h3>
      <p className="courier-quote">"Every parcel matters. I treat every delivery like it's my own."</p>

      <div className="courier-badges">
        <span className="badge green">98.7% On-Time Rate</span>
        <span className="badge blue">4.9★ Customer Rating</span>
        <span className="badge yellow">1,240 Deliveries</span>
      </div>

      <div className="courier-stats">
        <div>
          <h4>5</h4>
          <p>Years Experience</p>
        </div>
        <div>
          <h4>32km</h4>
          <p>Daily Average</p>
        </div>
        <div>
          <h4>24/7</h4>
          <p>Availability</p>
        </div>
      </div>
    </div>
  </div>
</section>


        {}
       <section className="faq-neo-section">
  <h2 className="faq-title">💬 Your Top Questions, Answered</h2>
  <p className="faq-subtitle">Everything you need to know before you send or receive with Deliveroo.</p>

  <div className="faq-container">
    {[
      {
        q: "🚚 How fast is Deliveroo’s delivery?",
        a: "We deliver within 1–3 hours inside cities and same-day nationwide using smart routing."
      },
      {
        q: "📦 What items can I send via Deliveroo?",
        a: "From food, documents, electronics, to fragile goods — we’ve got you covered."
      },
      {
        q: "🛰️ Can I live-track my delivery?",
        a: "Absolutely! Our GPS-enabled live map keeps you updated in real time."
      },
      {
        q: "💼 Do you offer business bulk shipping?",
        a: "Yes — we support API integrations, CSV bulk upload, and custom contracts for businesses."
      },
      {
        q: "🔒 Is my package insured?",
        a: "All parcels are covered up to KSh 100,000. You can also opt for premium insurance."
      },
      {
        q: "💳 What payment options are available?",
        a: "M-Pesa, cards, PayPal, and pay-on-delivery are all supported for your convenience."
      }
    ].map((item, i) => (
      <div className="faq-card" key={i}>
        <input type="checkbox" id={`faq-${i}`} className="faq-toggle" />
        <label htmlFor={`faq-${i}`} className="faq-question">
          {item.q}
          <span className="icon"></span>
        </label>
        <div className="faq-answer">{item.a}</div>
      </div>
    ))}
  </div>
</section>


        {}
        <section className="tips-section">
          <h2>Courier Tips & Tricks</h2>
          <ul>
            <li>📦 Use bubble wrap to protect fragile items.</li>
            <li>📋 Label packages clearly with both addresses.</li>
            <li>💧 Seal liquids in leak-proof containers.</li>
            <li>🔋 Charge your devices fully before sending electronics.</li>
            <li>🕒 Schedule deliveries early to avoid rush hours.</li>
          </ul>
        </section>

        {}
        <section className="final-cta">
          <h2>Ready to Deliver Smarter?</h2>
          <p>Join over 100,000 happy customers—ship with confidence today.</p>
          <button className="btn-secondary">Sign Up Now</button>
        </section>


        {showScrollTop && (
          <button
            className="scroll-top-btn"
            onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
          >
            ↑ Back to Top
          </button>
        )}
      </div>
    </>
  );
};

export default Home;
