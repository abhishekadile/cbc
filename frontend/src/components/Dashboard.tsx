import React, { useEffect, useState } from 'react';
import { Camera, HardDrive, Cpu, Activity, Play, Zap, CheckCircle2, AlertCircle } from 'lucide-react';
import { fetchDeviceStatus, triggerDemoScan, fetchScans, fetchHealth } from '../api/client';
import { motion } from 'framer-motion';

const StatusBadge = ({ connected, simulated }) => {
  if (!connected) return <span className="flex items-center text-red-400 text-xs"><AlertCircle className="w-3 h-3 mr-1"/> Offline</span>;
  if (simulated) return <span className="flex items-center text-yellow-500 text-xs"><Zap className="w-3 h-3 mr-1"/> Simulated</span>;
  return <span className="flex items-center text-green-400 text-xs"><CheckCircle2 className="w-3 h-3 mr-1"/> Online</span>;
};

const Dashboard = () => {
  const [status, setStatus] = useState<any>(null);
  const [scans, setScans] = useState<any[]>([]);
  const [isScanning, setIsScanning] = useState(false);

  useEffect(() => {
    const loadData = async () => {
      try {
        const [devStatus, scansData] = await Promise.all([
          fetchDeviceStatus(),
          fetchScans()
        ]);
        setStatus(devStatus);
        setScans(scansData);
      } catch (err) {
        console.error("Failed to load data", err);
      }
    };
    loadData();
    const interval = setInterval(loadData, 5000);
    return () => clearInterval(interval);
  }, []);

  const handleDemoScan = async () => {
    setIsScanning(true);
    try {
      await triggerDemoScan();
      setTimeout(async () => {
        const scansData = await fetchScans();
        setScans(scansData);
        setIsScanning(false);
      }, 3500); // Wait for demo scan to complete
    } catch (err) {
      console.error(err);
      setIsScanning(false);
    }
  };

  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-7xl mx-auto">
      {/* Hardware Status Panel */}
      <div className="col-span-1 space-y-4">
        <h2 className="text-lg font-semibold mb-4">Hardware Status</h2>
        
        <div className="bg-card border border-border rounded-xl p-4 flex items-center justify-between shadow-sm">
          <div className="flex items-center space-x-3">
            <div className="p-2 bg-blue-500/10 rounded-lg text-blue-400"><Camera size={20} /></div>
            <div>
              <p className="font-medium text-sm">IMX296 Camera</p>
              <p className="text-xs text-muted-foreground">MIPI CSI Global Shutter</p>
            </div>
          </div>
          {status && <StatusBadge connected={status.camera.connected} simulated={status.camera.simulated} />}
        </div>

        <div className="bg-card border border-border rounded-xl p-4 flex items-center justify-between shadow-sm">
          <div className="flex items-center space-x-3">
            <div className="p-2 bg-purple-500/10 rounded-lg text-purple-400"><Activity size={20} /></div>
            <div>
              <p className="font-medium text-sm">XY Stage & Focus</p>
              <p className="text-xs text-muted-foreground">Microcontroller Sync</p>
            </div>
          </div>
          {status && <StatusBadge connected={status.xy_stage.connected} simulated={status.xy_stage.simulated} />}
        </div>

        <div className="bg-card border border-border rounded-xl p-4 flex items-center justify-between shadow-sm">
          <div className="flex items-center space-x-3">
            <div className="p-2 bg-yellow-500/10 rounded-lg text-yellow-400"><Zap size={20} /></div>
            <div>
              <p className="font-medium text-sm">LED Light Engine</p>
              <p className="text-xs text-muted-foreground">Multispectral Array</p>
            </div>
          </div>
          {status && <StatusBadge connected={status.lights.connected} simulated={status.lights.simulated} />}
        </div>

        <div className="bg-card border border-border rounded-xl p-4 flex items-center justify-between shadow-sm mt-8">
          <div className="flex items-center space-x-3">
            <div className="p-2 bg-green-500/10 rounded-lg text-green-400"><HardDrive size={20} /></div>
            <div>
              <p className="font-medium text-sm">Local Storage</p>
              <p className="text-xs text-muted-foreground">{scans.length} scans saved</p>
            </div>
          </div>
          {status && <StatusBadge connected={status.storage.connected} simulated={status.storage.simulated} />}
        </div>
      </div>

      {/* Main Action Panel */}
      <div className="col-span-1 md:col-span-2 space-y-6">
        
        {/* Hero Card */}
        <div className="bg-gradient-to-br from-card to-card/50 border border-border rounded-2xl p-8 relative overflow-hidden">
          <div className="absolute top-0 right-0 w-64 h-64 bg-blue-500/5 rounded-full blur-3xl -mr-16 -mt-16"></div>
          <h2 className="text-2xl font-bold mb-2">Acquisition Controls</h2>
          <p className="text-muted-foreground text-sm mb-8 max-w-md">
            Initialize a multispectral scan. The system will acquire 5 discrete wavelengths (White, 405nm, 530nm, 660nm, 850nm) to prepare the sample for AI morphology analysis.
          </p>
          
          <button 
            onClick={handleDemoScan}
            disabled={isScanning}
            className={`px-6 py-3 rounded-xl font-medium flex items-center space-x-2 transition-all shadow-lg ${
              isScanning 
              ? 'bg-blue-600/50 text-white cursor-wait' 
              : 'bg-blue-600 hover:bg-blue-500 text-white'
            }`}
          >
            {isScanning ? (
              <motion.div animate={{ rotate: 360 }} transition={{ repeat: Infinity, duration: 1, ease: "linear" }}>
                <Activity size={18} />
              </motion.div>
            ) : (
              <Play size={18} />
            )}
            <span>{isScanning ? 'Acquiring Wavelengths...' : 'Run Multispectral Demo Scan'}</span>
          </button>
        </div>

        {/* Recent Scans Gallery */}
        <div>
          <h3 className="text-lg font-semibold mb-4">Recent Scans</h3>
          {scans.length === 0 ? (
            <div className="bg-card border border-border border-dashed rounded-xl p-12 flex flex-col items-center justify-center text-muted-foreground">
              <Camera className="w-8 h-8 mb-4 opacity-50" />
              <p>No scans found</p>
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {scans.slice(0, 4).map((scan) => (
                <div key={scan.scan_id} className="bg-card border border-border rounded-xl p-4 shadow-sm hover:border-blue-500/50 transition-colors cursor-pointer group">
                  <div className="flex justify-between items-start mb-3">
                    <span className="text-xs font-mono text-muted-foreground">{scan.scan_id.split('_')[1]}</span>
                    <span className="text-[10px] uppercase px-2 py-1 bg-secondary rounded-full">{scan.images.length} layers</span>
                  </div>
                  <h4 className="font-medium text-sm truncate mb-1">{scan.scan_id}</h4>
                  <p className="text-xs text-muted-foreground">{new Date(scan.created_at).toLocaleString()}</p>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
