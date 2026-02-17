import pygame

pygame.init() #initialized pygame library


#window size + putting frame tittle
WIDTH, HEIGHT = 400,300
win = pygame.display.set_mode((WIDTH,HEIGHT)) #here we use double(()) => its not really a double, the inner reprsents a tupple
# (400,300)=> tupple (two values grouped together) => pygame expects only ONE argument
#in java we use... new Dimension (400,300) => this created new object, in python we dont do that, we dont need a class
pygame.display.set_caption("For You....")

#Quick notes
#We set WIDTH, HEIGHT (capitalized) but we can also use lowercase
#This is just for organizing stuff, UPPERCASE => constant "I dont plan to change it in the future"
# When you run this code a window will pop up but will close automatically
# this needs a game loop that runs continously and updates constantly 
#tuple=> an ordered collection of objects