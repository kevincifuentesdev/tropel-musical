import pymunk


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

def create_ball(space, radius, mass):
    body = pymunk.Body()
    body.position = (300, 300)

    shape = pymunk.Circle(body, radius)
    shape.mass = mass
    shape.color = (255, 0, 0, 100) # RGBA
    shape.elasticity = 0.9
    shape.friction = 0.4

    space.add(body, shape)

    return shape

