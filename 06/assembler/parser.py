class Parser:
    def parse(self, line):
        if line[0] == '@':
            __parse_a_instruction(line)
        else:
            __parse_c_instruction(line)

    def __parse_a_instruction(self, line):
        print('yay')

    def __parse_c_instruction(self, line):
        print('k')