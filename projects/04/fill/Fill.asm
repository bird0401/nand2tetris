(KI)
    @cnt
    M=0
    @KBD
    D=M
    @WHITE
    D;JEQ
(BLACK)
    @8192
    D=A
    @cnt
    D=D-M
    @ENDL
    D;JEQ
    @cnt
    D=M
    @SCREEN
    A=A+D
    M=-1
    @cnt
    M=M+1
    @BLACK
    0;JMP
(WHITE)
    @8192
    D=A
    @cnt
    D=D-M
    @ENDL
    D;JEQ
    @cnt
    D=M
    @SCREEN
    A=A+D
    M=0
    @cnt
    M=M+1
    @WHITE
    0;JMP
(ENDL)
@KI
0;JMP