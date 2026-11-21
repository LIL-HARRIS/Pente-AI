"""Interface stubs for Pente board state and rules; no rules are implemented."""

from __future__ import annotations

from dataclasses import dataclass, field
from .enum import Stone

BOARD_SIZE = 19
Player = Stone
Coordinate = tuple[int, int]
Move = Coordinate
Board = list[list[Stone]]


def _empty_board() -> Board:
    """Create a fresh empty board for a new game state."""
    return [[Stone.EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def _initial_captures() -> dict[Player, int]:
    """Create independent capture counters for both players."""
    return {Stone.WHITE: 0, Stone.BLACK: 0}


@dataclass(frozen=True)
class MoveRecord:
    """Prior state needed to undo a move during search."""

    move: Move
    player: Player
    captured_positions: tuple[Coordinate, ...]
    previous_current_player: Player
    previous_winner: Player | None
    previous_last_move: Move | None
    previous_capture_count: int
    previous_move_count: int


@dataclass
class PenteGame:
    """Shared game state and planned rules API used by the UI and AI."""

    board: Board = field(default_factory=_empty_board)
    current_player: Player = Stone.WHITE
    captures: dict[Player, int] = field(default_factory=_initial_captures)
    winner: Player | None = None
    last_move: Move | None = None
    move_count: int = 0

    @staticmethod
    def in_bounds(row: int, col: int) -> bool:
        """Return whether a board coordinate is within the 19×19 grid."""
        raise NotImplementedError

    def is_legal_move(self, row: int, col: int) -> bool:
        """Check bounds, vacancy, and whether the game is still active."""
        raise NotImplementedError

    def legal_moves(self) -> list[Move]:
        """Return all legal moves, without AI-specific candidate pruning."""
        raise NotImplementedError

    def make_move(self, row: int, col: int) -> MoveRecord:
        """Place a stone, resolve captures, update the turn, and check victory."""
        raise NotImplementedError

    def undo_move(self, record: MoveRecord) -> None:
        """Restore the entire position to the state before ``record``."""
        raise NotImplementedError

    def find_captures(self, row: int, col: int, player: Player) -> list[Coordinate]:
        """Find enemy stone coordinates captured by a move at this point."""
        raise NotImplementedError

    def is_line_win(self, row: int, col: int, player: Player) -> bool:
        """Check for five or more contiguous stones through a given point."""
        raise NotImplementedError

    def is_capture_win(self, player: Player) -> bool:
        """Check whether the player has captured at least ten stones."""
        raise NotImplementedError

    def check_winner(self, row: int, col: int, player: Player) -> Player | None:
        """Return the winner after a move, or ``None`` if play continues."""
        raise NotImplementedError

    def has_line_win(self, player: Player) -> bool:
        """Check whether the player's current board position contains a five."""
        raise NotImplementedError

    def is_game_over(self) -> bool:
        """Return whether a winner exists or no legal moves remain."""
        raise NotImplementedError

    def is_draw(self) -> bool:
        """Return whether the board is full and neither player has won."""
        raise NotImplementedError

    def copy(self) -> PenteGame:
        """Return an independent copy of the position for analysis or display."""
        raise NotImplementedError
