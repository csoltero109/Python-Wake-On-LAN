from wakeonlan import send_magic_packet
from tkinter import *

class RemoteStart:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        frame.place(x=0, y=0, anchor="nw", width=w, height=h)
        frame.configure(bg = "blue")
        
        self.startUp = Button(frame, text = "Wake Up Server", command = self.turnOnServer)
        self.startUp.place(x=w*(1/4), y=h*(1/4))

        self.startGameUp = Button(frame, text = "Wake Up Main Rig", command = self.turnOnGamingRig)
        self.startGameUp.place(x=w*(1/4), y=h*(3/4))

        self.close = Button(frame, text = "Exit", command = exit)
        self.close.place(x=w*(3/4), y=h*(2/4))


    def turnOnServer(self):
        print("Turning On Server")
        #send_magic_packet('xx.xx.xx.xx.xx.xx')
    def turnOnGamingRig(self):
        print("Turning On Gaming Rig")
        #send_magic_packet('xx.xx.xx.xx.xx.xx')
    def exit(event):
        print("Turning off GUI")
        root.quit()
        

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.title("Wake-On-LAN")
root.configure(bg ="#002259")
b = RemoteStart(root)
root.mainloop()
        
