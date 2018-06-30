class Converter:
    def __init__(self):
        self.comp_table = {
            '0' : "0101010",
            '1' : "0111111",
            '-1' : "0111010",
            'D' : "0001100",
            'A' : "0110000",
            '!D' : "0001101",
            '!A' : "0110001",
            '-D' : "0001111",
            '-A' : "0110011",
            'D+1' : "0011111",
            'A+1' : "0110111",
            'D-1' : "0001110",
            'A-1' : "0110010",
            'D+A' : "0000010",
            'D-A' : "0010011",
            'A-D' : "0000111",
            'D&A' : "0000000",
            'D|A' : "0010101",
            'M' : "1110000",
            '!M' : "1110001",
            '-M' : "1110011",
            'M+1' : "1110111",
            'M-1' : "1110010",
            'D+M' : "1000010",
            'D-M' : "1010011",
            'M-D' : "1000111",
            'D&M' : "1000000",
            'D|M' : "1010101"
        }

        self.dest_table = {
            'M' : "001",
            'D' : "010",
            'MD' : "011",
            'A' : "100",
            'AM' : "101",
            'AD' : "110",
            'AMD' : "111"
        }

        self.jump_table = {
            'JGT' : "001",
            'JEQ' : "010",
            'JGE' : "011",
            'JLT' : "100",
            'JNE' : "101",
            'JLE' : "110",
            'JMP' : "111"
        }

        self.symbol_table = {
            'R0' : "0",
            'R1' : "1",
            'R2' : "2",
            'R3' : "3",
            'R4' : "4",
            'R5' : "5",
            'R6' : "6",
            'R7' : "7",
            'R8' : "8",
            'R9' : "9",
            'R10' : "10",
            'R11' : "11",
            'R12' : "12",
            'R13' : "13",
            'R14' : "14",
            'R15' : "15",
            'SCREEN' : "16384",
            'KBD' : "24576",
            'SP' : "0",
            'LCL' : "1",
            'ARG' : "2",
            'THIS' : "3",
            'THAT' : "4"
        }
        self.symbol_counter = 16;

    def convert_a_instruction(self, value):
        return format(value, '016b')

    def convert_c_instruction(self, dest, comp, jump):
        begin = '111'
        comp_binary = self.comp_table[comp]
        dest_binary = "000"
        jump_binary = "000"

        if dest is not None:
            dest_binary = self.dest_table[dest]

        if jump is not None:
            jump_binary = self.jump_table[jump]

        return begin + comp_binary + dest_binary + jump_binary

    def convert_symbol(self, line, line_number):
        symbol_binary = self.symbol_table.get(line)
        if symbol_binary is None:
            if line.startswith('('):
                self.symbol_table[line] = line_number + 1
                symbol_binary = self.symbol_table[line]
            else:
                self.symbol_table[line] = self.symbol_counter
                self.symbol_counter += 1

                symbol_binary = self.symbol_table[line]

        return format(symbol_binary, '016b')