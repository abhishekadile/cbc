import React from 'react';
import Dashboard from './components/Dashboard';

function App() {
  return (
    <div className="min-h-screen bg-background text-foreground flex flex-col">
      <header className="border-b border-border bg-card px-6 py-4 flex items-center justify-between">
        <div className="flex items-center space-x-2">
          <div className="w-8 h-8 rounded-full bg-blue-500 flex items-center justify-center">
            <span className="font-bold text-white text-sm">CBC</span>
          </div>
          <h1 className="text-xl font-semibold tracking-tight">Multispectral CBC Imaging</h1>
        </div>
        <div className="text-sm text-muted-foreground">
          Prototype Mode
        </div>
      </header>
      <main className="flex-1 p-6">
        <Dashboard />
      </main>
    </div>
  );
}

export default App;
