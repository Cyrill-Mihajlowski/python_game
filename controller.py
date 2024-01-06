import pygame
import sys


class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        self.model.is_left_pressed = keys[pygame.K_LEFT]
        self.model.is_right_pressed = keys[pygame.K_RIGHT]

    def update_view(self):
        self.model.update_position()
        self.view.draw(
            self.model.x_coordinate, self.model.y_coordinate, self.model.imgBackground
        )
