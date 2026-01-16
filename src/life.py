import pygame

from src.config import ORGANISM, State, GRID_DIM


class Organism(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int, int], color=ORGANISM) -> None:
        super().__init__()
        self.color = color
        self.state = State.ALIVE
        self.position = position

        self.image = pygame.Surface((GRID_DIM, GRID_DIM))
        self.image.fill(self.color)

        self.rect: pygame.Rect = self.image.get_rect(
            topleft=(self.position[0] * GRID_DIM, self.position[1] * GRID_DIM)
        )

    @classmethod
    def spawn(cls, position: tuple[int, int], color: str, organisms: list[Organism]):

        for organism in organisms:
            if organism.position == position:
                return None
        organism = cls(position, color)
        organisms.append(organism)
        return organism

    def kill(self, organisms: list[Organism]):
        for organism in organisms:
            if organism.position == self.position:
                req_organism = organism
        organisms.remove(req_organism)

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, self.rect)
