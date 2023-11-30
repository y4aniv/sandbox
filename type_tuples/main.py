def division_euclideienne(a, b):
    """
    :entrée a: int, b: int
    :sortie
    """
    q = a // b
    r = a % b
    return (q, r)

assert division_euclideienne(20, 3) == (6, 2)
assert type(division_euclideienne(20, 3)) == tuple


def parseNote(notes):
    N = ()
    for note in notes:
        if note != "abs":
            N += (int(note),)
    return N

assert parseNote((12, 14, 8, "abs", 15, 14, "abs")) == (12, 14, 8, 15, 14)
assert type(parseNote((12, 14, 8, "abs", 15, 14, "abs"))) == tuple
