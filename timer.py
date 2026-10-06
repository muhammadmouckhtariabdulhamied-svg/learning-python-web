import time
import os

while True:
    os.system("cls" if os.name == 'nt' else 'clear')
    current_time = time.strftime("%H:%M:%S")
    print("CURRENT TIME: " + current_time)
    time.sleep(1)
    if current_time == "11:53:06":  # adjust this to your desired alarm time
        print("ALARM!")
        os.system("over the horizon")  # adjust this to your desired alarm sound
        time.sleep(10)  # adjust this to the length of the alarm

