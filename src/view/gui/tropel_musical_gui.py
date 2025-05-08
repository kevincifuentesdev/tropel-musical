import pymunk
import pygame
import sys
import math

import pymunk.pygame_util
sys.path.append('src')

from model.testing_pymunk import create_ball, create_boundaries, create_table, create_ramps, create_domino

# Configuración
GRAVITY = 981
WIDTH, HEIGHT = 1080, 700

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

def draw(space, window, draw_options):
    window.fill("white")
    space.debug_draw(draw_options)
    pygame.display.update()

def ball_hits_domino(arbiter, space, data):
    impact_threshold = 6
    if arbiter.total_impulse.length > impact_threshold:
        print("¡La bola golpeó un dominó!")
    return True

def run(window, width, height):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    delta_time = 1/fps

    # Physic space config
    space = pymunk.Space()
    space.gravity = (0, GRAVITY)
    draw_options = pymunk.pygame_util.DrawOptions(window)

    # Constant Properties for Table and Ramps
    TABLE = HEIGHT - 150
    START_Y = TABLE - 200

    # Constan Properties for the dominoes
    NUM_DOMINOES = 10
    DOMINOES_WIDTH = 10
    DOMINOES_HEIGHT = 45
    DOMINOES_MASS = 0.5

    DOMINOES_FRICTION = 0.5
    DOMINOES_ELASTICITY = 0.4
    SPACING_FACTOR = 0.4
    START_X = 450
    GROUND_Y = TABLE - (DOMINOES_HEIGHT / 2)

    # Dominoes Creation
    domino_bodies = []
    domino_shapes = []
    cumulative_x = START_X
    last_half_width = DOMINOES_WIDTH / 2

    for i in range(NUM_DOMINOES):
        # Calculate current dimensions
        current_half_width = DOMINOES_WIDTH / 2

        # Calculate spacing based on the *previous* domino's height (more stable)
        # For the first domino, use initial height
        prev_height = DOMINOES_HEIGHT
        current_spacing = prev_height * SPACING_FACTOR

        # Calculate position for the center of the current domino
        # Position = previous X + half_width_prev + spacing + half_width_current
        x_pos = cumulative_x + last_half_width + current_spacing + current_half_width

        # Create the domino
        body, shape = create_domino(
            x_pos, GROUND_Y, DOMINOES_WIDTH, DOMINOES_HEIGHT, DOMINOES_MASS,
            DOMINOES_FRICTION, DOMINOES_ELASTICITY, space
        )
        domino_bodies.append(body)
        domino_shapes.append(shape)

        # Update cumulative position and width for next iteration
        cumulative_x = x_pos # Store center position
        last_half_width = current_half_width

    # Handling Collision
    handler = space.add_collision_handler(0,1)
    handler.post_solve = ball_hits_domino

    # Init functionalities
    create_boundaries(space, WIDTH, HEIGHT)

    create_table(space, WIDTH - 200, TABLE)

    create_ramps(space, start_x=225, start_y=START_Y)

    ball = None
    create_ball(space, radius=15, mass=0.2, position=(780, GROUND_Y))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # Clic derecho
                x, y = pygame.mouse.get_pos()
                ball = create_ball(space, radius=15, mass=0.5, position=(x, y))

        draw(space, window, draw_options)
        space.step(delta_time)
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)