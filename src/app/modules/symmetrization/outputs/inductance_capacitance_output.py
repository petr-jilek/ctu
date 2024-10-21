from ....shared.utils import common_utils


class InductanceCapacitanceOutput:
    def __init__(self, is_inductance: bool, value: float):
        self.is_inductance = is_inductance
        self.value = value

    def to_dict(self) -> dict:
        return {
            "is_inductance": self.is_inductance,
            "value": common_utils.float_to_str(
                self.value, decimals=3 if self.is_inductance else 6
            ),
        }
