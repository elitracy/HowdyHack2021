from tkinter import *
import tkinter as tk
import clipFunctions as cf
import pydub as dub

gui = Tk(className="mainWindow")
gui.geometry("900x500")

# T = Text(gui, height = 5, width = 52) #create text "div"

l = Label(gui, text = "This is the Label")
l.config(font = ("Arial", 15))

audioClips = ["cantina.wav","cantina.wav"]
playButtons = []

# cf.playAudio(dub.AudioSegment.from_wav(audioClips[0]))

for a in audioClips:
    clip = dub.AudioSegment.from_wav("./audioFiles/" + a)
    playButtons.append(Button(gui, text = a[:-4], command = lambda: cf.playAudio(clip)))

b2 = Button (gui, text = "Exit", command = gui.destroy) #closes window

#add elements to window
l.pack()
# T.spack()
b2.pack()

for b in playButtons:
    b.pack(side=tk.LEFT)

# T.insert(tk.END,)

gui.mainloop()