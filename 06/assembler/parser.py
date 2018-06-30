class Parser:
    def parse(self, line):
        if line[0] == '@':
            self._parse_a_instruction(line)
        else:
            self._parse_c_instruction(line)

    def _parse_a_instruction(self, line):
        print('yay')

    def _parse_c_instruction(self, line):
        print('k')