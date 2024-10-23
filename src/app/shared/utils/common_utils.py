def float_to_str(number: float, decimals: int = 3) -> str:
    return f"{number:.{decimals}f}"


def complex_to_str(number: complex, decimals: int = 3) -> str:
    if number.imag < 0:
        return f"{number.real:.{decimals}f} - {abs(number.imag):.{decimals}f}j"

    return f"{number.real:.{decimals}f} + {number.imag:.{decimals}f}j"
