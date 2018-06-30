class Converter:
    def convert_a_instruction(self, value):
        binary = format(value, "b")
        num_zeros = 16 - len(binary)