from tkinter import *
import random 
#This are constants for the game
GAME_WIDTH=700
GAME_HEIGHT =700
SPEED=100
SPACE_SIZE=50
BODY_PARTS=3
SNAKE_COLOR="#00FF00"
FOOD_COLOR="#FF0000"
BG_COLOR="#000000"

class Snake:
    def __init__(self):
        self.body_size=BODY_PARTS
        self.coordinates=[]
        self.square=[]

        for i in range(0,BODY_PARTS):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag="snake")
            self.square.append(square)


class Food:
    def __init__(self):
        x=random.randint(0,(GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y=random.randint(0,(GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates=[x,y]

        canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tag="food")

def next_turn(snake,food):
    x,y=snake.coordinates[0]

    if direction=="up":
        y-=SPACE_SIZE

    elif direction=="down":
        y+=SPACE_SIZE

    elif direction=="left":
        x-=SPACE_SIZE

    elif direction=="right":
        x+=SPACE_SIZE

    snake.coordinates.insert(0,(x,y))

    square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)

    snake.square.insert(0,square)

    if x==food.coordinates[0] and y==food.coordinates[1]:
        global score
        score+=1
        label.config(text="SCORE:{}".format(score))
        canvas.delete("food")
        food=Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.square[-1])
        del snake.square[-1] 

    if check_collision(snake):
        game_over()
    else:    
        window.after(SPEED,next_turn,snake,food)


def change_dir(new_direction):
    global direction

    if new_direction=='left':
        if direction!='right':
            direction=new_direction

    elif new_direction=='right':
        if direction!='left':
            direction=new_direction

    elif new_direction=='up':
        if direction!='down':
            direction=new_direction

    elif new_direction=='down':
        if direction!='up':
            direction=new_direction

def check_collision(snake):
    x,y=snake.coordinates[0]

    if x<0 or x>=GAME_WIDTH:
        
        return True
    
    elif y<0 or y>=GAME_HEIGHT:
        
        return True
    
    for body_part in snake.coordinates[1:]:
        if x==body_part[0] and y==body_part[1]:
            return True
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('italian',50),fill="red",text="Game Over")

window=Tk()
window.title("SNAKE GAME")
window.resizable(False,False)  #makes a non-resizable window in an application.

score=0
direction='down'

label=Label(window,text="Score:{}".format(score),font=('italian',40))  #Tkinter Label is a widget that is used to implement display boxes where you can place text or images.  
label.pack()

canvas=Canvas(window, bg=BG_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.bind('<Left>',lambda event:change_dir('left'))
window.bind('<Right>',lambda event:change_dir('right'))
window.bind('<Up>',lambda event:change_dir('up'))
window.bind('<Down>',lambda event:change_dir('down'))

snake=Snake()
food=Food()

next_turn(snake,food) 

window.mainloop()   #an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.