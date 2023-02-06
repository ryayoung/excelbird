import re
from excelbird._formulae import FORMULAE

def main():

    func = """
    something + something 
    and then
    something else      is new
    here is ## not a comment

    here IS a comment,# some comment stuff
    another comment # stuff!
    And an ending comment # Thanks"""
    # print(format_string(func) + "X")
    s = "MAX(HOLIDAYS = 'O', h)"
    print(format_formula(s))



def format_string(s):
    if not isinstance(s, str):
        return s
    # Remove comments from end of string
    s = re.sub(r"#+.*?$", "", s)
    # Remove comments at the end of lines
    s = re.sub(r"#+.*?\n", " ", s)
    # Remove whitespace
    s = re.sub(r"\s+", " ", s)
    return s



def format_formula(s):
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



main()


    # s = """= _xlfn.MAX(, _xlfn.NETWORKDAYS(,,( _xlfn.MAX(B10, I13), J13, _xlfn.IF( _xlfn.OR(G13 = "O", G13="U-N"), 0, 'EY Holidays'!A2:'EY Holidays'!A31 ), ), 0 ) , """

