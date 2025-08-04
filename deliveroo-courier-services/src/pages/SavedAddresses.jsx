import React, { useEffect, useState } from 'react';
import './SavedAddresses.css';

const SavedAddresses = () => {
  const [addresses, setAddresses] = useState([]);
  const [newAddress, setNewAddress] = useState('');
  const [label, setLabel] = useState('');
  const [error, setError] = useState('');
  const [status, setStatus] = useState('');

  const fetchAddresses = async () => {
    try {
      const res = await fetch('http://localhost:5000/api/user/addresses');
      const data = await res.json();
      if (!res.ok) throw new Error(data.message || 'Failed to fetch addresses');
      setAddresses(data.addresses || []);
    } catch (err) {
      setError(err.message);
    }
  };

  useEffect(() => {
    fetchAddresses();
  }, []);

  const handleAdd = async () => {
    if (!newAddress || !label) {
      setError('Please enter both address and label.');
      return;
    }

    try {
      const res = await fetch('http://localhost:5000/api/user/addresses', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ label, address: newAddress }),
      });

      const result = await res.json();
      if (!res.ok) throw new Error(result.message || 'Failed to add address.');

      setStatus('Address saved!');
      setNewAddress('');
      setLabel('');
      fetchAddresses();
    } catch (err) {
      setError(err.message);
    }
  };

  const handleDelete = async (id) => {
    try {
      const res = await fetch(`http://localhost:5000/api/user/addresses/${id}`, {
        method: 'DELETE',
      });
      if (!res.ok) throw new Error('Failed to delete address.');
      fetchAddresses();
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="saved-addresses-page">
      <div className="addresses-container">
        <h1>🏠 Saved Addresses</h1>
        <p className="subtitle">Manage your frequently used pickup and delivery locations.</p>

        <div className="address-form">
          <input
            type="text"
            placeholder="Label (e.g., Home, Office)"
            value={label}
            onChange={(e) => setLabel(e.target.value)}
          />
          <input
            type="text"
            placeholder="Full Address"
            value={newAddress}
            onChange={(e) => setNewAddress(e.target.value)}
          />
          <button onClick={handleAdd}>+ Save Address</button>
        </div>

        {status && <p className="status success">{status}</p>}
        {error && <p className="status error">{error}</p>}

        <div className="address-list">
          {addresses.length === 0 ? (
            <p className="empty">No saved addresses yet.</p>
          ) : (
            addresses.map((addr) => (
              <div className="address-card" key={addr.id}>
                <div className="address-label">{addr.label}</div>
                <div className="address-text">{addr.address}</div>
                <button className="delete-btn" onClick={() => handleDelete(addr.id)}>Delete</button>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
};

export default SavedAddresses;
