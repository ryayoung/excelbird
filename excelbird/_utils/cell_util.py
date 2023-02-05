import re
from excelbird._formulae import FORMULAE

def remove_paren_enclosure(value: str) -> str:
    if not isinstance(value, str):
        return value
    if value.startswith("(") and value.endswith(")"):
        return value.removeprefix("(").removesuffix(")")
    return value


def autofit_algorithm(value: str) -> int:
    """
    Decides column width given string value of a cell
    """
    filtered_value = str(value).replace("_xlfn.", "")
    length_coef = len(filtered_value)
    with_lower_bound = max(length_coef, 10)
    with_upper_bound = min(with_lower_bound, 40)
    return with_upper_bound


def approximate_arial_string_width(st):
    import string
    size = 0 # in milinches
    for s in st:
        if s in 'lij|\' ': size += 37
        elif s in '![]fI.,:;/\\t': size += 50
        elif s in '`-(){}r"': size += 60
        elif s in '*^zcsJkvxy': size += 85
        elif s in 'aebdhnopqug#$L+<>=?_~FZT' + string.digits: size += 95
        elif s in 'BSPEAKVXY&UwNRCHD': size += 112
        elif s in 'QGOMm%W@': size += 135
        else: size += 50
    return size * 6 / 1000.0 # Convert to picas


def prefix_formulae_funcs(func: str) -> str:
    """
    Openpyxl will insert '@' before any function it doesn't think is a valid
    excel function. Its list of functions is outdated, so newer functions, like "CONCAT"
    will be interpreted as invalid incorrectly.

    Our solution is to find functions in the string, where there are capital letters, dots,
    or digits, followed by a starting parenthese, check if they are in openpyxl's
    `FORMULAE`, and if not, prefix them with "_xlfn."
    """
    # First, capture a group at the START of the string, if present.
    # Add additional matches which do NOT start with a period. This serves two purposes:
    #   - Avoids capturing when func is already prefixed with _xlfn. (shouldn't happen, but just in case)
    #   - Avoids capturing midway through a function that has periods in it, like "BINOM.DIST"
    matches = re.findall(r"^([A-Z\.0-9]+)\(", func) + re.findall(r"[^\.]([A-Za-z\.0-9]+)\(", func)
    for match in matches:
        if match.upper() in FORMULAE:
            func = func.replace(match + "(", "_xlfn." + match + "(")
    return func
