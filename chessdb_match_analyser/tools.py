def getSideToMoveFromFEN(s):
    if 'w' in s.split(" "):
        return True
    else:
        return False