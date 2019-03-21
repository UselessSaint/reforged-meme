EXTRN M1: near
EXTRN M2: near
EXTRN M3: near
EXTRN M4: near
EXTRN M5: near
EXTRN M6: near

StkSeg  SEGMENT PARA STACK 'STACK'
        DB      200h DUP (0)
StkSeg  ENDS

DataS   SEGMENT BYTE PUBLIC 'DATA'
	OFFM 	dw M1, M2, M3, M4, M5, M6
	N		db 0
DataS   ENDS

ASSUME  CS:Code, DS:DataS, SS:StkSeg
Code    SEGMENT BYTE PUBLIC 'CODE'
        
	main:
		mov AX, DataS
		mov DS, AX
		call M1
		
	menu:
		mov AH, 8
		int 21h
		mov AH, 2
		mov DL, AL
		int 21h
		
		cmp   AL, '8'                
		JA    menu
		CMP   AL, '0'
		JB    menu
		
		mov BX, 0
		mov BL, AL
		sub BL, '0'
		
		call OFFM[BX]

	exit:
		mov AH, 4Ch
		int 21h
Code    ENDS
        END   main