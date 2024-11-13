import subprocess
import time
import pyautogui
from time import sleep

from first_test import path_report

#from main import  base_dir

images = {
    "FT": "images/ft_image.png",
    "run": "images/run_button.png",
    "admin": "images/admin_mode.PNG",
    "ate_checkbox": "images/ate_checkbox.PNG",
    "comm": "images/comm.PNG",
    "connect": "images/connect_button.PNG",
    "eol": "images/eol_image.PNG",
    "file_menu": "images/file_menu.PNG",
    "maxSize": "images/maxSize_button.PNG",
    "ok": "images/ok_button.PNG",
    "operator": "images/operator_field.PNG",
    "part": "images/part_field.PNG",
    "rack": "images/rack_number.PNG",
    "report_patch": "images/report_patch.PNG",
    "save": "images/save_button.PNG",
    "serial": "images/serial_field.PNG",
    "settings": "images/settings.PNG",
    "skip_ignore": "images/skip_ignore_box.PNG",
    "minimaze": "images/min_py.PNG",
    "tools": "images/tools.PNG"
}

#Function to safely click on an image, with retries
def safe_click(image_key, confidence=0.8, retries=2, delay=1):
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

# Start the script
pyautogui.click(pyautogui.locateCenterOnScreen(images["minimaze"], confidence=0.8))  # Click on "minimaze"
sleep(1)

# Attempt to click on "maxSize" button, with error handling
safe_click("maxSize", confidence=0.8)

sleep(2)
# Open the file menu
safe_click("file_menu", confidence=0.7)

# Click on "admin" mode
safe_click("admin", confidence=0.8)
sleep(1)

# Type in 'irp ate' into the input field
pyautogui.typewrite('irp ate', interval=0.5)
sleep(3)

# Click the OK button
safe_click("ok", confidence=0.8)

#find and fill in serial number field
pyautogui.click(pyautogui.locateCenterOnScreen(images["serial"], confidence=0.8))  # Click on "minimaze"
sleep(1)
pyautogui.click(pyautogui.move(0, 10))
pyautogui.typewrite('test', interval=0.5)

#find and fill in part number field
pyautogui.click(pyautogui.locateCenterOnScreen(images["part"], confidence=0.8))
sleep(1)
pyautogui.click(pyautogui.move(0, 10))
pyautogui.typewrite('test', interval=0.5)

#find and fill in operator name
pyautogui.click(pyautogui.locateCenterOnScreen(images["operator"], confidence=0.8))
sleep(1)
pyautogui.click(pyautogui.move(0, 10))
pyautogui.typewrite('test', interval=0.5)

#find and clik tools
safe_click(pyautogui.locateCenterOnScreen(images["tools"]))

#find and clik settings
safe_click(pyautogui.locateCenterOnScreen(images["settings"]))

#find and fill in reports path
pyautogui.click(pyautogui.locateCenterOnScreen(images["report_patch"], confidence=0.8))
sleep(1)
pyautogui.click(pyautogui.move(0, 10))
pyautogui.typewrite(path_report, interval=0.5)
sleep(1)
#click on the Save button
safe_click(pyautogui.locateCenterOnScreen(images["save"]))




