import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import api from "../../services/api";

const initialState = {
  user: null,
  token: localStorage.getItem("token"),
  loading: false,
};

export const loginUser = createAsyncThunk(
  "auth/login",
  async (creds, { rejectWithValue }) => {
    try {
      const { data } = await api.post("/auth/login", creds);
      localStorage.setItem("token", data.access_token);
      api.defaults.headers.common.Authorization = `Bearer ${data.access_token}`;
      return data;
    } catch (err) {
      return rejectWithValue(err.response.data);
    }
  }
);

export const fetchUser = createAsyncThunk(
  "auth/fetchUser",
  async (_, { getState, rejectWithValue }) => {
    try {
      const { data } = await api.get("/auth/profile");
      return data;
    } catch (err) {
      return rejectWithValue(err.response.data);
    }
  }
);

export const updateUser = createAsyncThunk(
  "auth/updateUser",
  async (payload, { rejectWithValue }) => {
    try {
      const { data } = await api.put("/auth/profile", payload);
      return data;
    } catch (err) {
      return rejectWithValue(err.response.data);
    }
  }
);

const authSlice = createSlice({
  name: "auth",
  initialState,
  reducers: {
    logout: (state) => {
      state.user = null;
      state.token = null;
      localStorage.removeItem("token");
      delete api.defaults.headers.common.Authorization;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(loginUser.pending, (s) => { s.loading = true; })
      .addCase(loginUser.fulfilled, (s, a) => {
        s.loading = false;
        s.token = a.payload.access_token;
      })
      .addCase(loginUser.rejected, (s) => { s.loading = false; })

      .addCase(fetchUser.pending, (s) => { s.loading = true; })
      .addCase(fetchUser.fulfilled, (s, a) => {
        s.loading = false;
        s.user = a.payload;
      })
      .addCase(fetchUser.rejected, (s) => { s.loading = false; })

      .addCase(updateUser.pending, (s) => { s.loading = true; })
      .addCase(updateUser.fulfilled, (s, a) => {
        s.loading = false;
        s.user = a.payload;
      })
      .addCase(updateUser.rejected, (s) => { s.loading = false; });
  },
});

export const { logout } = authSlice.actions;
export default authSlice.reducer;
