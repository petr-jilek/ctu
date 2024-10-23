from ....shared.utils import common_utils
from .inductance_capacitance_output import InductanceCapacitanceOutput


class SymmetrizationOutput:
    def __init__(
        self,
        phi: float,
        tan_phi: float,
        Y_12_complex: complex,
        Y_13_complex: complex,
        Y_23_complex: complex,
        Y_s_12: float,
        Y_s_13: float,
        Y_s_23: float,
        icr_12: InductanceCapacitanceOutput,
        icr_13: InductanceCapacitanceOutput,
        icr_23: InductanceCapacitanceOutput,
    ):
        self.phi = phi
        self.tan_phi = tan_phi
        self.Y_12_complex = Y_12_complex
        self.Y_13_complex = Y_13_complex
        self.Y_23_complex = Y_23_complex
        self.Y_s_12 = Y_s_12
        self.Y_s_13 = Y_s_13
        self.Y_s_23 = Y_s_23
        self.icr_12 = icr_12
        self.icr_13 = icr_13
        self.icr_23 = icr_23

    def to_dict(self) -> dict:
        return {
            "phi": common_utils.float_to_str(self.phi),
            "tan_phi": common_utils.float_to_str(self.tan_phi),
            "Y_1_complex": common_utils.complex_to_str(self.Y_1_complex),
            "Y_2_complex": common_utils.complex_to_str(self.Y_2_complex),
            "Y_3_complex": common_utils.complex_to_str(self.Y_3_complex),
            "Y_s_12": common_utils.float_to_str(self.Y_s_12),
            "Y_s_13": common_utils.float_to_str(self.Y_s_13),
            "Y_s_23": common_utils.float_to_str(self.Y_s_23),
            "icr_12": self.icr_12.to_dict(),
            "icr_13": self.icr_13.to_dict(),
            "icr_23": self.icr_23.to_dict(),
        }
