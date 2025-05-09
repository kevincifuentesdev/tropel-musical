import sys
from typing import Optional
import pygame
import pymunk
import pymunk.pygame_util

sys.path.append('src')
from model.tropel_musical_model import (
    create_ball,
    create_boundaries,
    create_table,
    create_ramps,
    create_domino,
)

# Configuración global
GRAVITY = 981
WIDTH, HEIGHT = 1080, 700
FPS = 60
DELTA_TIME = 1 / FPS
IMPACT_THRESHOLD = 6
DOMINO_PROPERTIES = {
    "num_dominoes": 10,
    "width": 10,
    "height": 45,
    "mass": 0.5,
    "friction": 0.5,
    "elasticity": 0.4,
    "spacing_factor": 0.4,
    "start_x": 450,
}
TABLE_HEIGHT = HEIGHT - 150
GROUND_Y = TABLE_HEIGHT - (DOMINO_PROPERTIES["height"] / 2)
START_Y = TABLE_HEIGHT - 200


def draw(space: pymunk.Space, window: pygame.Surface, draw_options: pymunk.pygame_util.DrawOptions) -> None:
    """
    Dibuja el espacio físico en la ventana de Pygame.

    :param space: Espacio físico de Pymunk.
    :param window: Ventana de Pygame.
    :param draw_options: Opciones de dibujo de Pymunk.
    """
    window.fill("white")
    space.debug_draw(draw_options)
    pygame.display.update()


def ball_hits_domino(arbiter: pymunk.Arbiter, space: pymunk.Space, data: dict) -> bool:
    """
    Maneja la colisión entre la bola y un dominó.

    :param arbiter: Objeto que contiene información de la colisión.
    :param space: Espacio físico de Pymunk.
    :param data: Datos adicionales (no utilizados).
    :return: Siempre devuelve True.
    """
    if arbiter.total_impulse.length > IMPACT_THRESHOLD:
        # Aquí podrías implementar un sistema de registro o eventos en lugar de un print.
        pass
    return True


def create_dominoes(space: pymunk.Space) -> None:
    """
    Crea una fila de dominós en el espacio físico.

    :param space: Espacio físico de Pymunk.
    """
    properties = DOMINO_PROPERTIES
    cumulative_x = properties["start_x"]
    last_half_width = properties["width"] / 2

    for _ in range(properties["num_dominoes"]):
        current_half_width = properties["width"] / 2
        current_spacing = properties["height"] * properties["spacing_factor"]
        x_pos = cumulative_x + last_half_width + current_spacing + current_half_width

        create_domino(
            x_pos,
            GROUND_Y,
            properties["width"],
            properties["height"],
            properties["mass"],
            properties["friction"],
            properties["elasticity"],
            space,
        )

        cumulative_x = x_pos
        last_half_width = current_half_width


def run(window: pygame.Surface, width: int, height: int) -> None:
    """
    Ejecuta el bucle principal del programa.

    :param window: Ventana de Pygame.
    :param width: Ancho de la ventana.
    :param height: Alto de la ventana.
    """
    pygame.init()
    clock = pygame.time.Clock()
    space = pymunk.Space()
    space.gravity = (0, GRAVITY)
    draw_options = pymunk.pygame_util.DrawOptions(window)

    create_boundaries(space, width, height)
    create_table(space, width - 200, TABLE_HEIGHT)
    create_ramps(space, start_x=225, start_y=START_Y)
    create_dominoes(space)

    handler = space.add_collision_handler(0, 1)
    handler.post_solve = ball_hits_domino

    create_ball(space, radius=15, mass=0.2, position=(780, GROUND_Y))

    running = True
    create_ball(space, radius=15, mass=0.5, position=(437, 53))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                x, y = pygame.mouse.get_pos()

                print((x, y))

        draw(space, window, draw_options)
        space.step(DELTA_TIME)
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tropel Musical Simulation")
    run(window, WIDTH, HEIGHT)