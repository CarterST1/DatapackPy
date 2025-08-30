from functools import total_ordering
from typing import overload


@total_ordering  # fills in >=, <=, != automatically
class GameVersion:
    """A utility class for game versions with comparison and other functions."""

    def __init__(self, major: int = 1, minor: int = 21, patch: int = 8):
        self.major: int = major
        self.minor: int = minor
        self.patch: int = patch

    @overload
    @staticmethod
    def fromTuple(input: tuple[int, int, int]) -> 'GameVersion': ...
    @overload
    @staticmethod
    def fromTuple(input: tuple[int, int]) -> 'GameVersion': ...
    @staticmethod
    def fromTuple(input: tuple) -> 'GameVersion':
        """Converts a tuple to a `GameVersion`. Missing patch defaults to 0."""
        return GameVersion(*input, *(0,) * (3 - len(input)))

    def __repr__(self) -> str:
        return f'v{self.major}.{self.minor}.{self.patch}'

    def _normalize(self, value: object) -> 'GameVersion':
        """Convert tuple -> GameVersion if needed, else return value unchanged."""
        if isinstance(value, GameVersion):
            return value
        if isinstance(value, tuple):
            return GameVersion.fromTuple(value)
        return NotImplemented

    def __eq__(self, value: object) -> bool:
        other = self._normalize(value)
        if other is NotImplemented:
            return NotImplemented
        return (self.major, self.minor, self.patch) == (other.major, other.minor, other.patch)

    def __lt__(self, value: object) -> bool:
        other = self._normalize(value)
        if other is NotImplemented:
            return NotImplemented
        return (self.major, self.minor, self.patch) < (other.major, other.minor, other.patch)
    
__all__ = ['GameVersion']