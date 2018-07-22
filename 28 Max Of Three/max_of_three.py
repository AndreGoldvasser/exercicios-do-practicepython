# Implement a function that takes as input three variables, and returns the largest of the three. Do this without
# using the Python max() function!
# The goal of this exercise is to think about some internals that Python normally takes care of for us.
# All you need is some variables and if statements!
def main():
    print(maior_dos_tres(128,992,56))


def maior_dos_tres(first,second,third):
    if first >= second and third:
        return first
    elif second >= first and third:
        return second
    else:
        return second


if __name__ == '__main__':
    main()