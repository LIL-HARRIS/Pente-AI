"""Interface stubs for non-terminal Pente position evaluation."""

from __future__ import annotations

from .game import PenteGame, Player
from .enum import Stone, Heuristic

DEFENSE_BIAS = 1.1


def evaluate(game: PenteGame, player: Player) -> int:
    """Score a non-terminal position from ``player``'s perspective."""
    #TODO: Implement a function that evaluates the game state and returns a score based on the current player's perspective.
    raise NotImplementedError


def score_patterns(game: PenteGame, player: Player) -> int:
    """Score contiguous and split line patterns for one player."""
    #TODO: Implement a scoring function that evaluates the board based on contiguous and split line patterns for the given player.
    raise NotImplementedError


def score_capture_progress(game: PenteGame, player: Player) -> int:
    """Score captured stones and proximity to the capture-win threshold."""
    #TODO: Implement a scoring function that rewards the player for capturing stones and getting closer to the capture-win threshold.
    raise NotImplementedError


def score_vulnerable_pairs(game: PenteGame, player: Player) -> int:
    """Return the heuristic penalty for pairs vulnerable to capture."""
    #TODO: Implement a function that returns the heuristic penalty for pairs that are vulnerable to capture.
    raise NotImplementedError
