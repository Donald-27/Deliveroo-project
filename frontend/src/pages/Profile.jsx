import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { fetchUser, updateUser } from "../redux/slices/authSlice";
import Input from "../components/common/Input";
import Button from "../components/common/Button";

const Profile = () => {
  const dispatch = useDispatch();
  const { user, loading } = useSelector((state) => state.auth);

  useEffect(() => {
    dispatch(fetchUser());
  }, [dispatch]);

  const handleSubmit = (e) => {
    e.preventDefault();
    const form = Object.fromEntries(new FormData(e.target));
    dispatch(updateUser(form));
  };

  if (loading) return <p>Loading...</p>;

  return (
    <div className="max-w-3xl mx-auto p-6 bg-white shadow rounded">
      <h2 className="text-2xl font-bold text-primary mb-4">My Profile</h2>
      <form onSubmit={handleSubmit}>
        <Input label="Name" name="name" defaultValue={user.name} />
        <Input label="Email" name="email" defaultValue={user.email} disabled />
        <Input label="Phone" name="phone" defaultValue={user.phone} />

        <div className="mb-4">
          <label className="block mb-1 font-medium">Referral Code</label>
          <div className="flex items-center space-x-2">
            <span className="px-3 py-2 border rounded bg-gray-100">{user.referralCode}</span>
            <Button onClick={() => navigator.clipboard.writeText(user.referralCode)}>Copy</Button>
          </div>
        </div>

        <div className="mb-4">
          <h3 className="font-semibold mb-2">Loyalty Points: <span className="text-accent">{user.loyaltyPoints}</span></h3>
        </div>

        <Button type="submit">Save Changes</Button>
      </form>
    </div>
  );
};

export default Profile;
