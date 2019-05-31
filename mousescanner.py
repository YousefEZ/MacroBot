import pyautogui
import win32api
import time


pos1 = pyautogui.position()
save = ""
state_left = win32api.GetKeyState(0x01)
state_right = win32api.GetKeyState(0x02)
t = 0
Timer = False
while True:
    try:
        a = win32api.GetKeyState(0x01)
        b = win32api.GetKeyState(0x02)
        pos = pyautogui.position()
        
        if a != state_left:  # Button state changed
            state_left = a
            print('Left Button Pressed')
            t1 = time.time()
            save = str(save) + "L" + str(pos) + "\n"
            save = str(save) + "{:.2f}".format(t1-t2) + "\n"
            print("{:.2f}".format(t1-t2))
            Timer = False

                
        elif b != state_right:
            state_right = b
            print('Right Button Pressed')
            t1 = time.time()
            save = str(save) + "R" + str(pos) + "\n"
            save = str(save) + "{:.2f}".format(t1-t2) + "\n"
            print("{:.2f}".format(t1-t2))
            Timer = False

        
        elif pos != pos1:
            print(pos)
            pos1 = pos
            t1 = time.time()
            save = str(save) + "N" + str(pos1) + "\n"
            save = str(save) + "{:.2f}".format(t1-t2) + "\n"
            print("{:.2f}".format(t1-t2))
            Timer = False

        elif pos == pos1 and Timer is not True:
            t2 = time.time()
            Timer = True
            


    except KeyboardInterrupt:
        print ('')
        f = open('temp.txt','w')
        f.write(save)
        f.close()
