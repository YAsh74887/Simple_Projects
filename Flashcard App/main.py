
import random
import pandas
import tkinter

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
learn = data.to_dict(orient="records")


current_card = {} 


def nxt_word():
  global current_card, learn
  current_card=random.choice(learn)
  canvas.itemconfig(card_title, text="French" , fill="black")
  canvas.itemconfig(card_word, text=current_card["French"], fill="black")
  canvas.itemconfig(old_img , image=my_img)
  learn.remove(current_card)
  
 
  
def nxt_word_english():
  global current_card
  canvas.itemconfig(card_title, text="English", fill="white")
  canvas.itemconfig(card_word, text=current_card["English"], fill="white") 
  canvas.itemconfig(old_img, image=new)
   
  
window = tkinter.Tk()
window.after(3000 , func=nxt_word_english)

window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = tkinter.Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
my_img = tkinter.PhotoImage(file="images/card_front.png")
old_img = canvas.create_image(400,263, image=my_img)
new = tkinter.PhotoImage(file="C:/Users/ASUS/Desktop/Flashcard App/images/card_back.png")
card_title = canvas.create_text(400,150,text="", font=("Arial", 28))
card_word = canvas.create_text(400,263,text="", font=("Arial", 60))
canvas.grid(row=0, column=0, columnspan=2 )





bu1=tkinter.PhotoImage(file=("images/right.png"))
unknown_bu = tkinter.Button(image=bu1, highlightthickness=0, command=nxt_word)
unknown_bu.grid(row=1, column=1)

bu2=tkinter.PhotoImage(file=("images/wrong.png"))
known_bu = tkinter.Button(image=bu2, highlightthickness=0 , command=nxt_word_english)
known_bu.grid(row=1, column=0)

nxt_word()

window.mainloop()



