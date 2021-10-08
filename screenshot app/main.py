import time
import pyautogui

def screenshot():
    name = int(round(time.time() * 1000))
    #geting time and multipy it with 1000 and use it as name
    #this will prevent you from overwriting the corrent screenshot
    name = 'screenshot_files/{}.png'.format(name)
    #giving a specific folder for saving the files
    #take the time and add .png extension
    time.sleep(5)  
    #adding a delay of 5 seconds
    img = pyautogui.screenshot(name)  
    #built in fn for making screenshot using pyautogui
    img.show()  
    #Showing the screenshot taken 

screenshot()

