import pyautogui
import time

def get_mouse_position():
    """Print the current pointer position."""
    while True:
        x, y = pyautogui.position()
        print(f"Mouse Position: X={x}, Y={y}", end="\r")  # Overwrites the previous line
        time.sleep(0.5)  # Update every 0.5 seconds

if __name__ == "__main__":
    print("Move your mouse to the desired position and note the coordinates.")
    get_mouse_position()
