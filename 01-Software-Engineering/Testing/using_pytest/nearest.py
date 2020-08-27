def nearest_square(num):
    """ return the nearest perfect square
    that is less than or equal to the number """
    root = 0
    while ((root + 1) ** 2 <= num):
        root +=1

    return root ** 2


# test it in python environment:
# >>> from nearest import nearest_square
# >>> nearest_square(5)