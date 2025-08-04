import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

const BASE_URL = "http://localhost:5000/api/auth";

export const registerUser = createAsyncThunk(
  "auth/registerUser",
  async (formData, thunkAPI) => {
    try {
      const response = await axios.post(`${BASE_URL}/signup`, formData);
      return response.data;
    } catch (error) {
      return thunkAPI.rejectWithValue(error.response?.data?.message || "Registration failed");
    }
  }
);

export const loginUser = createAsyncThunk(
  "auth/loginUser",
  async (formData, thunkAPI) => {
    try {
      const response = await axios.post(`${BASE_URL}/login`, formData);
      localStorage.setItem("token", response.data.token);
      return response.data;
    } catch (error) {
      return thunkAPI.rejectWithValue(error.response?.data?.message || "Login failed");
    }
  }
);

const authSlice = createSlice({
  name: "auth",
  initialState: {
    user: null,
    token: localStorage.getItem("token") || null,
    loading: false,
    error: null,
  },
  reducers: {
    logout: (state) => {
      state.user = null;
      state.token = null;
      localStorage.removeItem("token");
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(registerUser.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(registerUser.fulfilled, (state, action) => {
        state.loading = false;
        state.user = action.payload.user;
        state.token = action.payload.token;
      })
      .addCase(registerUser.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      })
      .addCase(loginUser.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(loginUser.fulfilled, (state, action) => {
        state.loading = false;
        state.user = action.payload.user;
        state.token = action.payload.token;
      })
      .addCase(loginUser.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  },
});

export const { logout } = authSlice.actions;
export default authSlice.reducer;
