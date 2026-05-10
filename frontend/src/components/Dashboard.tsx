import React, { useEffect, useState } from 'react';
import { Camera, HardDrive, Cpu, Activity, Play, Zap, CheckCircle2, AlertCircle, Image as ImageIcon, ChevronLeft } from 'lucide-react';
import { fetchDeviceStatus, triggerDemoScan, triggerSingleCapture, fetchScans, fetchScan } from '../api/client';
import { motion } from 'framer-motion';

interface DeviceStatus {
  connected: boolean
  simulated: boolean
  detail?: string
  model?: string
  source?: string
}

interface SystemStatus {
  camera: DeviceStatus
  xy_stage: DeviceStatus
  z_focus?: DeviceStatus
  lights: DeviceStatus
  storage: DeviceStatus
  network?: DeviceStatus
}

interface ScanImage {
  filename: string
  wavelength_nm?: number
  capture_id?: number
  thumbnail_url?: string
  url?: string
  label?: string
  camera_source?: string
  image_simulated?: boolean
  light_simulated?: boolean
}

interface ScanSession {
  scan_id: string
  created_at: string
  images: ScanImage[]
  camera_source?: string
  simulated?: boolean
}

const StatusBadge = ({ connected, simulated, source }: { connected: boolean, simulated: boolean, source?: string }) => {
  if (!connected) return <span className="flex items-center text-red-400 text-xs"><AlertCircle className="w-3 h-3 mr-1"/> Offline</span>;
  if (simulated) return <span className="flex items-center text-yellow-500 text-xs"><Zap className="w-3 h-3 mr-1"/> Simulated</span>;
  if (source === 'picamera2') return <span className="flex items-center text-green-400 text-xs"><CheckCircle2 className="w-3 h-3 mr-1"/> Real Camera</span>;
  return <span className="flex items-center text-green-400 text-xs"><CheckCircle2 className="w-3 h-3 mr-1"/> Online</span>;
};

