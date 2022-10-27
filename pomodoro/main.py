import math
import tkinter
from turtle import title
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timmer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
  window.after_cancel(timmer)
  canvas.itemconfig(timer_text, text= "00:00")
  global reps
  reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timmer():
  global reps
  reps += 1
  
  work_sec = WORK_MIN * 60
  short_sec = SHORT_BREAK_MIN * 60
  long_break = LONG_BREAK_MIN * 60
  
  if reps % 2 ==0:
    count_down(short_sec)
    label_text.config(text="Break" , fg=PINK)
    
  elif reps % 8 == 0:
    count_down(long_break)
    label_text.config(text="Break" , fg=RED)
    
  else:
    count_down(work_sec) 
    label_text.config(text="Work" , fg=GREEN)   
  
  

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
  count_min = math.floor (count / 60)
  count_sec = count % 60
  
  if count_sec == 0:
    count_sec == "00"
    
  if count_sec < 10:
    count_sec = f"0{count_sec}"  
  
  canvas.itemconfigure(timer_text, text=f"{count_min}:{count_sec}")
  if count > 0:
    global timmer 
    timmer = window.after(1000, count_down , count - 1)
    
  else:
    start_timmer()  
    
# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title( "Pamadora")
window.config(padx=100 , pady=50, bg=YELLOW)


canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, fill="white", text="00:00", font=(FONT_NAME, 34 ,"bold"))
canvas.grid(row=2, column=2)


label_text = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
label_text.grid(row=1, column=2)

label_tick = tkinter.Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
label_tick.grid(row=4, column=2)

start_bu = tkinter.Button(text="Start", command=start_timmer)
start_bu.grid(row=4, column=1)

stop_bu = tkinter.Button(text="Reset", command=reset)
stop_bu.grid(row=4, column=3)




window.mainloop()