import time

import pyautogui

images = {
    "new_serial": "images/new_serial.png",
    "run": "images/run_button.png",
    "serial": "images/serial_field.PNG",
    "mini": "images/min_py.PNG",
    "x":"images/x.jpg"
}

def safe_click(image_key, confidence=0.6, retries=2, delay=0.5, ):
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

        safe_click("file_menu", confidence=0.7)

i=0
x=0
time.sleep(2)
for i in range (10):
        time.sleep(3)
        pyautogui.click(pyautogui.locateCenterOnScreen(r"C:\Users\ilyar\Pictures\new_serial.PNG", confidence=0.4))
        time.sleep(1)
        pyautogui.click(pyautogui.move(0, 10))
        pyautogui.typewrite('test'+str(x), interval=0.5)
        x+=1
        #  pyautogui.click(pyautogui.locateCenterOnScreen(images["run"], confidence=0.8))
        #need to add ok button error twice
        # time.sleep(1800)