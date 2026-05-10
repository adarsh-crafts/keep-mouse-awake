import pyautogui
import time
from datetime import datetime, timedelta

def click_every_5_minutes(run_hours=None):
    if run_hours is not None:
        print(f"Starting clicker. Will run for {run_hours} hour(s). Press Ctrl+C to stop early.")
        end_time = datetime.now() + timedelta(hours=run_hours)
    else:
        print("Starting clicker with no time limit. Press Ctrl+C to stop.")

    try:
        while True:
            if run_hours is not None and datetime.now() >= end_time:
                print(f"Finished clicking after {run_hours} hour(s).")
                break

            pyautogui.click()
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"{current_time}: Clicked at current position.")
            time.sleep(300)  # 5 minutes
    except KeyboardInterrupt:
        print("Stopped by user.")

# --- USAGE ---

# Default behavior (infinite loop)
click_every_5_minutes()

# Or, to run for a specific number of hours:
# click_every_5_minutes(run_hours=2.5)  # For 2 hours 30 minutes
