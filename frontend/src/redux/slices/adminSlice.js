import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import api from "../../services/api";

const initialState = {
  performance: [],
  loading: false,
};

export const fetchPerformance = createAsyncThunk(
  "admin/fetchPerf",
  async (_, { rejectWithValue }) => {
    try {
      const { data } = await api.get("/admin/performance");
      return data;
    } catch (err) {
      return rejectWithValue(err.response.data);
    }
  }
);

const adminSlice = createSlice({
  name: "admin",
  initialState,
  extraReducers: (builder) => {
    builder
      .addCase(fetchPerformance.pending, (s) => { s.loading = true; })
      .addCase(fetchPerformance.fulfilled, (s, a) => {
        s.loading = false;
        s.performance = a.payload;
      })
      .addCase(fetchPerformance.rejected, (s) => { s.loading = false; });
  },
});

export default adminSlice.reducer;
