#!/bin/bash

./ghidra_11.3_PUBLIC/support/analyzeHeadless ./projects decompile -import ./programs/chall0.exe -overwrite -postScript decompile.py