import pygame

pygame.init()

#win size
Width,Height = 700, 500
win = pygame.display.set_mode ((Width,Height))
pygame.display.set_caption("Super xavier")

#creating objects, whatever in my brain this is like in java (button) =>also in pythomn its state heavy so we have to make it step by step
#its not static component like the ones in swing
#step 1: button rect shape, then youll create a new class like name then use the pygame
#step 2: we need to draw inside the while loop cuz its not static it needs to be rendered again and again
x= 50
y= 60
width = 60
height = 60
enter_btn=pygame.Rect(x,y,width,height) #Rect here is an attribute, also case sensitive

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #QUIT HERE case sensitive, lowercase wont work
            running = False

    win.fill((100,100,250))
    #drawing the button syntax
    pygame.draw.rect(win,(200,205,105),enter_btn)

    pygame.display.update()
pygame.quit() #also here its case sensitive, so it wont work if you change it
#notes: in java we change panel, in python pygame we change "state"