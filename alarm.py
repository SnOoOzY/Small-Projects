from tkinter import *
import datetime
import time
import winsound


# main loop

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


# GUI

clock = Tk()

clock.title("Swagger Alarm Clock")
clock.geometry("400x200")
time_format = Label(clock, text = "Hour    Min    Sec", font = 60).place(x = 110)
setYourAlarm = Label(clock, text = "Time", fg = "blue", relief = "solid", font = ("Heleventica", 7, "bold")).place(x = 295, y = 30)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(clock, textvariable = hour, bg = "pink", width = 15).place(x=110, y=30)
minTime = Entry(clock, textvariable = min, bg = "pink", width = "15").place(x=150, y=30)
secTime = Entry(clock, textvariable = sec, bg = "pink", width = "15").place(x=200, y=30)

submit = Button(clock, text = "Set Alarm", fg = "red", width = 10, command = actual_time).place(x = 110, y=70)

clock.mainloop()