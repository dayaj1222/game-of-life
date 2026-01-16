import pygame


class StartStopButton(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int = 100, height: int = 40):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.is_running = False

        self.start_color = (40, 167, 69)
        self.stop_color = (220, 53, 69)
        self.font = pygame.font.Font(None, 28)

        if not pygame.font.get_init():
            pygame.font.init()

    def handle_click(self, mouse_pos: tuple[int, int]) -> bool:
        if self.rect.collidepoint(mouse_pos):
            self.is_running = not self.is_running
            return True
        return False

    def draw(self, screen: pygame.Surface):
        color = self.stop_color if self.is_running else self.start_color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)

        text = "STOP" if self.is_running else "START"
        text_surface = self.font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
