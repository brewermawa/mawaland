from enum import Enum

class PeepRole(Enum):
    FARMER = "farmer"

class Mawapeep:
    _current_role: PeepRole | None

    def __init__(self):
        self._current_role = None

    @property
    def current_role(self):
        return self._current_role
    
    @current_role.setter
    def current_role(self, role):
        if not isinstance(role, PeepRole) and role is not None:
            raise ValueError(f"{role} is not a valid peep role")
        
        self._current_role = role
