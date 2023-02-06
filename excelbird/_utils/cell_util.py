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


def format_formula(s: str) -> str:
    """
    The last step in finalizing a formula. Attempting to correct
    user mistakes, trailing commas, unwanted spaces, etc. Assume
    the function is fully built, starts with '=', and all functions
    are prefixed with '_xlfn.'
    """
    s = re.sub(r"\([, ]+", r"(", s)  # comma before opening paren
    s = re.sub(r"[, ]+\)", r")", s) # trailing comma before closing paren
    s = re.sub(r"^= +", "=", s)  # leading space
    s = re.sub(r"[, ]+$", "", s)  # trailing comma
    s = re.sub(r"= *'(.*?)'", r'="\1"', s)  # using single quotes instead of double
    return s


def prefix_formulae_funcs(func: str) -> str:
    """
    Openpyxl will insert '@' before any function it doesn't think is a valid
    excel function. Its list of functions is outdated, so newer functions, like "CONCAT"
    will be interpreted as invalid incorrectly.

    Our solution is to find functions in the string, where there are capital letters, dots,
    or digits, followed by a starting parenthese, check if they are in openpyxl's
    `FORMULAE`, and if not, prefix them with "_xlfn."
    """

    matches = re.findall(r"([A-Z\.a-z0-9]+)\(", func)
    # matches = re.findall(r"^([A-Z\.0-9]+)\(", func) + re.findall(r"(?<![^\.A-Za-z0-9])([A-Za-z\.0-9]+)\(", func)
    matches = set([match for match in matches if match.upper() in FORMULAE])
    for match in matches:
        func = func.replace(match + "(", "_xlfn." + match + "(")
    return func
