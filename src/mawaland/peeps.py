from enum import Enum

class PeepRole(Enum):
    FARMER = "farmer"

class Mawapeep:
    current_role: PeepRole | None

    def __init__(self):
        self.current_role = None