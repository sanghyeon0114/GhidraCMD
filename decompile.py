from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

programName = currentProgram

decompinterface = DecompInterface()
binaryName = programName.getName()
decompinterface.openProgram(programName);
print('[*] Binary Name : '+str(binaryName))

functions = programName.getFunctionManager().getFunctions(True)

for function in list(functions):
    print("[*] Function Found : "+str(function))
    tokengrp = decompinterface.decompileFunction(function, 0, ConsoleTaskMonitor())
    #print(tokengrp.getDecompiledFunction().getC())