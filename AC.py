#Import All From tkinter module
from tkinter import *
# message box import from tkinter
from tkinter import messagebox
# imported time for clock
import time
# imported datetime for hours and minutes
import datetime
# imported pillow module for images
from PIL import ImageTk, Image
# imported winsound to use sound from system for alarm clock
import winsound
from playsound import playsound

# defined tick function.
# passed a parameter name as clk
def tick(clk):
    global clock
    # window is created
    window = Toplevel()
    #Created window with dimensions 300x130.
    window.geometry("300x130")
    clock = Label(window, font=('Helvetica', 30, "bold"), fg="light green", bg="black", bd=16, relief=SUNKEN)
    clock.place(x=18, y=30)
    # used Conditional Statement.
    if clk == "btn_24":
        #Runs 24 hrs clock
        time24()
    elif clk == "btn_12":
        # Runs 12 hrs clock
        time12()
    else:
        # Runs Alarm clock
        alarm()


def time24():
    global clock
    # used strftime which returns string with date and time
    # H = hours in 24 , M = minutes, S= seconds
    ts = time.strftime("%H:%M:%S")
    clock["text"] = ts
    # clock loops after every 1000 miliseconds which is 1 second.
    clock.after(1000, time24)


def time12():
    global clock
    # used strftime which returns string with date and time
    # H = Hour (12-hour clock) , M = minutes, S= seconds , p= Am or Pm (when used in 12 hr clock)
    ts = time.strftime("%I:%M:%S:%p")
    clock["text"] = ts
    # clock loops after every 1000 miliseconds which is 1 second.
    clock.after(1000, time12)


def alarm():
    global e1, e2
    window = Toplevel()
    window.geometry("350x200")
    hours = Label(window, text=" Enter Hours !\n (0-23 hrs)",font=('Helvetica', 12, "bold"))
    hours.place(x=30, y=20)
    # Entry widget is used to provde the single line text-box to the user to accept a value from the user.
    e1=Entry(window)
    # placing the entry widget
    e1.place(x=30, y=70)
    minutes=Label(window, text="Minute's (00-59 min)", font=('Helvetica', 12, "bold"))
    minutes.place(x=30, y=100)
    e2=Entry(window)
    e2.place(x=30, y=130)
    #seconds = Label(window, text="second's (00-59 min)", font=('Helvetica', 12, "bold"))
    #seconds.place(x=30, y=100)
    #e3 = Entry(window)
    #e3.place(x=30, y=130)
    begin=Button(window, text="Start", relief=GROOVE)
    begin.place(x=200, y=150)
    begin.bind("<Button-1>", alarm_begin)


def alarm_begin(event):
    global e1,e2
    # object h gets the user inputed value
    h=e1.get()
    # object m gets the user inputed value
    m=e2.get()
    #s=e3.get()
    while(True):
        set_alarm_time = f"{e1.get()}:{e2.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
        # if user inputed time and system sound match loops exits.
        if (int(h)==datetime.datetime.now().hour and int(m)==datetime.datetime.now().minute):
            # plays sound when time matches.
            winsound.PlaySound("Alarm_Clock.wav",winsound.SND_ASYNC)
            # pops new window to alert user
            messagebox.showinfo("Alarm", "Time's up!")
            break

# Object Created as root to use Tkinter Module.
root = Tk()
# Title of window.
root.title("Digital and Alarm Clock")
#Created window with dimensions 550x400.
root.geometry("550x400")
# Usung PIL Module import image's.
img1 = PhotoImage(file="12 hour.png")
img2 = PhotoImage(file="24 hour.png")
img3 = PhotoImage(file="Alarm_Clock.png")

# Text used as header of window.
text = Label(root, text="Which Clock Do You Wish To Prefer?", font=("Helvetica", 20, "bold"), fg="dark red")
text.place(x=80, y=20)

# Button Created using tkinter,Image merged on button,Button are Curved using borderwidth=0
#Tick function is used to run the clock
btn1 = Button(root, image=img1, borderwidth=0, command=lambda: tick("btn_12")).place(anchor=SW, x=0, y=200)
btn2 = Button(root, image=img2, borderwidth=0, command=lambda: tick("btn_24")).place(anchor=SW, x=0, y=300)
btn3 = Button(root, image=img3, borderwidth=0, command=alarm).place(anchor=SW, x=0, y=400)

# Imported Image (Show's Beside Button)
photo = ImageTk.PhotoImage(Image.open("Digital_Clock1.png"))

# Using image in tkinter and placing it as required
img_label = Label(root, image=photo)
img_label.place(x=230, y=140)


# Looping it(runs infinitely)
root.mainloop()
