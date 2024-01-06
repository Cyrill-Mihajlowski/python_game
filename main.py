import pygame

from model import GameModel
from view import GameView
from controller import GameController

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1000
TITLE = "Game in Python"
FPS = 30


def main():
    pygame.init()

    model = GameModel(SCREEN_WIDTH, SCREEN_HEIGHT)
    view = GameView(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    controller = GameController(model, view)

    clock = pygame.time.Clock()

    while True:
        controller.handle_events()
        controller.update_view()

        clock.tick(FPS)


if __name__ == '__main__':
    main()