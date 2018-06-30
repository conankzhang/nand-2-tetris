import os
from assembler.parser import Parser 

class Assembler:
    def __init__(self, file):
        self.file = file

    def assemble(self):
        file_in = open(self.file, 'r')

        file_name = os.path.splitext(file_in.name)[0]
        file_out = open(file_name + '.hack', 'w')

        parser = Parser()
        for line in file_in:
            if not line.isspace() and not line.startswith('/'):
                instruction = parser.parse(line)

                if instruction is not None:
                    file_out.write(instruction)
                    file_out.write('\n')
