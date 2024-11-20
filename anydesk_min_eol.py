from time import sleep

import pyautogui



i=0
x=0
sleep(2)
for i in range (30):
        sleep(3)
        pyautogui.click(x=218,y=298)
        sleep(1)
       
        pyautogui.typewrite('test-'+str(x), interval=0.5)
        x+=1
    
        pyautogui.click(x=242,y=712)
        
        #pyautogui.click(x=665,y=558)
        sleep(850)
        #ok button location looking for firmware
        pyautogui.click(x=877,y=620)
        print("Ok button")        
        sleep(90)
        
        #ok button location 
        pyautogui.click(x=878,y=618)
        print("Clicked")
        sleep(1200)