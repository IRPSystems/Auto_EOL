from time import sleep

import pyautogui

images = {
    "new_serial": "images/new_serial.png",
    "run": "images/run_button.png",
    "serial": "images/serial_field.PNG",
    "mini": "images/min_py.PNG",
    "ok":"images/ok.jpg"
}

def safe_click(image_key, confidence=0.6, retries=3, delay=0.5, ):
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
                sleep(delay)
        print(f"Failed to find {image_key} after {retries} retries.")
    except Exception as e:
        print(f"Error with {image_key}: {e}")
        sleep(1)

        safe_click("file_menu", confidence=0.7)

i=0
x=0
sleep(2)
for i in range (2):
        sleep(3)
        pyautogui.click(x=218,y=298)
        sleep(1)
        #pyautogui.click(pyautogui.move(0, 10))
        pyautogui.typewrite('test'+str(x), interval=0.5)
        x+=1
    	sleep(1)
        pyautogui.click(x=242,y=712)
        sleep(420)
        safe_click("ok", confidence=0.5)
        #pyautogui.click(pyautogui.locateCenterOnScreen(images["ok"], confidence=0.8))
        sleep(20)
        safe_click("ok", confidence=0.5)
        sleep(1200)