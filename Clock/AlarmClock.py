import time

alarm_time = input("Set the alarm time (HH:MM:SS): ")
while True:
    current_time = time.strftime("%H:%M:%S")
    if current_time == alarm_time:
        print("Alarm! Wake up!")
        break
    time.sleep(1)