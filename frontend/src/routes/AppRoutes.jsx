import React, { useEffect } from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { fetchUser } from "../redux/slices/authSlice";
import Home from "../pages/Home";
import Login from "../pages/Login";
import Dashboard from "../pages/Dashboard";
import TrackParcel from "../pages/TrackParcel";
import CreateDelivery from "../pages/CreateDelivery";
import AdminPanel from "../pages/AdminPanel";
import Profile from "../pages/Profile";

const PrivateRoute = ({ children }) => {
  const { token } = useSelector((state) => state.auth);
  return token ? children : <Navigate to="/login" />;
};

export default function AppRoutes() {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(fetchUser());
  }, [dispatch]);

  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />

      <Route path="/dashboard" element={
        <PrivateRoute><Dashboard /></PrivateRoute>
      } />

      <Route path="/track/:trackingId" element={<TrackParcel />} />

      <Route path="/create-delivery" element={
        <PrivateRoute><CreateDelivery /></PrivateRoute>
      } />

      <Route path="/admin" element={
        <PrivateRoute><AdminPanel /></PrivateRoute>
      } />

      <Route path="/profile" element={
        <PrivateRoute><Profile /></PrivateRoute>
      } />

      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  );
}
