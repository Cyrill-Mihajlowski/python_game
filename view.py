import pygame.display


class GameView:
    def __init__(self, width, height, title):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

    def draw(self, x, y, background):
        background_image = pygame.image.load(background)

        self.screen.fill((255, 255, 255))
        self.screen.blit(background_image, (0, 0))

        pygame.draw.circle(self.screen, (230, 0, 0), (x, y - 40), 40)

        pygame.display.update()
        pygame.display.flip()
