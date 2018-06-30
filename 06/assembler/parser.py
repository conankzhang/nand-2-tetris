from assembler.converter import Converter

class Parser:
    def __init__(self):
        self.converter = Converter()

    def parse(self, line, line_number):
        if line.startswith('@') or line.startswith('('):
            return self._parse_a_instruction(line, line_number)
        else:
            return self._parse_c_instruction(line)

    def _parse_a_instruction(self, line, line_number):
        symbol = None
        if line.startswith('('):
            symbol = line[line.index("(")+1:line.index(")")].strip()
        else:
            symbol = line[line.index("@")+1:].strip()

        if symbol.isdigit():
            value = int(line[1:])
            return self.converter.convert_a_instruction(value)
        else:
            return self.converter.convert_symbol(line, line_number)

    def _parse_c_instruction(self, line):
        dest = None
        comp = None
        if line.find("=") is not -1:
            dest = line[:line.index("=")].strip()
            comp = line[line.index("=")+1:].strip()

            if line.find("/") is not -1:
                comp = line[line.index("=")+1:line.index("/")].strip()

        jump = None

        if line.find(";") is not -1:
            jump = line[line.index(";")+1:].strip()
            comp = line[:line.index(";")].strip()

            if line.find("/") is not -1:
                jump = line[line.index(";")+1:line.index("/")].strip()

            if line.find("=") is not -1:
                comp = line[line.index("=")+1:line.index(";")].strip()

        return self.converter.convert_c_instruction(dest, comp, jump)