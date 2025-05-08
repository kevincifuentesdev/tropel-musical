import pymunk
import math

def create_boundaries(space, width, height):
    rects = [
        [(width/2, height - 10), (width, 20)],
        [(width/2, 10), (width, 20)],
        [(10, height/2), (20, height)],
        [(width - 10, height/2), (20, height)],
    ]

    for pos, size in rects:
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size)
        shape.elasticity = 0.4
        shape.friction = 0.5
        space.add(body, shape)

def create_ball(space, radius, mass, position):
    body = pymunk.Body()
    body.position = position
    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (255, 0, 0, 100)
    shape.elasticity = 0.9
    shape.friction = 0.4
    space.add(body, shape)
    
    return shape

def create_mesa(space, width, y_pos, thickness=10):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (width/2, y_pos)
    shape = pymunk.Poly.create_box(body, (width, thickness))
    shape.friction = 0.5
    shape.elasticity = 0.2
    space.add(body, shape)

def create_ramps(space, start_x, start_y, ramp_length=200, drop_height=80, thickness=5):
    """
    Crea una serie de rampas alternadas en un espacio Pymunk.

    Parámetros:
    - space: El espacio de Pymunk donde se agregarán las rampas.
    - start_x: Coordenada inicial en X de la primera rampa.
    - start_y: Coordenada inicial en Y de la primera rampa.
    - ramp_length: Longitud de cada rampa.
    - drop_height: Altura de caída entre cada rampa.
    - thickness: Grosor de las rampas.
    """
    # Primera rampa
    body1 = pymunk.Body(body_type=pymunk.Body.STATIC)
    x1, y1 = start_x, start_y
    x2, y2 = x1 + ramp_length, y1 - (drop_height // 2)
    ramp1 = pymunk.Segment(body1, (x1, y1), (x2, y2), thickness)
    ramp1.friction = 0.7
    ramp1.elasticity = 0.2
    space.add(body1, ramp1)

    # Segunda rampa (pendiente contraria)
    body2 = pymunk.Body(body_type=pymunk.Body.STATIC)

    x3, y3 = start_x, y2 - drop_height
    x4, y4 = x3 - ramp_length, y3 - (drop_height // 2)

    ramp2 = pymunk.Segment(body2, (x3, y3), (x4, y4), thickness)
    ramp2.friction = 0.7
    ramp2.elasticity = 0.2
    space.add(body2, ramp2)

    # Tercera rampa (similar a la primera)
    body3 = pymunk.Body(body_type=pymunk.Body.STATIC)
    x5, y5 = x4 + 20 + ramp_length, y4 - drop_height
    x6, y6 = x5 + ramp_length, y5 - (drop_height // 2)

    ramp3 = pymunk.Segment(body3, (x5, y5), (x6, y6), thickness)

    ramp3.friction = 0.7
    ramp3.elasticity = 0.2
    space.add(body3, ramp3)

    # Cuarta rampa (similar a la segunda)
    body4 = pymunk.Body(body_type=pymunk.Body.STATIC)

    x7, y7 = start_x, y6 + 700-230
    x8, y8 = x7 - ramp_length - 20, y7 - (drop_height // 2)

    ramp4 = pymunk.Segment(body4, (x7, y7), (x8, y8), thickness)

    ramp4.friction = 0.7
    ramp4.elasticity = 0.2
    space.add(body4, ramp4)
