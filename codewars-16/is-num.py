def isDigit(string):
    try:
        string = float(string)
        return True
    except:
        return False
