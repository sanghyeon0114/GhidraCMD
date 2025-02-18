#!/bin/bash

./ghidra/*/support/analyzeHeadless ./projects decompile -import $1 -overwrite -postScript decompile.py
#./ghidra/*/support/analyzeHeadless ./projects decompile -process chall0.exe -postScript decompile.py