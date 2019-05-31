import ast
import pyautogui
import time




def Play(File):
    pyautogui.FAILSAFE = False
    f = open((File+".txt"),'r')
    reader = " "
    while reader != "":
        try:
            for i in range (5):
                if reader[0:1] != "R" or reader[0:1] != "L":
                    reader = f.readline()
                    timer = ast.literal_eval(f.readline())
                    print(reader)
            Pos = ast.literal_eval(reader[1:999])
            print(Pos)
            pyautogui.moveTo(Pos[0],Pos[1],timer)
            if reader[0:1] == "R":
                time.sleep(0.1)
                pyautogui.click(Pos[0], Pos[1], clicks=1, interval=0, button='right')
            elif reader[0:1] == "L":
                time.sleep(0.1)
                pyautogui.click(Pos[0], Pos[1], clicks=1, interval=0, button='left')
            #time.sleep(timer/2)


            reader = " "
        except KeyboardInterrupt:
            break
        except SyntaxError:
            break

if __name__ == "__main__":
    Play('Temp')
