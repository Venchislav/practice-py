# replace letters to each other from dict or from maketrans() table
def switcheroo(s):
    return s.translate(s.maketrans('ab', 'ba'))
