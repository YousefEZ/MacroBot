import pyautogui
import win32api
import time
from tkinter import ttk
from tkinter import *
from tkinter import messagebox




class confirm(Tk):
    def __init__(self):
        Tk.__init__(self)
        Tk.wm_title(self, 'Saved!')
        Tk.geometry(self, '225x125')
        Label = ttk.Label(self, text = "Saved successfully").grid(row = 0, column = 0, padx = 60, pady = 15)
        Button2 = ttk.Button(self, text = "Exit", command = lambda:self.destroy()).grid(row = 1, column = 0, padx = 60, pady = 15)


        

class SaveWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        Tk.wm_title(self, 'Save File')
        Tk.geometry(self, '400x100')
        Label = ttk.Label(self, text = 'Save Name:').grid(row = 0, column = 0,padx = 15, pady = 2)
        Save = ttk.Entry(self, width = 30)
        Save.grid(row = 0, column = 1, padx = 40, pady = 15)
        Submit = ttk.Button(self, text = "Save", command = lambda:self.savefile(str(Save.get())))
        Submit.grid(row = 1, column = 1, padx = 30, pady = 2)

    def savefile(self, name):
        global savename
        savename = name + ".txt"
        self.quit()
        

def Record():
    global Run
    Run = True
    pos1 = pyautogui.position()
    pyautogui.FAILSAFE = True
    save = ""
    state_left = win32api.GetKeyState(0x01)
    state_right = win32api.GetKeyState(0x02)
    t = 0
    Timer = False
    while Run:
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

        if pos[0] == 0 and pos[1] == 0:
            Run = False
                
    getname = SaveWindow()
    getname.mainloop()
    f = open(savename,'w')
    f.write(save)
    f.close()
    getname.destroy()
    x = confirm()


if __name__ == "__main__":
    Record()
