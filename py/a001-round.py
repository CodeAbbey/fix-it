#!/usr/bin/env python3

while True:
    try:
        vals = [int(v) for v in input().split()]
        if len(vals) != 2:
            break
        print(round(vals[0] / vals[1]))
    except EOFError:
        break
