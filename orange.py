import time
import os

while True:
    os.system("cls" if os.name == 'nt' else 'clear')
    current_time = time.strftime("%H:%M:%S")
    print("CURRENT TIME: " + current_time)
    time.sleep(1)