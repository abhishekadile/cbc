import platform
import socket
from datetime import datetime

def get_system_info():
    return {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "release": platform.release(),
        "architecture": platform.machine(),
        "time": datetime.utcnow().isoformat()
    }
