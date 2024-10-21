def array_to_latex_table(arr, caption):
    """
    Converts a 2D array to a LaTeX table.

    Args:
    arr (list): 2D array to be converted to LaTeX table.

    Returns:
    str: LaTeX table string.
    """
    table_str = ""

    for row in arr:
        table_str += "\\hline\n"
        row_str = " & ".join(map(str, row))
        table_str += row_str + "\\\\\n"

    table_str += "\\hline\n"

    return table_str
