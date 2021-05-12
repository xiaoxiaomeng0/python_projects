from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repo = 0
timer = None

window = Tk()
window.title("Pomodoro")
window.minsize(width=500, height=400)
window.config(padx=100, pady=50, bg=YELLOW)


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    label_check.config(text="")
    global repo
    repo = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_count():
    global repo
    repo += 1
    worktime = WORK_MIN * 60
    shortbreak = SHORT_BREAK_MIN * 60
    longbreak = LONG_BREAK_MIN * 60
    if repo % 8 == 0:
        countdown(longbreak)
        label.config(text="Long Break", fg=RED)
    elif repo % 2 == 0:
        countdown(shortbreak)
        label.config(text="Short Break", fg=PINK)
    else:
        countdown(worktime)
        label.config(text="Work Time", fg=GREEN)
        # label_check.config(text=label_check["text"] + "✔")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        if repo % 2 != 0:
            label_check.config(text=label_check["text"] + "✔")
        start_count()


# ---------------------------- UI SETUP ------------------------------- #


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
label.grid(row=0, column=1)

button_start = Button(text="Start", highlightthickness=0, command=start_count)
button_start.grid(row=2, column=0)
button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(row=2, column=2)

label_check = Label(bg=YELLOW, fg=GREEN)
label_check.grid(row=3, column=1)

window.mainloop()
