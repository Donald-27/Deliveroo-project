import React from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";

const LiveMap = ({ courier }) => {
  const { lat, lng } = courier.location || { lat: 1.2921, lng: 36.8219 }; // Default Nairobi

  return (
    <MapContainer center={[lat, lng]} zoom={13} scrollWheelZoom={false} className="h-64 w-full rounded-md shadow-md z-0">
      <TileLayer
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a>'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <Marker position={[lat, lng]}>
        <Popup>
          Courier is here. <br /> {courier.name}
        </Popup>
      </Marker>
    </MapContainer>
  );
};

export default LiveMap;
