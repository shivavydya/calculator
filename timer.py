import time
import threading

def countdown_timer(seconds):
    def run_timer():
        nonlocal seconds
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            print(f"{mins:02}:{secs:02}", end='\r')
            time.sleep(1)
            seconds -= 1
        print("Time's up! 🔔🔔🔔")

    t = threading.Thread(target=run_timer)
    t.start()