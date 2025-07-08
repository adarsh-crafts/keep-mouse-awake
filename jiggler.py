import pyautogui
import random
import time

def move_mouse_randomly(interval=10, move_range=20):
    print("Starting mouse jiggler. Press Ctrl+C to stop.")
    try:
        while True:
            # Get current mouse position
            x, y = pyautogui.position()
            # Move to a new random nearby location
            dx = random.randint(-move_range, move_range)
            dy = random.randint(-move_range, move_range)
            pyautogui.moveTo(x + dx, y + dy, duration=0.2)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMouse jiggler stopped.")

if __name__ == "__main__":
    move_mouse_randomly()
