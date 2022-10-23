import pandas as pd 
import turtle 


screen = turtle.Screen()
screen.title("US State game")

image = "C:/Users/ASUS/Desktop/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)




guessed_state = []
while len(guessed_state) < 50:
  
  data = pd.read_csv("C:/Users/ASUS/Desktop/us-states-game-start/50_states.csv")
  all_states = data.state.to_list()
  answer = screen.textinput(f"{len(guessed_state)}/50", "What is the name of state  ").title()
  
  if answer in all_states:
    guessed_state.append(answer)
    t=turtle.Turtle()
    t.penup()
    t.hideturtle()
    state_data = data[data.state == answer]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(answer)
    
  if answer == "Exit":
    missing = []
    for i in all_states:
      if i not in guessed_state:
        missing.append(i)
        
    new_data = pd.DataFrame(missing)
    new_data.to_csv("states_need_to_learn.csv")   
    break  
    
