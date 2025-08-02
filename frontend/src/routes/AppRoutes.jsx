// frontend/src/routes/AppRoutes.jsx
import React from "react";
import { Routes, Route } from "react-router-dom";
import {
  Home, Login, Dashboard, CreateDelivery, TrackParcel, AdminPanel, Profile,
  BookDelivery, SavedAddresses, Templates, ScheduleDelivery, QRReceipt, Referrals,
  BulkBooking, EcoMode, LiveCourier, Alerts, Performance, ReportIncident, SmartAssign,
} from "../pages";

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/create" element={<CreateDelivery />} />
      <Route path="/track" element={<TrackParcel />} />
      <Route path="/admin" element={<AdminPanel />} />
      <Route path="/profile" element={<Profile />} />
      <Route path="/book" element={<BookDelivery />} />
      <Route path="/saved" element={<SavedAddresses />} />
      <Route path="/templates" element={<Templates />} />
      <Route path="/schedule" element={<ScheduleDelivery />} />
      <Route path="/qr" element={<QRReceipt />} />
      <Route path="/referrals" element={<Referrals />} />
      <Route path="/bulk" element={<BulkBooking />} />
      <Route path="/eco" element={<EcoMode />} />
      <Route path="/live" element={<LiveCourier />} />
      <Route path="/alerts" element={<Alerts />} />
      <Route path="/performance" element={<Performance />} />
      <Route path="/incident" element={<ReportIncident />} />
      <Route path="/smartassign" element={<SmartAssign />} />
    </Routes>
  );
};

export default AppRoutes;
