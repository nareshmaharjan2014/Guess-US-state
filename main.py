import turtle
import pandas as pd
from tkinter import messagebox
#root = Tk()

screen = turtle.Screen()
screen.title("Guess The State")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
	answer_state = screen.textinput(title=f"{len(guessed_state)}/ 50 Guess the state", prompt="What's another state name").title()
	missing_state = []
	
		
	if answer_state == "Exit":
		for state in all_states:
			if state not in guessed_state:
				missing_state.append(state)
				new_data = pd.DataFrame(missing_state)
				new_data.to_csv("states_to_learn.csv")
			
		break
	if answer_state in guessed_state:
		#t.goto(-800, 700)
		#t.write("the state already guessed")
		messagebox.showinfo("Guess the state", f"{answer_state} is already guessed")
		
	elif answer_state in all_states:
		guessed_state.append(answer_state)
		
		state_data = data[data.state == answer_state]
		t.goto(int(state_data.x), int(state_data.y))
		t.write(state_data.state.item())


