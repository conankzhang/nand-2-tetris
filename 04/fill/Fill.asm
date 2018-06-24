// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
 (INIT)
     @SCREEN
     D=A
     @screenAddress
     M=D // screenAddress = 16384

    @i
    M = 0 // i = 0 (row 0 of display)

    @8191
    D = A
    @n
    M = D // n = 8192 (number of pixel words in display)

    @KBD
    D=M
    @PRESSED
    D;JGT // keyAddress > 0 goto PRESSED

    @color
    M = 0 // color = 0 (white)
    @LOOP
    0;JMP // goto LOOP

(PRESSED)
    @color
    M = -1 // color = -1 (black)

(LOOP)
    @i
    D=M
    @n
    D=D-M
    @INIT
    D;JGT // if i > goto INIT 

    @color
    D=M
    @screenAddress
    A=M
    M=D // RAM[screenAddress]=color

    @i
    M=M+1 // i = i + 1

    @screenAddress
    M=M+1 // screenAddress = screenAddress + 1 (move to next screenAddress word)
    @LOOP
    0;JMP