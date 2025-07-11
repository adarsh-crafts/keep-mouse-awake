import pyautogui
import random
import time

def move_mouse_randomly(interval=10, move_range=20):
    print("Starting mouse jiggler. Press Ctrl+C to stop.")
    
    # Get screen size
    screenWidth, screenHeight = pyautogui.size()

    try:
        while True:
            # Get current mouse position
            x, y = pyautogui.position()

            # Generate a small random offset
            dx = random.randint(-move_range, move_range)
            dy = random.randint(-move_range, move_range)

            # Compute new coordinates safely, avoiding screen edges
            new_x = min(max(1, x + dx), screenWidth - 2)
            new_y = min(max(1, y + dy), screenHeight - 2)

            # Move mouse to new position
            pyautogui.moveTo(new_x, new_y, duration=0.2)

            # Wait before next move
            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nMouse jiggler stopped.")

if __name__ == "__main__":
    move_mouse_randomly()
