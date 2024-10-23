from app.modules.symmetrization import symmetrization
from app.modules.symmetrization.inputs.symmetrization_input import SymmetrizationInput
from app.shared.consts import path_consts

symmetrization_input = SymmetrizationInput(
    U=400,
    f=50,
    cos_phi=0.8,
    P_12=63000,
    P_13=28000,
    P_23=26000,
    P_12_inductive=True,
    P_13_inductive=True,
    P_23_inductive=False,
)

symmetrization_output = symmetrization.symmetrize(symmetrization_input)

assignment_latex = symmetrization.get_latex_file_assignment(symmetrization_input)
solution_latex = symmetrization.get_latex_file_solution(
    symmetrization_input, symmetrization_output
)

folder_path = path_consts.ROOT_FOLDER_PATH / "tex" / "en3" / "res"

with open(folder_path / "symmetrization_assignment_1.tex", "w") as f:
    f.write(assignment_latex)

with open(folder_path / "symmetrization_solution_1.tex", "w") as f:
    f.write(solution_latex)
