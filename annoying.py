import pyautogui, random
pyautogui.FAILSAFE= False
screen_size_x, screen_size_y = pyautogui.size()

def moveMouse():
    xx=0
    while True:
        xx+=1
        print(xx)
        if xx == 50:
            break
        else:
            x = random.randint(0, screen_size_x)
            y = random.randint(0, screen_size_y)
            pyautogui.moveTo(x,y)

value = pyautogui.prompt(text='The answer is up to you', title='"Can I control your computer?"' , default='No')

if value == "Yes":
    moveMouse()
else:
    moveMouse()
