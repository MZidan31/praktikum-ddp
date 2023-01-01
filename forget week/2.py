#fungsi tambah
def sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result

#fungsi kurang
def sub(*args):
    result = args[0]
    for arg in args[1:]:
        result -= arg
    return result

#fungsi kali
def times(*args):
    result = 1
    for arg in args:
        result *= arg
    return result