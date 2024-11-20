from time import sleep, time
import pyautogui

i = 0
x = 0
sleep(2)

# Function to display a countdown timer
def countdown_timer(duration):
    while duration > 0:
        print(f"Time remaining: {duration} seconds", end="\r")
        sleep(1)
        duration -= 1

for i in range(30):
    sleep(3)
    #pyautogui.click(x=218, y=298)
    pyautogui.click(x=188, y=345)
    sleep(2)
    pyautogui.typewrite('test-' + str(x), interval=0.5)
    x += 1

    pyautogui.click(x=242, y=712)

    # Timer before next step (800 seconds)
    print("Test started\n")
    countdown_timer(800)
    print("The test is over")
    
    # OK button location (looking for firmware)
    pyautogui.click(x=877, y=669)
    print("Ok button\n")

    # OK button location
    pyautogui.click(x=878, y=618)
    print("Waiting for the next test")
    countdown_timer(1200)  # Timer for 1200 seconds
