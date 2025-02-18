import logging
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor

class Log():
    file_path = './logs/'

    def __init__(self, binary_name):
        self.log = logging.getLogger()
        self.log.setLevel(logging.INFO)
        self.binary_name = binary_name
        file_handler = logging.FileHandler('{}{}.log'.format(self.file_path, str(self.binary_name)))
        self.log.addHandler(file_handler)
        self.log.info('[*] binary Name : ' + str(self.binary_name) + '\n')

    def loggingFunction(self, function_name, decompile_info):
        self.log.info("---------------- [*] Function : "+str(function_name) + " ----------------")
        self.log.info(decompile_info)

class Ghidra():
    def __init__(self):
        self.program = currentProgram
        self.decomp_interface = DecompInterface()
        self.decomp_interface.openProgram(self.program);
        self.program_name = self.program.getName()
        self.functions = self.program.getFunctionManager().getFunctions(True)

    def getProgramName(self):
        return self.program_name
    
    def getFunctions(self):
        return self.functions
    
    def decompileFunctions(self, function):
        tokengrp = self.decomp_interface.decompileFunction(function, 0, ConsoleTaskMonitor())
        decompile_func = tokengrp.getDecompiledFunction().getC()
        return decompile_func
    
def main():
    log = Log(program_name)

    ghidra = Ghidra()
    program_name = ghidra.getProgramName()

    for function in ghidra.getFunctions():
        decompile_func = ghidra.decompileFunctions(function)
        log.loggingFunction(function, decompile_func)
        
if __name__ == '__main__':
    main()