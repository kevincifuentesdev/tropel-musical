import pymunk
import pygame
import sys

import pymunk.pygame_util
sys.path.append('src')

from model.testing_pymunk import create_ball, create_boundaries, create_mesa, create_ramps

# Configuración
GRAVITY = 981
WIDTH, HEIGHT = 1080, 700

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

def draw(space, window, draw_options):
    window.fill("white")
    space.debug_draw(draw_options)
    pygame.display.update()

def run(window, width, height):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    delta_time = 1/fps

    # Configurar espacio físico
    space = pymunk.Space()
    space.gravity = (0, GRAVITY)
    draw_options = pymunk.pygame_util.DrawOptions(window)

    create_boundaries(space, WIDTH, HEIGHT)

    MESA = HEIGHT - 150
    create_mesa(space, WIDTH - 200, MESA)

    # Ajustar start_y para que las rampas estén dentro del área visible
    START_Y = MESA - 200  # Reducir la distancia desde la mesa
    create_ramps(space, start_x=225, start_y=START_Y)

    ball = None

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # Clic derecho
                x, y = pygame.mouse.get_pos()
                ball = create_ball(space, radius=15, mass=0.005, position=(x, y))

        draw(space, window, draw_options)
        space.step(delta_time)
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)