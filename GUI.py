from wakeonlan import send_magic_packet
from tkinter import *

class RemoteStart:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        
        self.startUp = Button(frame, text = "Wake Up Server", command = self.turnOnServer)
        self.startUp.pack(side = LEFT)
        
        self.close = Button(frame, text = "Closing Prompt", command = frame.quit)
        self.close.pack(side = LEFT)
        
    def turnOnServer(self):
        print("Turning On Server")
        send_magic_packet('xx.xx.xx.xx.xx.xx')
        
root = Tk()
b = RemoteStart(root)
root.mainloop()
        