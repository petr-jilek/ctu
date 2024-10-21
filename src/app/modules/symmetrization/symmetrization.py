import math

from ...shared.utils import common_utils
from .inputs.symmetrization_input import SymmetrizationInput
from .outputs.inductance_capacitance_output import InductanceCapacitanceOutput
from .outputs.symmetrization_output import SymmetrizationOutput


def symmetrize(input: SymmetrizationInput) -> SymmetrizationOutput:
    phi = math.acos(input.cos_phi)
    tg_phi = math.tan(phi)

    def inductive_sign(inductive):
        return -1 if inductive else 1

    def get_Y_complex(P, inductive):
        return (
            P / (input.U**2) * (1 + inductive_sign(inductive) * complex(0, 1) * tg_phi)
        )

    Y_12_complex = get_Y_complex(input.P_12, input.P_12_inductive)
    Y_13_complex = get_Y_complex(input.P_13, input.P_13_inductive)
    Y_23_complex = get_Y_complex(input.P_23, input.P_23_inductive)

    Y_s_12_complex = complex(0, 1) * (
        -Y_12_complex.imag
        + Y_13_complex.real / math.sqrt(3)
        - Y_23_complex.real / math.sqrt(3)
    )
    Y_s_13_complex = complex(0, 1) * (
        -Y_13_complex.imag
        - Y_12_complex.real / math.sqrt(3)
        + Y_23_complex.real / math.sqrt(3)
    )
    Y_s_23_complex = complex(0, 1) * (
        -Y_23_complex.imag
        + Y_12_complex.real / math.sqrt(3)
        - Y_13_complex.real / math.sqrt(3)
    )

    def get_icr(Y_complex: complex):
        imag = Y_complex.imag
        imag_abs = abs(imag)
        omega = 2 * math.pi * input.f

        is_inductance = imag < 0

        value = 1 / (omega * abs(imag)) if is_inductance else imag_abs / omega

        return InductanceCapacitanceOutput(
            is_inductance=is_inductance,
            value=value,
        )

    icr_12 = get_icr(Y_s_12_complex)
    icr_13 = get_icr(Y_s_13_complex)
    icr_23 = get_icr(Y_s_23_complex)

    return SymmetrizationOutput(
        phi=phi,
        tan_phi=tg_phi,
        Y_1_complex=Y_12_complex,
        Y_2_complex=Y_13_complex,
        Y_3_complex=Y_23_complex,
        Y_s_12=Y_s_12_complex.imag,
        Y_s_13=Y_s_13_complex.imag,
        Y_s_23=Y_s_23_complex.imag,
        icr_12=icr_12,
        icr_13=icr_13,
        icr_23=icr_23,
    )


def get_latex_file_assignment(input: SymmetrizationInput) -> str:
    latex_str = r"""
    Mějme 3 fázovou nesymetrickou zátěž nazančenou na obrázku:
    \begin{center}
        \begin{circuitikz}[scale=0.8][european voltages]
            \draw
            (0,0)
            to [fullgeneric, *-, l_=$P_{1,3}$] (3,5)
            to [fullgeneric, *-, l_=$P_{1,2}$] (6,0)
            to [fullgeneric, *-, l_=$P_{2,3}$] (0,0);
            \nodesThreeF
        \end{circuitikz}
    \end{center}

    """

    latex_str += r"""
    Parametry:
    \begin{itemize}
    """

    def inductive_to_str(inductive: bool):
        return "induktivní" if inductive else "kapacitní"

    latex_str += (
        f"\\item $U = {common_utils.float_to_str(input.U, decimals=0)} \\fs \\uV$,\n"
    )
    latex_str += (
        f"\\item $f = {common_utils.float_to_str(input.f, decimals=0)} \\fs \\uHZ$,\n"
    )
    latex_str += f"\\item $\\cos (\\varphi) = {common_utils.float_to_str(input.cos_phi,decimals=1)}$,\n"
    latex_str += f"\\item $P_{{1,2}} = {common_utils.float_to_str(input.P_12 / 1000, decimals=0)} \\fs \\uKW$, {inductive_to_str(input.P_12_inductive)},\n"
    latex_str += f"\\item $P_{{1,3}} = {common_utils.float_to_str(input.P_13 / 1000, decimals=0)} \\fs \\uKW$, {inductive_to_str(input.P_13_inductive)},\n"
    latex_str += f"\\item $P_{{2,3}} = {common_utils.float_to_str(input.P_23 / 1000, decimals=0)} \\fs \\uKW$, {inductive_to_str(input.P_23_inductive)}."

    latex_str += r"""
    \end{itemize}

    """

    latex_str += "Proveďte výpočet symetrizačních admitancí $Y_{s,1,2}$, $Y_{s,1,3}$ a $Y_{s,2,3}$. "
    latex_str += "Nakreslete schéma zapojení symetrizačních admitancí. "
    latex_str += "Vypočtěte hodnoty indukčnosti, nebo kapacity pro každou symetrizační admitanci."

    return latex_str


def get_latex_file_solution(
    input: SymmetrizationInput, output: SymmetrizationOutput
) -> str:
    latex_str = "Nejprve získáme úhel $\varphi$:"
    latex_str += f"$$\\varphi = \\arccos({common_utils.float_to_str(input.cos_phi, decimals=1)}) = {common_utils.float_to_str(output.phi, decimals=3)}$$"

    latex_str += "Dále vypočítáme $\\te{tg} (\\varphi)$:"
    latex_str += "$$\\te{tg} (\\varphi) = \\tg (\\varphi) = "
    latex_str += f"{common_utils.float_to_str(output.tan_phi, decimals=3)}$$"

    latex_str += "Nyní vypočítáme komplexní admitance $Y_{1,2}$, $Y_{1,3}$ a $Y_{2,3}$:"
    latex_str += (
        "$$Y_{1,2} = \\frac{P_{1,2}}{U^2} \\left(1 + j \\tg (\\varphi) \\right) = "
    )

    return latex_str
