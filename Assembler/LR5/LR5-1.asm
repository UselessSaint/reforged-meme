SSEG	SEGMENT PARA STACK 'STACK'
		DB 64 DUP(?)
SSEG	ENDS

DSEG	SEGMENT PARA PUBLIC 'DATA'
	X	DB	1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5
	N	DB	5
DSEG	ENDS

CSEG	SEGMENT PARA PUBLIC 'CODE'
		ASSUME CS:CSEG,DS:DSEG,SS:SSEG
		
main:	mov AX, DSEG
		mov DS, AX
		
		mov AL, 4
		mov BX, offset X
		
		mov CL, N
		dec CL
		
outloop:
		push CX
		
		mov CL, AL
		
		mov DI, 4
		mov SI, 1
		
inloop:
		push DI
		add DI, SI
		
		mov DL, [BX][SI]
		xchg DL, [BX][DI]
		mov [BX][SI], DL
		
		pop DI
		
		add DI, 3
		inc SI
		loop inloop
		
		dec AL
		add BX, 5
		pop CX
		loop outloop
		
finish:
		mov AH, 4ch
		mov AL, 0
		int 21h
		
CSEG ENDS
		END main
		
		