import pymunk, pygame, sys, math
import pymunk.pygame_util

sys.path.append('src')

from model.testing_pymunk import create_ball, create_boundaries

GRAVITY = 981

pygame.init()

WIDTH, HEIGHT = 1080, 700

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

    space = pymunk.Space()
    space.gravity = (0, GRAVITY)

    ball = create_ball(space, 30, 10)
    create_boundaries(space, WIDTH, HEIGHT)

    draw_options = pymunk.pygame_util.DrawOptions(window)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(space, window, draw_options)
        space.step(delta_time)
        clock.tick(fps)

    pygame.quit()

if __name__ == "__main__":
    run(window, WIDTH, HEIGHT)