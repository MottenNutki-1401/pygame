import pygame

#start init the library pygame
pygame.init()

#canvas window of the ball
win = pygame.display.set_mode((500,400))
pygame.display.set_caption("Hey Baby Ball Mwah!")

#ball position, like in cartesian yk duhh...wtvr im stressed
#this is my repo so don't judge
#why i'm venting in vscode *cries in binary code*
x= 100
y= 100

#ball speed => faster unlike your boring life!
dx = 3
dy = 3

running = True
while running:

    #events idk how this works yet but it does its f*ckin job
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                                running = False
    
    #move the ball, not stuck like you
            x = x + dx
            y= y + dy

            #bounce
            if x < 0 or x > 480:
                dx = -dx

            # bounce top/bottom
            if y < 0 or y > 380:
                dy = -dy

            # draw
            win.fill((20, 20, 40))              # background
            pygame.draw.circle(win, (255, 80, 150), (x, y), 20)  # ball
            pygame.display.update()

pygame.quit()

