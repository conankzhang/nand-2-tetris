from assembler.converter import Converter

class Parser:
    def __init__(self):
        self.converter = Converter()

    def parse(self, line):
        if line.startswith('@'):
            return self._parse_a_instruction(line)
        else:
            return self._parse_c_instruction(line)

    def _parse_a_instruction(self, line):
        value = int(line[1:])
        return self.converter.convert_a_instruction(value)

    def _parse_c_instruction(self, line):
        begin = '111'
        dest = line[:line.index("=")]
        comp = line[line.index("=")+1:]
        jump = None

        if line.find(";") is not -1:
            comp = line[line.index("=")+1:line.index(";")]
            jump = line[line.index(";")+1:]

        return self.converter.convert_c_instruction(dest, comp, jump)