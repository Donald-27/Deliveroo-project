// frontend/src/components/Layout.jsx

import { Link, Outlet, useLocation } from "react-router-dom";
import { useEffect } from "react";
import { Toaster } from "react-hot-toast";
import { UserNav } from "./UserNav";
import { Footer } from "./Footer";
import ChatWidget from "./widgets/ChatWidget";
import FeedbackPrompt from "./widgets/FeedbackPrompt";
import NotificationToast from "./widgets/NotificationToast";

export default function Layout() {
  const location = useLocation();

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [location.pathname]);

  return (
    <div className="min-h-screen flex flex-col bg-gray-50 text-gray-800">
      <Toaster position="top-right" />
      <NotificationToast />
      <UserNav />

      <main className="flex-grow container mx-auto px-4 py-6">
        <Outlet />
        <ChatWidget />
        <FeedbackPrompt />
      </main>

      <Footer />
    </div>
  );
}
