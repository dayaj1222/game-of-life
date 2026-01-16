from pygame import Surface
from src.config import HEIGHT, WIDTH, State
from src.life import Organism
from src.button import StartStopButton


class Renderer:
    def __init__(self, organisms: list[Organism]) -> None:
        self.organisms = organisms

    def render(self, screen: Surface, button: StartStopButton):
        alive_organisms = [o for o in self.organisms if o.state == State.ALIVE]
        for organism in alive_organisms:
            if organism.state == State.ALIVE:
                organism.draw(screen)

        button.draw(screen)
