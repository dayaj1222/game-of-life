import math
import pygame
from pygame.time import Clock
from src.button import StartStopButton
from src.life import Organism
from src.config import GRID_DIM, HEIGHT, ORGANISM, WIDTH, GameState
from src.renderer import Renderer
from src.rules import LifeEngine


class GameManager:
    def __init__(self) -> None:
        self.life = Organism((int(WIDTH / 2), int(HEIGHT / 2)))
        self.organisms: list[Organism] = [self.life]
        self.num: int = 0
        self.state = GameState.STOPPED
        self.button = StartStopButton(WIDTH // 2 - 60, HEIGHT - 50)
        self.fps = 120

        self.renderer = Renderer(self.organisms)

        # Initialize LifeEngine AFTER patterns are spawned
        self.life_engine = LifeEngine(self.organisms)

        print(f"Alive cells after spawn: {len(self.life_engine.alive_cells)}")

    def handle_click(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if self.button.handle_click(mouse_pos):
                return

        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            mouse_pos = pygame.mouse.get_pos()
            if not self.button.rect.collidepoint(mouse_pos):
                mouse_x = math.floor(mouse_pos[0] / GRID_DIM)
                mouse_y = math.floor(mouse_pos[1] / GRID_DIM)
                self.life.spawn((mouse_x, mouse_y), ORGANISM, self.organisms)
                self.life_engine.update_alive_cells()

    def update(self, screen: pygame.Surface, clock: Clock):

        clock.tick(self.fps)
        if self.button.is_running:
            self.fps = 10
            self.life_engine.step()
        else:
            self.fps = 120

        self.renderer.render(screen, self.button)
