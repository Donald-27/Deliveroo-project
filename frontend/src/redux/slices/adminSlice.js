// frontend/src/redux/slices/adminSlice.js
import { createSlice } from "@reduxjs/toolkit";

const adminSlice = createSlice({
  name: "admin",
  initialState: {
    users: [],
    couriers: [],
    loading: false,
    error: null,
  },
  reducers: {
    setUsers: (state, action) => {
      state.users = action.payload;
    },
    setCouriers: (state, action) => {
      state.couriers = action.payload;
    },
  },
});

export const { setUsers, setCouriers } = adminSlice.actions;
export default adminSlice.reducer;
