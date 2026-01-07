## 1. CPU & Memory Monitor, Write a script that: Displays CPU usage and memory usage every 5 seconds, Stops after 1 minute

import psutil
import time 

def cpu_uage_get():
    thershold = int(input("enter the thershold of the CPU: "))

    cpu_usage = psutil.cpu_percent(interval=1)
    sleep = time.sleep(5)

    if cpu_usage >= thershold: 
        print("CPU usage is high")
    else: 
        print("Safe")


def memory_usage_get():

    memory_usage = psutil.virtual_memory().percent
    sleep = time.sleep(5)

    print(memory_usage)  

cpu_uage_get()
memory_usage_get()
