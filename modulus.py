#!/usr/bin/python3

def modulusDivision(__integer, __divisor):

    return [__integer//__divisor, __integer%__divisor]

def consoleIO():

    __integer = None
    __divisor = None

    print("Enter an integer to divide: ")
    __integer = int(input())
    print("Enter an integer divisor: ")
    __divisor = int(input())
    print("Answer: " + str(modulusDivision(__integer, __divisor)[0]) + " remainder " + str(modulusDivision(__integer, __divisor)[1]))

def main():

    from sys import exit
    from argparse import ArgumentParser

    __parser = ArgumentParser()
    __parser.add_argument("-i", "--integer", type=int, help="Integer to divide. Must be specified along with -i for non-interactive use.")
    __parser.add_argument("-d", "--divisor", type=int, help="Integer to divide by. Must be specified along with -d for non-interactive use.")
    __args = __parser.parse_args()

    if __args.integer is not None and __args.divisor is not None:
        print("Answer: " + str(modulusDivision(__args.integer, __args.divisor)[0]) + " remainder " + str(modulusDivision(__args.integer, __args.divisor)[1]))
    else:
        consoleIO()
    exit()

main()
