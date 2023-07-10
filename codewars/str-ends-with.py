def solution(text, ending):
    try:
        return text.index(ending) != -1 and text[-1] == ending[-1]
    except ValueError:
        return False

# Better


def solution(string, ending):
    return string.endswith(ending)
