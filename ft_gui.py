import os
import subprocess
import time
import pyautogui
from time import sleep

from pyautogui import click


desktop_path = os.path.join("C:\\Users", os.getlogin(), "Desktop")
report_dir = os.path.join(desktop_path, "Report")
print(report_dir)
if not os.path.exists(report_dir):
    os.makedirs(report_dir)
    print(f"Created 'Report' directory at {report_dir}")
else:
    print("'Report' directory already exists.")
images = {
    "FT": "images/ft_image.png",
    "run": "images/run_button.png",
    "admin": "images/admin_mode.PNG",
    "ate_checkbox": "images/ate_box.JPG",
    "comm": "images/comm.PNG",
    "connect": "images/connect_button.PNG",
    "eol": "images/eol_image.PNG",
    "file_menu": "images/file_menu.PNG",
    "maxSize": "images/maxSize_button.PNG",
    "ok": "images/ok_button.PNG",
    "operator": "images/operator_field.PNG",
    "part": "images/part_field.PNG",
    "rack": "images/rack_nmb.JPG",
    "report": "images/test.png",
    "save": "images/save_btn.jpg",
    "serial": "images/serial_field.PNG",
    "settings": "images/settings.PNG",
    "skip_ignore": "images/skip_ignore.jpg",
    "mini": "images/min_py.PNG",
    "tools": "images/tools_btn.jpg",
    "other": "images/other.jpg",
    "x":"images/x.jpg"
}
sleep(1)
#Function to safely click on an image, with retries
def safe_click(image_key, confidence=0.8, retries=2, delay=0.5, ):
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
pyautogui.click(pyautogui.locateCenterOnScreen(images["mini"], confidence=0.8))  # Click on "minimaze"
sleep(1)

pyautogui.click(pyautogui.locateCenterOnScreen(images["FT"], confidence=0.8))  # Click on "minimaze"
sleep(1)

# # Attempt to click on "maxSize" button, with error handling
# safe_click("maxSize", confidence=0.8)p a

# Open the file menu
safe_click("file_menu", confidence=0.7)
sleep(2)
# Click on "admin" mode
#safe_click(pyautogui.move(0, 10))
safe_click("admin", confidence=0.7)

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
sleep(2)
#find and clik tools

pyautogui.click(pyautogui.locateCenterOnScreen(images["tools"], confidence=0.8))
sleep(1)

#find and clik settings
pyautogui.click(pyautogui.locateCenterOnScreen(images["settings"], confidence=0.8))
sleep(2)
#find and fill in reports path
pyautogui.locateCenterOnScreen("report", confidence=0.1)
sleep(2)
#pyautogui.click(pyautogui.move(0, 10))
# pyautogui.typewrite(report_dir, interval=0.5)
# sleep(1)
#click on the Save button
safe_click(pyautogui.locateCenterOnScreen(images["save"]))
sleep(1)

pyautogui.click(pyautogui.locateCenterOnScreen(images["other"], confidence=0.5))
sleep(1)
pyautogui.click(pyautogui.locateCenterOnScreen(images["skip_ignore"], confidence=0.8))

pyautogui.click(pyautogui.locateCenterOnScreen(images["rack"], confidence=0.8))
pyautogui.click(pyautogui.move(2,0 ))
pyautogui.typewrite('test', interval=0.5)

sleep(1)
pyautogui.click(pyautogui.locateCenterOnScreen(images["comm"], confidence=0.8))
sleep(1)
pyautogui.click(pyautogui.locateCenterOnScreen(images["ate_checkbox"], confidence=0.8))
sleep(1)
#pyautogui.click(pyautogui.locateCenterOnScreen(images["connect"], confidence=0.8))
sleep(1)
pyautogui.click(pyautogui.locateCenterOnScreen(images["x"], confidence=0.8))
sleep(2)

pyautogui.click(pyautogui.locateCenterOnScreen(images["run"], confidence=0.8))


i=0
x=0
for i in range (10):
        time.sleep(3)
        pyautogui.click(pyautogui.locateCenterOnScreen(images["serial"], confidence=0.8))
        sleep(1)
        pyautogui.click(pyautogui.move(0, 10))
        pyautogui.typewrite('test'+x, interval=0.5)
        x+=1
        pyautogui.click(pyautogui.locateCenterOnScreen(images["run"], confidence=0.8))
        time.sleep(1800)