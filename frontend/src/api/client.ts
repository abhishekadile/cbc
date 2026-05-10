const API_BASE = '/api';

export const fetchHealth = async () => {
  const res = await fetch(`${API_BASE}/health`);
  if (!res.ok) {
    console.error(`Failed to fetch health: ${res.status} ${res.statusText}`);
    return null;
  }
  return res.json();
};

export const fetchDeviceStatus = async () => {
  const res = await fetch(`${API_BASE}/devices/status`);
  if (!res.ok) {
    console.error(`Failed to fetch device status: ${res.status} ${res.statusText}`);
    return null;
  }
  return res.json();
};

export const triggerSingleCapture = async () => {
  const res = await fetch(`${API_BASE}/capture/single`, { method: 'POST' });
  if (!res.ok) {
    console.error(`Failed to trigger capture: ${res.status} ${res.statusText}`);
    throw new Error('Capture failed');
  }
  return res.json();
};

export const triggerDemoScan = async () => {
  const res = await fetch(`${API_BASE}/capture/demo-multispectral`, { method: 'POST' });
  if (!res.ok) {
    console.error(`Failed to trigger demo scan: ${res.status} ${res.statusText}`);
    throw new Error('Demo scan failed');
  }
  return res.json();
};

export const fetchScans = async () => {
  const res = await fetch(`${API_BASE}/scans`);
  if (!res.ok) {
    console.error(`Failed to fetch scans: ${res.status} ${res.statusText}`);
    return [];
  }

  const data = await res.json();
  return Array.isArray(data) ? data : [];
};

export const fetchScan = async (scanId: string) => {
  const res = await fetch(`${API_BASE}/scans/${scanId}`);
  if (!res.ok) {
    console.error(`Failed to fetch scan detail: ${res.status} ${res.statusText}`);
    return null;
  }
  return res.json();
};
