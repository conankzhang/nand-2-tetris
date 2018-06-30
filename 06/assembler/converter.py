class Converter:
    def convert_a_instruction(self, value):
        return format(value, '016b')

    def convert_c_instruction(self, dest, comp, jump):
        return "okay"