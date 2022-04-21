# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 17:08:33 2022

@author: clambert

model8 relateds to the "Animation-Behaviour" practical and should be used with 
the agentframework8 and the csvreader8 files.

in.txt is the input data for the csvreader8 file and should be stored in the same directory

Directions:
1. Save model8, agentframework8, in.txt and csvreader8 in the same directory location
2. Run model8

Expected outputs:
1. Scatter chart of agents, coloured individually and displayed on environment
background in a seperate window. The animation will show how the agents move
and the eaten "paths" will be displayed
2. print shared neighberhood values between agents (sharing)
3. "Finished" printed on closing the seperate window.
"""

#Imported modules
import random
import operator
import matplotlib.animation 
import matplotlib.pyplot
import agentframework8
import csvreader8

# Set the seed for reducability
#random.seed(0) #testing reducability of model - when set, output should be the same each time
#random.seed(1)

#bring enviroment data in from csvreader8
environment = csvreader8.get_data()

#List of Agents created
agents = []


a = agentframework8.Agent(environment, agents)
#a. __init__()
a. move ()
#print(a.y, a.x) #test agentframework

num_of_agents = 10 #changable value
num_of_iterations = 100 #changable value
neighbourhood = 25 #changable value

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework8.Agent(environment, agents))

carry_on = True	
        
# Move the agents.
def update(frame_number):
    """
    Parameters
    ----------
    moves agents by frame during the animation 

    Returns
    -------
    None.

    """
    fig.clear() # clears previous frame in amnimation (?)
    global carry_on
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move() #moving the agents
            agents[i].eat() #eating into the environment
            agents[i].share_with_neighbours(neighbourhood) #sharing locations between agents

    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
   
#returns graphical results
    matplotlib.pyplot.xlim(0, 99) #x axis
    matplotlib.pyplot.ylim(0, 99) #y axis
    matplotlib.pyplot.imshow(environment) #plots enviroment data from csvreader8
    for i in range(num_of_agents): #created and moved agents based on number of agents
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y) #plot scatter of agents
        print(agents[i].x,agents[i].y) #print list of agents
      
def gen_function(b = [0]):
    """
    Parameters
    ----------
    Frames start at 0 and count through until stopping condition is met

    Yields
    ------
    Returns control and waits next call.

    """
    a = 0
    global carry_on
    while (a < 10) & (carry_on) :
        yield a			# 
        a = a + 1

#animation lines
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
matplotlib.pyplot.show() #show window


# done marker
print ("finished")
