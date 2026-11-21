"""Interface stubs for candidate generation and Minimax search."""

from __future__ import annotations

from .game import Move, PenteGame, Player
from .enum import Stone, Minimax

WIN_SCORE = 1_000_000


def candidate_moves(game: PenteGame, radius: int = Minimax.RADIUS) -> list[Move]:
    """Generate a reduced set of legal points near existing stones."""
    raise NotImplementedError


def order_moves(game: PenteGame, moves: list[Move], player: Player) -> list[Move]:
    """Order candidates to try wins, blocks, and captures before quiet moves."""
    raise NotImplementedError


def choose_move(
    game: PenteGame,
    depth: int = Minimax.DEPTH,
    branch_limit: int = Minimax.BRANCH_LIMIT,
) -> Move | None:
    """Choose a move for the side to move using Minimax and alpha-beta pruning."""
    raise NotImplementedError


def minimax(
    game: PenteGame,
    depth: int,
    ai_player: Player,
    alpha: float,
    beta: float,
    branch_limit: int = Minimax.BRANCH_LIMIT,
) -> float:
    """Search a position recursively, maximizing for AI and minimizing for opponent."""
    raise NotImplementedError


def terminal_score(game: PenteGame, ai_player: Player, depth_remaining: int) -> float:
    """Return a large depth-adjusted score for a terminal win or loss."""
    raise NotImplementedError


def immediate_winning_moves(game: PenteGame, player: Player) -> list[Move]:
    """Find candidate moves that win immediately for ``player``."""
    raise NotImplementedError
