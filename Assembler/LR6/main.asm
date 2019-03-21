EXTRN M1: near
EXTRN M2: near
EXTRN M3: near
EXTRN M4: near
EXTRN M5: near
EXTRN M6: near

StkSeg  SEGMENT PARA STACK 'STACK'
        DB      200h DUP (?)
StkSeg  ENDS
;
DataS   SEGMENT BYTE PUBLIC 'DATA'
	menu	db "'0' Print menu", 13, 10
		db "'1' Print menu", 13, 10
		db "'2' Print menu", 13, 10
		db "Choose: ", 13, 10
		db "$"
		
	OFFM 	dw M1, M2, M3, M4, M5, M6
	N	db 0

DataS   ENDS
;
Code    SEGMENT BYTE PUBLIC 'CODE'
        ASSUME  CS:Code, DS:DataS, SS:StkSeg
main:
        mov   AX,DataS
        mov   DS,AX    

	mov DX, OFFSET menu
	mov AH, 9
	int 21h

	mov BH, 0
	mov BL, N
	call OFFM[BX]

	mov AH, 4Ch
	int 21h

Code    ENDS
        END   main