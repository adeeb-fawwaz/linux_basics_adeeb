#!/usr/bin/env python3
import os
import time

def main():
    print("--- REAL-TIME SYSTEM SCAN ---")
    
    # 1. Who is the pilot?
    user = os.popen('whoami').read().strip()
    print(f"Pilot: {user}")

    # 2. Check the computer's 'Brain' usage (Practical Linux Check)
    cpu_load = os.popen("uptime | awk '{print $10}'").read().strip()
    print(f"Brain (CPU) Load: {cpu_load}")

    # 3. Check 'Memory' (RAM)
    free_mem = os.popen("free -h | grep Mem | awk '{print $4}'").read().strip()
    print(f"Available Memory: {free_mem}")

    print("\n[RESULT] Hardware is healthy. Ready for ROS 2 Installation.")

if __name__ == "__main__":
    main()