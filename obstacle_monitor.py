#!/usr/bin/env python3
import os
import time

def main():
    print("--- ROBOT PROXIMITY MONITOR ---")
    
    # In a real robot, we would use 'ros2 topic echo' 
    # Here, we simulate checking the 'X' coordinate from the system
    
    try:
        for i in range(10):
            # Simulating a distance check
            distance_to_wall = 10 - i 
            
            if distance_to_wall > 3:
                print(f"[SAFE] Distance to wall: {distance_to_wall}m")
            else:
                print(f"[WARNING] Obstacle detected! Distance: {distance_to_wall}m")
                print("!!! TRIGGERING AUTO-BRAKE !!!")
                break
                
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nMonitor stopped by Pilot.")

if __name__ == "__main__":
    main()