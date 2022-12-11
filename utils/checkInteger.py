def checkInteger(lst):

    for number in lst:
        if type(number) is not int:
            return False
        
    return True