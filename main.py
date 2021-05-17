# FUNCTION THAT TAKES 3 PARAS AND COMPRES TWO OF THEM

def compare(x, y, z):
    if  int(x) == int(y) or int(x) == int(z) or int(y) == int(z):
        return True
    else:
        return False

compare(2, "10", 2)