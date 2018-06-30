import sys
from assembler.assembler import Assembler

def main():
    assembler = Assembler(sys.argv[1])
    assembler.assemble()

if __name__ == "__main__":
    main()