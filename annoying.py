import pyautogui, random, time, os
pyautogui.FAILSAFE= False


screen_size_x, screen_size_y = pyautogui.size()

def mauseHaraket():
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





pyautogui.confirm(text='', title='', buttons=['OK', 'Cancel'])

deneme = pyautogui.prompt(text='Yaz yoksa virüs bilgisayarını sıfırlar', title='"Hakkımı helal ediyorum" yazmalısın!' , default='Etmiyorum')


if deneme == "Hakkımı helal ediyorum":
    pass
else:
    mauseHaraket()












