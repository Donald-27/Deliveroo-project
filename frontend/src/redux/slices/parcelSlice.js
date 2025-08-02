// frontend/src/redux/slices/parcelSlice.js
import { createSlice } from "@reduxjs/toolkit";

const parcelSlice = createSlice({
  name: "parcels",
  initialState: {
    items: [],
    loading: false,
    error: null,
  },
  reducers: {
    fetchParcelsStart: (state) => {
      state.loading = true;
    },
    fetchParcelsSuccess: (state, action) => {
      state.loading = false;
      state.items = action.payload;
    },
    fetchParcelsFailure: (state, action) => {
      state.loading = false;
      state.error = action.payload;
    },
  },
});

export const { fetchParcelsStart, fetchParcelsSuccess, fetchParcelsFailure } = parcelSlice.actions;
export default parcelSlice.reducer;
