from dataclasses import dataclass, field

from peeps import Mawapeep


@dataclass
class GameState:
    food: float = 0.0
    food_per_sec: float = 0.0
    mawapeeps: int = 0
    farmers: list[Mawapeep] = field(default_factory=list)