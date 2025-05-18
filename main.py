import pgzrun
import random


TITLE="Recycling Paper Bags"
WIDTH=800
HEIGHT=600

START_SPEED=10
ITEMS = ["bag","battery","bottle","chips"]
FINAL_LEVEL = 6
current_level = 1

#lose the game
game_over =False
#win the game
game_complete=False

items = []
animations = []

def draw():
    global items, game_over,game_complete,current_level
    screen.clear()
    screen.blit("bground",(0,0))

    if game_over:
        #Abstraction-Trying to call a user defined function before creating it
        display_message("GAME OVER","Try again")
    elif game_complete:
        display_message("GOOD JOB!","You won!")
    else:
        for item in items:
            item.draw()

def display_message(heading,sub_heading):
    screen.draw.text(heading,fontsize=60,center=(400,300), color="black")
    screen.draw.text(sub_heading,fontsize=50,center=(400,250),color="black")

def update():
    global items

    if len(items)==0:
        items=make_items(current_level)

#Decomposition: breaking down a problem into small chunks/portions and solving it seperately
#Make items
#1.get the options from ITEMS list- random
#2.Create actors and add it to items list
#3.Layout items-display them with equal spacing
#4.Animations-move objects down
#Create Function for all the steps

def make_items(number_of_extra_items):
    #Step1:
    items_to_create= get_option_to_create(number_of_extra_items) #function in front because it returns a value as a result of the function.Whenever you return something you need to store it in a variable.
    #Step2:
    new_items = create_items(items_to_create) #function in front because it returns a list as a result of the function.Whenever you return something you need to store it in a variable.
    #Step 3:
    layout_items(new_items)
    #Step 4:
    animate_items(new_items)

    return new_items
    
def get_option_to_create(number_of_extra_items):
    items_to_create=['paper']
    for i in range(0,number_of_extra_items):
        random_option=random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_items=[]
    for i in items_to_create:
        item = Actor( i +'img')
        new_items.append(item)
    return new_items

def layout_items(items_to_layout):
    pass

def animate_items(items_to_animate):
    pass


pgzrun.go()

