import platform
import socket
import getpass

def get_system_info():
    return {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "Logged in User": getpass.getuser()
    }
