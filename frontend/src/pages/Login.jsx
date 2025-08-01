import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { loginUser } from "../redux/slices/authSlice";
import { useNavigate } from "react-router-dom";
import Input from "../components/common/Input";
import Button from "../components/common/Button";

const Login = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [credentials, setCredentials] = useState({ email: "", password: "" });

  const handleChange = (e) => {
    setCredentials({ ...credentials, [e.target.name]: e.target.value });
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    const result = await dispatch(loginUser(credentials));
    if (result?.payload?.token) {
      navigate("/dashboard");
    } else {
      alert("Invalid login. Try again.");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-100 to-purple-100">
      <form onSubmit={handleLogin} className="bg-white p-8 rounded shadow-lg w-full max-w-md">
        <h2 className="text-2xl font-bold mb-6 text-center text-blue-700">Deliveroo Login</h2>
        <Input label="Email" type="email" name="email" value={credentials.email} onChange={handleChange} required />
        <Input label="Password" type="password" name="password" value={credentials.password} onChange={handleChange} required />
        <Button type="submit" className="w-full mt-4">Login</Button>
      </form>
    </div>
  );
};

export default Login;
