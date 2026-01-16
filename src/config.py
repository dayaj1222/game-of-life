from enum import Enum, auto

HEIGHT = 800
WIDTH = 1200
GRID_DIM = 20


GRID_COL = int(WIDTH / GRID_DIM)
GRID_ROW = int(HEIGHT / GRID_DIM)

BACKGROUND = "BLACK"
ORGANISM = "WHITE"


class State(Enum):
    DEAD = auto()
    ALIVE = auto()


class GameState(Enum):
    RUNNING = auto()
    STOPPED = auto()
