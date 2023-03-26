#!/usr/bin/python3
import os
import time
from plyer import notification

def notify(message):

    notification.notify(
    title = "Pomodoro Effect",
    message=message ,
    timeout=2)
    # waiting time
    time.sleep(1)

count_in_secs = 0
while True:
    count_in_secs += 1
    time.sleep(1)
    if count_in_secs == 1800:
        print("Timer : " + str(count_in_secs))
        notify("Time to take a break")
        count_in_secs = 0
        time.sleep(100)
