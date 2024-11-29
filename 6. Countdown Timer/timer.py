from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time

clo = Tk()
clo.geometry("350x300")
clo.title("Countdown Timer")
clo.config(bg ="hot pink")
clo.resizable(0,0)

hour=StringVar()
minute=StringVar()
second=StringVar()

hour.set("00")
minute.set("01")
second.set("00")

L1 = Label(clo, text= "Countdown Timer",font=("Baskerville Old Face",25,"bold"))
L1.config(bg= "hot pink",fg = 'black')
L1.place(x=50,y = 15)

hourEntry= Entry(clo, width=2, font=("Impact",50,""),textvariable=hour)
hourEntry.place(x=50,y=80)
  
minuteEntry= Entry(clo, width=2, font=("Impact",50,""),textvariable=minute)
minuteEntry.place(x=140,y=80)
  
secondEntry= Entry(clo, width=2, font=("Impact",50,""),textvariable=second)
secondEntry.place(x=230,y=80)

def submit():
    try:
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
        mins,secs = divmod(temp,60) 
        hours=0
        if mins >60:
             hours, mins = divmod(mins, 60)
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        clo.update()
        time.sleep(1)

        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
        temp -= 1
        
btn = Button(clo, text='Set Time Countdown',font=("Goudy Old Style",20,"bold"), bd='5',command= submit)
btn.place(x = 40,y = 190)

clo.mainloop()




