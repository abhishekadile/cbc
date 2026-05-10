const API_BASE = '/api';

export const fetchHealth = async () => {
  const res = await fetch(`${API_BASE}/health`);
  return res.json();
};

export const fetchDeviceStatus = async () => {
  const res = await fetch(`${API_BASE}/devices/status`);
  return res.json();
};

export const triggerSingleCapture = async () => {
  const res = await fetch(`${API_BASE}/capture/single`, { method: 'POST' });
  return res.json();
};

export const triggerDemoScan = async () => {
  const res = await fetch(`${API_BASE}/capture/demo-multispectral`, { method: 'POST' });
  return res.json();
};

export const fetchScans = async () => {
  const res = await fetch(`${API_BASE}/scans`);
  return res.json();
};
