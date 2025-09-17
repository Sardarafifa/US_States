import turtle
import pandas #used for data analysis






screen=turtle.Screen()
screen.title("U.S States")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_list=[]


while len(guessed_list)<50:
    answer_state=screen.textinput(title=f"{len(guessed_list)}/50 states correct",prompt="What's another state's name?").title()
    if answer_state=="Exit":
        missing_state=[]
        for state in all_states:
            if state not in guessed_list:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("States_to_learn.csv")        
        print(missing_state)
        break        
    if answer_state in all_states:
        guessed_list.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(state_data.x.item(),state_data.y.item()) #item is used to get first item wihtout any index or line number
        t.write(state_data.state.item())



#states to learn



#tuple.mainloop()
#screen.exitonclick()