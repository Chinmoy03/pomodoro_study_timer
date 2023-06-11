from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✓"
reps = 0
tic_tic = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # Change reps to 0. Reset the check marks shown to 0. Change the label back to Timer. Cancel the time loop set up
    # for the timer. Change the timer count back to 0
    global reps
    reps = 0
    check_marks["text"] = ""
    label["text"] = "Timer"
    window.after_cancel(tic_tic)
    canvas.itemconfig(time_text, text= "00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
# This is the timer mechanism that decides whether it is work, break, or long break
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        label["text"] = "Long Break"
        countdown(int(LONG_BREAK_MIN * 100))
    elif reps % 2 == 0:
        label["text"] = "Short Break"
        countdown(int(SHORT_BREAK_MIN * 100))
    else:
        label["text"] = "Work"
        countdown(int(WORK_MIN * 100))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# This function is a recursive function which deals with counting down from a time assigned
def countdown(timer):
    global reps
    global tic_tic
    local_time = timer
    if local_time == 0:
        if reps % 2 == 1:
            check_marks["text"] += CHECK_MARK
        start_timer()

    else:
        if local_time % 100 == 0:
            local_time -= 41
        else:
            local_time -= 1
        canvas.itemconfig(time_text,
                          text=f"{local_time // 1000}{(local_time % 1000) // 100}:{(local_time % 100) // 10}{local_time % 10}")
        tic_tic = window.after(10, countdown, local_time)


# ---------------------------- UI SETUP ------------------------------- #


# To create a window for the program
window = Tk()
window.title("Pomodoro")
window.configure(padx=100, pady=40, bg=YELLOW)

# Creating a canvas and adding image and text to the canvas
img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = canvas.create_image(100, 112, image=img)
time_text = canvas.create_text(100, 130,
                               text=f"00:00",
                               fill='white',
                               font=(FONT_NAME, 20, "bold"))
canvas.grid(row=1, column=1)

# to create a label that says "Timer"
label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
label.grid(row=0, column=1)

# To create command buttons for "Start" and "Reset"
start_btn = Button(text="Start", command=start_timer, borderwidth=0, fg="black", font=(FONT_NAME, 12, "normal"))
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", borderwidth=0, command= reset_timer, fg="black", font=(FONT_NAME, 12, "normal"))
reset_btn.grid(row=2, column=2)

# Adding check mark at the bottom of the tomato
check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "bold"))
check_marks.grid(row=3, column=1)

window.mainloop()
