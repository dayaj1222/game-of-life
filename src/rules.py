from src.config import GRID_COL, GRID_ROW, ORGANISM, State
from src.life import Organism


class LifeEngine:
    def __init__(self, organisms: list[Organism]) -> None:
        self.organisms = organisms
        self.update_alive_cells()

    def step(self):
        to_kill = []
        to_reproduce = []

        # 1. Determine who dies
        for organism in self.organisms:
            if organism.state == State.ALIVE:
                neighbors = self.get_neighbors(organism.position)
                if len(neighbors) < 2 or len(neighbors) > 3:
                    to_kill.append(organism)

        # 2. Determine who is born
        candidates = set()
        for x, y in self.alive_cells:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < GRID_COL and 0 <= ny < GRID_ROW:
                        if (nx, ny) not in self.alive_cells:
                            candidates.add((nx, ny))

        for cell in candidates:
            if len(self.get_neighbors(cell)) == 3:
                to_reproduce.append(cell)

        # 3. Apply all changes at once (The 'Frame' update)
        for organism in to_kill:
            organism.kill(self.organisms)

        for cell in to_reproduce:
            Organism.spawn(cell, ORGANISM, self.organisms)

        self.update_alive_cells()

    def get_neighbors(self, pos: tuple[int, int]):
        x, y = pos
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if (x + dx, y + dy) in self.alive_cells:
                    count += 1
        # Returning a list of positions for compatibility, though a count is faster
        return [None] * count

    def update_alive_cells(self):
        self.alive_cells = {
            o.position for o in self.organisms if o.state == State.ALIVE
        }
