#!/usr/bin/env bash
if uname -m | grep 64
then
	export LD_LIBRARY_PATH=./Engines/Linux64
else
	export LD_LIBRARY_PATH=./Engines/Linux32
fi

python ./Lucas.py
