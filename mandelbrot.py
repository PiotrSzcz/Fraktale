from pygame.locals import *
import pygame

width, height = 1000,1000
screen = pygame.display.set_mode((width,height),DOUBLEBUF)
xaxis = width/1.5+140
yaxis = height/2
scale = 400
iterations = 50

def mandelbrot():
    for iy in range(int(height)):
        for ix in range(width):
            z = 0+0j
            c = complex(float(ix-xaxis)/scale, float(iy-yaxis)/scale)
            x=c.real
            y=c.imag
            y2=y*y
            q=(x-0.25)**2+y2
            if not(q*(q+(x-0.25))<y2/4.0 or (x+1.0)**2 + y2 <0.0625):
                for i in range(iterations):
                    z = z**2+c
                    if abs(z) > 2:
                        v = 765*i/iterations
                        if v > 510:
                            color = (255, 255, v%255)
                        elif v > 255:
                            color = (255, v%255, 0)
                        else:
                            color = (v%255, 0, 0)
                        break
                    else:
                        color = (0, 0, 0)
            screen.set_at((ix, iy), color)
    pygame.display.update()

def main():
    pygame.display.set_caption('Mandelbrot')
    global xaxis, yaxis, scale
    run = True
    mandelbrot()
    while run:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            scale += 50
            mandelbrot()
        if keys[pygame.K_DOWN]:
            scale -= 50
            mandelbrot()

        for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    run = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    xaxis, yaxis = pos
                    mandelbrot()

if __name__ == "__main__":
    main()
