#importing tkinter module
from tkinter import *
root = Tk()
#setting root title
root.title("Stopwatch")
#setting root icon 
root.iconbitmap('stopwatch.ico') 
root.geometry("300x250")   #setting root geometry
#fixing root size after this the root is not resizable
root.resizable(0,0)
#cretng variable which are used in program   
running = False
counter = -1

#function to start counting
def count(label1):
    def display():
        if running:
            global counter
            if counter == -1:
                label1['text'] = "Starting..."
                
            else:
                screen = str(counter)
                label1['text'] = screen
            label1.after(1000,display)
            counter = counter+1
    display()
        
#function to start stopwatch 
# It executes when start button is pressed
def Start(label1):
    global running
    running = True
    count(label1)
    bstart['state']='disabled'
    bstop['state']='normal'

#function to stop stopwatch 
# It executes when stop button is pressed
def Stop():
    global running
    running = False
    bstart['state'] = 'normal'
    bstop['state'] = 'disable'
    breset['state'] = 'normal'

#function to reset the stopwatch 
# It executes when reset button is pressed
def Reset(label1):
    global counter
    counter = -1
    if running:
        breset['state'] = 'disabled'
        label1['text'] = "Starting..."
    else:
        label1['text'] = "Welcome!!!"

#creating label of the root window
label1 = Label(root,
    text = "Welcome!!", 
    font = ("Verdana", 25),
    background = "#ffffff",
    fg = "#000000",
)
#packing label
label1.pack(expand = True,fill = BOTH)

#Creating Frame in root window
frame1 = Frame(root)
#packing frame
frame1.pack(expand = True,fill = BOTH)
#Creating start button
bstart = Button(frame1,font =("Verdana",20),text = "Start",command = lambda:Start(label1))
bstart.pack(expand = True,fill = BOTH)

#creating stop button
bstop = Button(frame1,font =("Verdana",20),state = 'disabled',text = "Stop",command = Stop)
bstop.pack(expand = True,fill = BOTH)

#creating reset button
breset = Button(frame1,font =("Verdana",20),state = 'disabled', text = "Reset",command = lambda:Reset(label1))
breset.pack(expand = True,fill = BOTH)

root.mainloop()