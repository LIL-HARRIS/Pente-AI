from enum import Enum

class Stone(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2

class Heuristic(Enum):
    ONE_PAIR = 100
    TWO_PAIR = 200
    THREE_PAIR_OPPONENT_STONE = 400
    THREE_PAIR_NO_OPPONENT_STONE = 600
    FOUR_PAIR_OPPONENT_STONE = 800
    FOUR_PAIR_NO_OPPONENT_STONE = 1000
    FIVE_PAIR = 2000

    CAPTURE = 500
    VULNERABLE_PAIRS = -150

class Minimax(Enum):
    DEPTH = 3
    RADIUS = 2
    BRANCH_LIMIT = 12

