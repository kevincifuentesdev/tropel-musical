import pymunk
from typing import Tuple


def create_boundaries(space: pymunk.Space, width: int, height: int) -> None:
    """
    Crea los límites del espacio físico.

    :param space: Espacio físico de Pymunk.
    :param width: Ancho del espacio.
    :param height: Alto del espacio.
    """
    boundaries = [
        [(width / 2, height - 10), (width, 20)],  # Límite inferior
        [(width / 2, 10), (width, 20)],          # Límite superior
        [(10, height / 2), (20, height)],        # Límite izquierdo
        [(width - 10, height / 2), (20, height)] # Límite derecho
    ]

    for position, size in boundaries:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = position
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)


def create_ball(space: pymunk.Space, radius: float, mass: float, position: Tuple[float, float]) -> pymunk.Shape:
    """
    Crea una bola en el espacio físico.

    :param space: Espacio físico de Pymunk.
    :param radius: Radio de la bola.
    :param mass: Masa de la bola.
    :param position: Posición inicial de la bola (x, y).
    :return: La forma de la bola creada.
    """
    body = pymunk.Body()
    body.position = position
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (255, 0, 0, 100)
    shape.elasticity = 0.9
    shape.friction = 0.4
    shape.collision_type = 0
    space.add(body, shape)
    return shape


def create_table(space: pymunk.Space, width: float, y_pos: float, thickness: float = 10) -> None:
    """
    Crea una mesa en el espacio físico.

    :param space: Espacio físico de Pymunk.
    :param width: Ancho de la mesa.
    :param y_pos: Posición vertical de la mesa.
    :param thickness: Grosor de la mesa.
    """
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (width / 2, y_pos)
    shape = pymunk.Poly.create_box(body, (width, thickness))
    shape.friction = 0.5
    shape.elasticity = 0.2
    space.add(body, shape)


def create_ramps(
    space: pymunk.Space,
    start_x: float,
    start_y: float,
    ramp_length: float = 200,
    drop_height: float = 80,
    thickness: float = 5
) -> None:
    """
    Crea una serie de rampas alternadas en el espacio físico.

    :param space: Espacio físico de Pymunk.
    :param start_x: Coordenada inicial en X de la primera rampa.
    :param start_y: Coordenada inicial en Y de la primera rampa.
    :param ramp_length: Longitud de cada rampa.
    :param drop_height: Altura de caída entre cada rampa.
    :param thickness: Grosor de las rampas.
    """
    # Primera rampa
    body1 = pymunk.Body(body_type=pymunk.Body.STATIC)
    x1, y1 = start_x, start_y
    x2, y2 = x1 + ramp_length, y1 - (drop_height // 2)
    ramp1 = pymunk.Segment(body1, (x1, y1), (x2, y2), thickness)
    ramp1.friction = 0.7
    ramp1.elasticity = 0.2
    space.add(body1, ramp1)

    # Segunda rampa
    body2 = pymunk.Body(body_type=pymunk.Body.STATIC)
    x3, y3 = start_x, y2 - drop_height
    x4, y4 = x3 - ramp_length, y3 - (drop_height // 2)
    ramp2 = pymunk.Segment(body2, (x3, y3), (x4, y4), thickness)
    ramp2.friction = 0.7
    ramp2.elasticity = 0.2
    space.add(body2, ramp2)

    # Tercera rampa
    body3 = pymunk.Body(body_type=pymunk.Body.STATIC)
    x5, y5 = x4 + 20 + ramp_length, y4 - drop_height
    x6, y6 = x5 + ramp_length, y5 - (drop_height // 2)
    ramp3 = pymunk.Segment(body3, (x5, y5), (x6, y6), thickness)
    ramp3.friction = 0.7
    ramp3.elasticity = 0.2
    space.add(body3, ramp3)

    # Cuarta rampa
    body4 = pymunk.Body(body_type=pymunk.Body.STATIC)
    x7, y7 = start_x, y6 + 700 - 230
    x8, y8 = x7 - ramp_length - 20, y7 - (drop_height // 2)
    ramp4 = pymunk.Segment(body4, (x7, y7), (x8, y8), thickness)
    ramp4.friction = 0.7
    ramp4.elasticity = 0.2
    space.add(body4, ramp4)


def create_domino(
    pos_x: float,
    pos_y: float,
    width: float,
    height: float,
    mass: float,
    friction: float,
    elasticity: float,
    space: pymunk.Space
) -> Tuple[pymunk.Body, pymunk.Shape]:
    """
    Crea un dominó en el espacio físico.

    :param pos_x: Posición en X del dominó.
    :param pos_y: Posición en Y del dominó.
    :param width: Ancho del dominó.
    :param height: Alto del dominó.
    :param mass: Masa del dominó.
    :param friction: Fricción del dominó.
    :param elasticity: Elasticidad del dominó.
    :param space: Espacio físico de Pymunk.
    :return: El cuerpo y la forma del dominó creados.
    """
    body = pymunk.Body(mass, pymunk.moment_for_box(mass, (width, height)))
    body.position = (pos_x, pos_y)
    shape = pymunk.Poly.create_box(body, (width, height))
    shape.friction = friction
    shape.elasticity = elasticity
    shape.collision_type = 1
    space.add(body, shape)
    return body, shape
