
def hello(name: str):  # give hint about input data type
    print(f"Hello {name}")


def addition(int1, int2):
    return int1 + int2


def division(int1, int2) -> float:  # To give hints of what the output will be
    return int1/int2


def division1(int1=8, int2=4):  # to give default for any of the arguments
    return int1/int2
# int1:int=9 to add default and hints


