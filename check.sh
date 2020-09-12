#!/usr/bin/env bash

pushd py/test
./a001.sh
res=$?
popd
exit $res