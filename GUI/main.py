from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import mousescanner
import mouseplayer


class MainApp(Tk):

    def __init__(self):
        Tk.__init__(self)
        Tk.wm_title(self, 'Syber Recorder')
        Tk.geometry(self, '300x100')
        Record = ttk.Button(self,  text = "Record", command = lambda:self.StartRecord())
        Record.grid(row = 0, column = 0, padx = 20, pady = 10, ipady = 5, ipadx = 5)
        
        Stop = ttk.Button(self, text = "Stop Recording", command = lambda:self.StopRecord())
        Stop.grid(row = 0, column = 1, padx = 20, pady = 10, ipady = 5, ipadx = 5)

        File = ttk.Entry(self, width = 20)
        File.grid(row = 1, column = 0, padx = 20, pady = 10, ipady = 5, ipadx = 5)

        Play = ttk.Button(self, text = "Play", command = lambda:self.Play(File.get()))
        Play.grid(row = 1, column = 1, padx = 20, pady = 10, ipady = 5, ipadx = 5)

    def StartRecord(self):
        global Run
        mousescanner.Record()

    def StopRecord(self):
        Run = False

    def Play(self, name):
        mouseplayer.Play(name)

if __name__ == "__main__":
    Mainapplication = MainApp()
    Mainapplication.mainloop()
        
