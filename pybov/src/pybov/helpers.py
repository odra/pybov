"""
Your usual "helpers" module to contain stuff that doesn't
fit anywhere else.
"""
def fill_str(s: str, full_size: int, char: str = ' ', order: int = 1) -> str:
    """
    Fills a string with extra characters based on full_size.

    This is used so data classes can convert themselves to the original
    string value they parsed from.
    """
    spaces = full_size - len(s)

    if spaces <= 0:
        return s

    filled = [char for c in range(0, spaces)]

    if order == 1:
        return ''.join([s] + filled)

    return ''.join(filled + [s])

