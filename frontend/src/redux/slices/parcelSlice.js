import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import api from "../../services/api";

const initialState = {
  parcels: [],
  loading: false,
};

export const fetchParcels = createAsyncThunk(
  "parcel/fetchAll",
  async (_, { rejectWithValue }) => {
    try {
      const { data } = await api.get("/parcels");
      return data;
    } catch (err) {
      return rejectWithValue(err.response.data);
    }
  }
);

const parcelSlice = createSlice({
  name: "parcel",
  initialState,
  extraReducers: (builder) => {
    builder
      .addCase(fetchParcels.pending, (s) => { s.loading = true; })
      .addCase(fetchParcels.fulfilled, (s, a) => {
        s.loading = false;
        s.parcels = a.payload;
      })
      .addCase(fetchParcels.rejected, (s) => { s.loading = false; });
  },
});

export default parcelSlice.reducer;
