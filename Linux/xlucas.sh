#!/usr/bin/env bash
if uname -m | grep 64
then
	export LD_LIBRARY_PATH=../Engines/Linux64/_tools
else
	export LD_LIBRARY_PATH=../Engines/Linux32/_tools
fi

python ../Lucas.py
