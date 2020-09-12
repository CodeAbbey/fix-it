#!/usr/bin/env python3

def my_round(x):
    """
    Rounds to nearest integer, in case of exact half (3.5, 10.5 etc) rounds up
    as taught in school
    """
    return round(x)

def main():
    """
    Reads two values A and B from each line, outputs A / B rounded
    """
    while True:
        try:
            vals = [int(v) for v in input().split()]
            if len(vals) != 2:
                break
            print(my_round(vals[0] / vals[1]))
        except EOFError:
            break

if __name__ == '__main__':
    main()
