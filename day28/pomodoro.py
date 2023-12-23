"""
The Pomodoro Timer
"""

from tkinter import *

PINK = "#E2979C"
RED = "#E7305B"
GREEN = "#9BDEAC"
YELLOW = "#F7F5DD"
FONT = "COURIER"

WORK_TIME = 30
SHORT_BREAK = 5
LONG_BREAK = 15

reps = 0
timer = None


# ----------------- RESET TIMER ------------------ #

def reset_timer():
    """Reset timer to 00:00"""
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    reps = 0
    start_button.config(state='normal')

# --------------- TIMER MECHANISM ---------------- #


def start_timer():
    """Starts the timer when the start button is pressed"""
    global reps
    reps += 1

    start_button.config(state='disabled')

    work_sec = WORK_TIME * 60
    short_break_sec = SHORT_BREAK * 60
    long_break_sec = LONG_BREAK * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break!", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break!", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work!", fg=GREEN)


# ------------- COUNTDOWN MECHANISM ----------------#


def count_down(count):
    """Counts down from start time"""
    global timer

    minutes = count // 60
    seconds = count % 60
    if minutes < 10:
        minutes = "{}{}".format(0, minutes)
    if seconds < 10:
        seconds = "{}{}".format(0, seconds)
    canvas.itemconfig(timer_text, text="{}:{}".format(minutes, seconds))
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(reps // 2):
            mark += "✔"
        check_mark.config(text=mark)


# -------------------- UI SETUP ------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW,
                highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT, 35, "bold")
)

canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW,
                    font=(FONT, 30, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0,
                      command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0,
                      command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(text="", fg=GREEN, bg=YELLOW,
                   font=(FONT, 20, "bold"))
check_mark.grid(column=1, row=3)


window.mainloop()
