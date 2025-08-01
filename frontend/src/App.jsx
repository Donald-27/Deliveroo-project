import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import TrackParcel from "./pages/TrackParcel";
import BookDelivery from "./pages/BookDelivery";
import SavedAddresses from "./pages/SavedAddresses";
import Templates from "./pages/Templates";
import ScheduleDelivery from "./pages/ScheduleDelivery";
import QRReceipt from "./pages/QRReceipt";
import Referrals from "./pages/Referrals";
import BulkBooking from "./pages/BulkBooking";
import EcoMode from "./pages/EcoMode";
import LiveCourier from "./pages/LiveCourier";
import Alerts from "./pages/Alerts";
import Performance from "./pages/Performance";
import ReportIncident from "./pages/ReportIncident";
import SmartAssign from "./pages/SmartAssign";
import Layout from "./components/Layout";

export default function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/track" element={<TrackParcel />} />
          <Route path="/book" element={<BookDelivery />} />
          <Route path="/addresses" element={<SavedAddresses />} />
          <Route path="/templates" element={<Templates />} />
          <Route path="/schedule" element={<ScheduleDelivery />} />
          <Route path="/receipt" element={<QRReceipt />} />
          <Route path="/referrals" element={<Referrals />} />
          <Route path="/bulk" element={<BulkBooking />} />
          <Route path="/eco" element={<EcoMode />} />
          <Route path="/live" element={<LiveCourier />} />
          <Route path="/alerts" element={<Alerts />} />
          <Route path="/performance" element={<Performance />} />
          <Route path="/incident" element={<ReportIncident />} />
          <Route path="/assign" element={<SmartAssign />} />
        </Routes>
      </Layout>
    </Router>
  );
}
