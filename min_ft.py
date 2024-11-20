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
import time

# Start the timer
start_time = time.time()
def counter():
    try:
        while True:
            # Calculate the elapsed time
            elapsed_time = int(time.time() - start_time)

            # Format the elapsed time as HH:MM:SS
            hours = elapsed_time // 3600
            minutes = (elapsed_time % 3600) // 60
            seconds = elapsed_time % 60

            # Display the timer in the terminal
            print(f'\rTimer: {hours:02}:{minutes:02}:{seconds:02}', end='')

            # Wait for 1 second before updating
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nTimer stopped.")



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
t = 0
time.sleep(2)

for i in range(10):
    time.sleep(3)
    pyautogui.click(x=51, y=108 )

    pyautogui.typewrite('test-' + str(t), interval=0.5)
    t += 1
    #counter()
   # pyautogui.move(0, 10)
    # pyautogui.click()
    #  pyautogui.click(pyautogui.locateCenterOnScreen(images["run"], confidence=0.8))
    time.sleep(0.5)
    pyautogui.click(x=79, y=941)
    print("clicked")
    time.sleep(120)
    pyautogui.click(x=1205, y=645)
    print("clicked")
    time.sleep(120)

