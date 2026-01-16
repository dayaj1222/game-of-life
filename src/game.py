import pygame
from src.config import BACKGROUND, HEIGHT, WIDTH
from src.game_manager import GameManager


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.font.init()
        self.running = True
        self.game_manager = GameManager()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Game of Life")

        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                self.game_manager.handle_click(event)

            self.screen.fill(BACKGROUND)

            self.game_manager.update(self.screen, self.clock)
            pygame.display.flip()
        pygame.quit()
