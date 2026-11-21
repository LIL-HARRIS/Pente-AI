"""Public interfaces for the Pente rules engine and AI scaffold."""

from .ai_engine import (
    candidate_moves,
    choose_move,
    immediate_winning_moves,
    minimax,
    order_moves,
    terminal_score,
)
from .game import (
    BOARD_SIZE,
    Board,
    Coordinate,
    Move,
    MoveRecord,
    PenteGame,
    Player,
)
from .heuristics import (
    count_vulnerable_pairs,
    evaluate,
    score_capture_progress,
    score_patterns,
    score_vulnerable_pairs,
)
from .enum import Stone, Minimax, Heuristic

__all__ = [
    "Stone",
    "Minimax",
    "Heuristic",
    "BOARD_SIZE",
    "Board",
    "Coordinate",
    "Move",
    "MoveRecord",
    "Player",
    "PenteGame",
    "BOARD_SIZE",
    "Board",
    "Coordinate",
    "Move",
    "MoveRecord",
    "Player",
    "PenteGame",
    "candidate_moves",
    "choose_move",
    "immediate_winning_moves",
    "minimax",
    "order_moves",
    "terminal_score",
    "count_vulnerable_pairs",
    "evaluate",
    "score_capture_progress",
    "score_patterns",
    "score_vulnerable_pairs",
]
