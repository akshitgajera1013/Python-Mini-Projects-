import time
from plyer import notification

while True:
    print("Please sip some water")
    notification.notify(
        title="Reminder",
        message="You Need To Drink Some Water!!!",
        timeout=2  # Notification stays for 10 seconds
    )
    time.sleep(3)  # Remind every 30 minutes (change as needed)