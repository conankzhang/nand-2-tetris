class Converter:
    def __init__(self):
        self.comp_table = {
            'A' : "0110000",
            'D+A' : "0000010",
            'D' : "0001100"
        }

        self.dest_table = {
            'D' : "010",
            'M' : "001"
        }

        self.jump_table = {
            'JGT' : "001",
        }

    def convert_a_instruction(self, value):
        return format(value, '016b')

    def convert_c_instruction(self, dest, comp, jump):
        begin = '111'
        comp_binary = self.comp_table[comp]
        dest_binary = self.dest_table[dest]
        jump_binary = "000"

        if jump is not None:
            jump = self.jump_table[jump]

        return begin + comp_binary + dest_binary + jump_binary