import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Home from './pages/Home';
import TrackParcel from './pages/TrackParcel';
import BookDelivery from './pages/BookDelivery';
import SmartAssign from './pages/SmartAssign';
import LiveMap from './pages/LiveMap';
import Receipt from './pages/Receipt';
import Alerts from './pages/Alerts';
import Dashboard from './pages/Dashboard';
import Settings from './pages/Settings';

import Header from './components/Header';
import Footer from './components/Footer';

import './styles/globals.css';

function App() {
  return (
    <Router>
      <div className='app-wrapper'>
        <Header />
        <main>
          <Routes>
            <Route path='/' element={<Home />} />
            <Route path='/track' element={<TrackParcel />} />
            <Route path='/book' element={<BookDelivery />} />
            <Route path='/smart-assign' element={<SmartAssign />} />
            <Route path='/map' element={<LiveMap />} />
            <Route path='/receipt' element={<Receipt />} />
            <Route path='/alerts' element={<Alerts />} />
            <Route path='/dashboard' element={<Dashboard />} />
            <Route path='/settings' element={<Settings />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
