#!/usr/bin/env bash

read -d '' INPUT << EOT
4 3
5 3
5 2
6 2
7 2
10 4
EOT

read -d '' EXPECT << EOT
1
2
3
3
4
3
EOT

RESULT=$(python3 ../a001-round.py <<< "$INPUT")

if [[ "$RESULT" != "$EXPECT" ]] ; then
    echo "Too bad"
    exit 1
else
    echo "Passed"
fi