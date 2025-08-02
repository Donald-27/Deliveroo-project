import React from "react";
import { FaUserPlus } from "react-icons/fa";
import Button from "../components/common/Button";

const Referrals = () => {
  const referralCode = "DELIV123";

  return (
    <div className="min-h-screen p-8 bg-gradient-to-tr from-[#121826] to-[#1e2c4a] text-white">
      <div className="max-w-2xl mx-auto text-center">
        <h1 className="text-4xl font-bold mb-4">Refer & Earn</h1>
        <p className="text-gray-400 mb-6">Invite your friends and earn rewards when they send or receive packages.</p>

        <div className="bg-[#202d44] p-6 rounded-xl border border-purple-600">
          <p className="text-xl font-semibold">Your Referral Code</p>
          <div className="mt-4 text-2xl bg-[#1a2538] rounded-lg p-2 border border-purple-500">{referralCode}</div>
          <Button label="Copy Code" className="mt-4" />
        </div>
      </div>
    </div>
  );
};

export default Referrals;
