#!/usr/bin/env python3
import os
import time

def main():
    print("--- Robot Initialization ---")
    # Using a Linux command inside Python
    user = os.popen('whoami').read().strip()
    print(f"Hello Engineer {user}!")
    
    print("Checking system battery...")
    time.sleep(1)
    print("Battery: 100%. System is GO.")
    
    print("\nRobot is now scanning the room...")
    for i in range(3, 0, -1):
        print(f"Scanning in {i}...")
        time.sleep(1)
    
    print("\n[SUCCESS] Room scan complete. No obstacles found!")

if __name__ == "__main__":
    main()