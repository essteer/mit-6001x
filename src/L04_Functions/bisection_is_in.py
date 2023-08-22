def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    if aStr == "":
        return False

    elif len(aStr) == 0:
        if char == aStr:
            return True
        else:
            return False

    elif char == aStr[int(len(aStr)/2)]:
        return True

    elif char < aStr[int(len(aStr)/2)]:
        return isIn(char, (aStr[:int(len(aStr)/2)]))

    elif char > aStr[int(len(aStr)/2)]:
        return isIn(char, (aStr[int(len(aStr)/2) + 1:]))
