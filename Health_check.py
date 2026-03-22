import psutil 
import time
import os
from datetime import datetime

def clear_screen():
    # Clears the terminal for a clean look
    os.system('cls' if os.name == 'nt' else 'clear')

def get_system_status():
    clear_screen()
    print("="*40)
    print(f" SYSTEM MONITORING - {datetime.now().strftime('%H:%M:%S')}")
    print("="*40)

    # 1. CPU Usage
    cpu = psutil.cpu_percent(interval=1)
    print(f"CPU Usage:    [{cpu}%]")

    # 2. RAM Usage
    memory = psutil.virtual_memory()
    print(f"RAM Usage:    [{memory.percent}%]")

    # 3. Disk Usage
    disk = psutil.disk_usage('/')
    free_gb = disk.free // (1024**3)
    print(f"Free Disk:    [{free_gb} GB]")
    
    # 4. Critical Alerts
    if cpu > 80:
        print("\n[!] ALERT: High CPU Usage Detected!")
    if memory.percent > 90:
        print("\n[!] ALERT: Low Memory Available!")

    print("="*40)
    print("Press Ctrl+C to stop the monitor.")

def main():
    try:
        while True:
            get_system_status()
            # Log data to a file (DevOps Best Practice)
            with open("system_log.txt", "a") as log:
                log.write(f"{datetime.now()}: CPU {psutil.cpu_percent()}% | RAM {psutil.virtual_memory().percent}%\n")
            
            time.sleep(5) # Wait for 5 seconds before next check
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    main()