const Dashboard = () => {
  const [status, setStatus] = useState<SystemStatus | null>(null);
  const [scans, setScans] = useState<ScanSession[]>([]);
  const [isScanning, setIsScanning] = useState(false);
  const [selectedScanId, setSelectedScanId] = useState<string | null>(null);
  const [selectedScan, setSelectedScan] = useState<ScanSession | null>(null);

  useEffect(() => {
    const loadData = async () => {
      try {
        const [devStatus, scansData] = await Promise.all([
          fetchDeviceStatus(),
          fetchScans()
        ]);
        setStatus(devStatus);
        setScans(Array.isArray(scansData) ? scansData : []);
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
      const response = await triggerDemoScan();
      setTimeout(async () => {
        const scansData = await fetchScans();
        setScans(Array.isArray(scansData) ? scansData : []);
        setIsScanning(false);
        if (response.scan_id) {
            handleScanClick(response.scan_id);
        }
      }, 3500); // Wait for demo scan to complete
    } catch (err) {
      console.error(err);
      setIsScanning(false);
    }
  };

  const handleSingleCapture = async () => {
      setIsScanning(true);
      try {
          const response = await triggerSingleCapture();
          const scansData = await fetchScans();
          setScans(Array.isArray(scansData) ? scansData : []);
          setIsScanning(false);
          if (response.scan_id) {
              handleScanClick(response.scan_id);
          }
      } catch (err) {
          console.error(err);
          setIsScanning(false);
      }
  };

  const handleScanClick = async (scanId: string) => {
      setSelectedScanId(scanId);
      const data = await fetchScan(scanId);
      setSelectedScan(data);
  };

  return (
    <div className="max-w-7xl mx-auto space-y-6">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Hardware Status Panel */}
          <div className="col-span-1 space-y-4">
            <h2 className="text-lg font-semibold mb-4">Hardware Status</h2>
            
            <div className="bg-card border border-border rounded-xl p-4 flex items-center justify-between shadow-sm">
              <div className="flex items-center space-x-3">
                <div className="p-2 bg-blue-500/10 rounded-lg text-blue-400"><Camera size={20} /></div>
                <div>
                  <p className="font-medium text-sm">{status?.camera?.model || 'Camera'}</p>
                  <p className="text-xs text-muted-foreground">{status?.camera?.source === 'picamera2' ? 'MIPI CSI Global Shutter' : 'Mock Mode'}</p>
                </div>
              </div>
              {status && <StatusBadge connected={status.camera.connected} simulated={status.camera.simulated} source={status.camera.source} />}
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
                <br /><br />
                <span className="text-xs text-yellow-500 font-semibold border border-yellow-500/30 bg-yellow-500/10 px-2 py-1 rounded">Research mode: Not for clinical use</span>
              </p>
              
              <div className="flex space-x-4">
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
                    <span>{isScanning ? 'Acquiring...' : 'Run Multispectral Demo Scan'}</span>
                  </button>

                  <button 
                    onClick={handleSingleCapture}
                    disabled={isScanning}
                    className={`px-6 py-3 rounded-xl font-medium flex items-center space-x-2 transition-all shadow-lg ${
                      isScanning 
                      ? 'bg-zinc-800 text-zinc-500 cursor-wait border border-zinc-700' 
                      : 'bg-zinc-800 hover:bg-zinc-700 text-white border border-zinc-700'
                    }`}
                  >
                    <Camera size={18} />
                    <span>Capture Single Image</span>
                  </button>
              </div>
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
                    <div key={scan.scan_id} onClick={() => handleScanClick(scan.scan_id)} className="bg-card border border-border rounded-xl p-4 shadow-sm hover:border-blue-500/50 transition-colors cursor-pointer group">
                      <div className="flex justify-between items-start mb-3">
                        <span className="text-xs font-mono text-muted-foreground">{scan.scan_id.split('_')[1]}</span>
                        <div className="flex space-x-2">
                            {scan.simulated ? (
                                <span className="text-[10px] uppercase px-2 py-1 bg-yellow-500/20 text-yellow-300 rounded-full">Mock</span>
                            ) : (
                                <span className="text-[10px] uppercase px-2 py-1 bg-green-500/20 text-green-300 rounded-full">Real IMX296</span>
                            )}
                            <span className="text-[10px] uppercase px-2 py-1 bg-secondary rounded-full">{Array.isArray(scan.images) ? scan.images.length : 0} layers</span>
                        </div>
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

        {/* Scan Detail View */}
        {selectedScan && (
            <div className="mt-8 pt-8 border-t border-border">
                <div className="flex items-center justify-between mb-6">
                    <div>
                        <h2 className="text-2xl font-bold flex items-center">
                            <button onClick={() => { setSelectedScan(null); setSelectedScanId(null); }} className="mr-4 text-muted-foreground hover:text-white transition-colors">
                                <ChevronLeft size={24} />
                            </button>
                            Scan Detail
                        </h2>
                        <p className="text-muted-foreground text-sm mt-1 ml-10">{selectedScan.scan_id}</p>
                    </div>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 ml-10">
                    {selectedScan.images?.map((img, idx) => (
                        <div key={idx} className="bg-card border border-border rounded-xl overflow-hidden shadow-sm">
                            <div className="h-48 bg-black relative flex items-center justify-center">
                                {img.thumbnail_url || img.url ? (
                                    <a href={img.url} target="_blank" rel="noreferrer">
                                        <img src={img.thumbnail_url || img.url} alt={img.label} className="object-cover w-full h-full hover:opacity-80 transition-opacity" />
                                    </a>
                                ) : (
                                    <ImageIcon className="text-zinc-800 w-12 h-12" />
                                )}
                            </div>
                            <div className="p-4">
                                <h4 className="font-semibold text-sm mb-2 capitalize">{img.label} Channel</h4>
                                <div className="space-y-1">
                                    <p className="text-xs flex justify-between"><span className="text-muted-foreground">Wavelength:</span> <span>{img.wavelength_nm ? `${img.wavelength_nm} nm` : 'Broadband'}</span></p>
                                    <p className="text-xs flex justify-between"><span className="text-muted-foreground">Source:</span> <span>{img.camera_source}</span></p>
                                    <p className="text-xs flex justify-between"><span className="text-muted-foreground">Camera:</span> <span className={img.image_simulated ? 'text-yellow-400' : 'text-green-400'}>{img.image_simulated ? 'Simulated' : 'Real Capture'}</span></p>
                                    <p className="text-xs flex justify-between"><span className="text-muted-foreground">Lighting:</span> <span className={img.light_simulated ? 'text-yellow-400' : 'text-green-400'}>{img.light_simulated ? 'Simulated' : 'Real Hardware'}</span></p>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        )}
    </div>
  );
};

export default Dashboard;
