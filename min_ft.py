import time
import pyautogui

# Dictionary containing paths to the images
images = {
    "new_serial": "images/new_serial.png",
    "run": "images/run_button.png",
    "serial": "images/serial_field.PNG",
    "mini": "images/min_py.PNG",
    "x": "images/x.jpg"
}

def safe_click(image_key, confidence=0.6, retries=2, delay=0.5):
    """Tries to locate an image on the screen and click on it."""
    try:
        image = images[image_key]
        for _ in range(retries):
            location = pyautogui.locateCenterOnScreen(image, confidence=confidence)
            if location:
                pyautogui.click(location)
                print(f"Clicked on {image_key}")
                return
            else:
                print(f"{image_key} not found, retrying...")
                time.sleep(delay)
        print(f"Failed to find {image_key} after {retries} retries.")
    except Exception as e:
        print(f"Error with {image_key}: {e}")
        time.sleep(1)

i = 0
x = 1
time.sleep(2)

for i in range(10):
    time.sleep(3)
    # Use the correct key name from the dictionary, not a direct path
    safe_click("new_serial")

    # Move the cursor slightly and click (or remove this if unnecessary)
    pyautogui.move(0, 10)
    pyautogui.click()

    pyautogui.typewrite('test' + str(x), interval=0.5)
    x += 1
    # need to add output button at the end of test
    #  pyautogui.click(pyautogui.locateCenterOnScreen(images["run"], confidence=0.8))

    # time.sleep(1800)

