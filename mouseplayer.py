import ast
import pyautogui
import time

f = open('temp.txt','r')
reader = " "
while reader != "":
    try:
        for i in range (10):
            if reader[0:1] != "R" or reader[0:1] != "L":
                reader = f.readline()
                timer = ast.literal_eval(f.readline())
                print(reader)
        Pos = ast.literal_eval(reader[1:999])
        print(Pos)
        pyautogui.moveTo(Pos[0],Pos[1], 3,pyautogui.easeInElastic)
        if reader[0:1] == "R":
            time.sleep(0.1)
            pyautogui.click(Pos[0], Pos[1], clicks=1, interval=0, button='right')
        elif reader[0:1] == "L":
            time.sleep(0.1)
            pyautogui.click(Pos[0], Pos[1], clicks=1, interval=0, button='left')
        time.sleep(timer)


        reader = " "
    except KeyboardInterrupt:
        break
    except SyntaxError:
        break
