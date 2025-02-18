#!/bin/bash

./ghidra_11.3_PUBLIC/support/analyzeHeadless ./projects decompile -import ./programs/chall0.exe -overwrite -postScript decompile.py
#./ghidra_11.3_PUBLIC/support/analyzeHeadless ./projects decompile -process chall0.exe -postScript decompile.py