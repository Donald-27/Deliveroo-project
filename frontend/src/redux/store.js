import { configureStore } from "@reduxjs/toolkit";
import authReducer from "./slices/authSlice";
import parcelReducer from "./slices/parcelSlice";
import adminReducer from "./slices/adminSlice";

export default configureStore({
  reducer: {
    auth: authReducer,
    parcel: parcelReducer,
    admin: adminReducer,
  },
});
