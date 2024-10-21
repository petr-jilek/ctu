class SymmetrizationInput:
    def __init__(
        self,
        U: float,
        f: float,
        cos_phi: float,
        P_12: float,
        P_13: float,
        P_23: float,
        P_12_inductive: bool,
        P_13_inductive: bool,
        P_23_inductive: bool,
    ):
        self.U = U
        self.f = f
        self.cos_phi = cos_phi
        self.P_12 = P_12
        self.P_13 = P_13
        self.P_23 = P_23
        self.P_12_inductive = P_12_inductive
        self.P_13_inductive = P_13_inductive
        self.P_23_inductive = P_23_inductive
