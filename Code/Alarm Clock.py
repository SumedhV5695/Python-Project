import os
from tkinter import *
from tkinter import messagebox  # (message is module not a class)
import time
import datetime
from playsound import playsound
from PIL import ImageTk, Image
import winsound


def tick(val):
    global clock
    window = Toplevel()
    window.geometry("300x130")
    clock = Label(window, font=('Helvetica', 30, "bold"), fg="light green", bg="black", bd=16, relief=SUNKEN)
    clock.place(x=18, y=30)
    if val == "btn_24":
        time24()
    elif val == "btn_12":
        time12()
    else:
        alarm()


def time24():
    global clock
    ts = time.strftime("%H:%M:%S")
    clock["text"] = ts
    clock.after(1000, time24)


def time12():
    global clock
    ts = time.strftime("%I:%M:%S:%p")
    clock["text"] = ts
    clock.after(1000, time12)


def alarm():
    global e1, e2
    window = Toplevel()
    window.geometry("350x200")
    hours = Label(window, text="At what hour do u want to ring?\n Please Enter military Time", bg="white", bd=16, relief=SUNKEN)
    hours.place(x=30, y=20)
    e1=Entry(window, relief=GROOVE)
    e1.place(x=30, y=70)
    minutes=Label(window, text="At what minute do u want to ring?", font=('Helvetica', 12, "bold"))
    minutes.place(x=30, y=100)
    e2=Entry(window, relief=GROOVE)
    e2.place(x=30, y=130)
    begin=Button(window, text="Start", relief=GROOVE)
    begin.place(x=200, y=150)
    begin.bind("<Button-1>", alarm_begin)


def alarm_begin(event):
    global e1,e2
    h=e1.get()
    m=e2.get()
    while(True):
        if (int(h)==datetime.datetime.now().hour and int(m)==datetime.datetime.now().minute):
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            messagebox.showinfo("Alarm", "Time's up!")
            break


root = Tk()
root.geometry("550x400")
# img=cv2.imread('image1.png')
# cv2.imwrite("image1.png",img)
img1 = PhotoImage(file="12 hour.png")
img2 = PhotoImage(file="24 hour.png")
img3 = PhotoImage(file="Alarm_Clock.png")

text = Label(root, text="Which Clock Do You Wish To Prefer?", font=("Helvetica", 20, "bold"), fg="dark red")
text.place(x=80, y=20)

btn1 = Button(root, image=img1, borderwidth=0, command=lambda: tick("btn_12")).place(anchor=SW, x=0, y=200)
btn2 = Button(root, image=img2, borderwidth=0, command=lambda: tick("btn_24")).place(anchor=SW, x=0, y=300)
btn3 = Button(root, image=img3, borderwidth=0, command=alarm).place(anchor=SW, x=0, y=400)

photo = ImageTk.PhotoImage(Image.open("Digital_Clock.png"))


img_label = Label(root, image=photo)
img_label.place(x=230, y=140)



root.mainloop()
