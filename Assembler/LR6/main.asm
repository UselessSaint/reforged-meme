EXTRN M1: NEAR
EXTRN M2: NEAR
;EXTRN M3: NEAR
;EXTRN M4: NEAR
;EXTRN M5: NEAR
;EXTRN M6: NEAR

StkSeg  SEGMENT PARA STACK 'STACK'
        DB      200h DUP (?)
StkSeg  ENDS

DataS   SEGMENT BYTE PUBLIC
	X    DW 1
	OFFM DW M1, M2;, M3, M4, M5, M6 
DataS   ENDS
	
Code    SEGMENT BYTE PUBLIC 'CODE'
        ASSUME  CS:Code, DS:DataS

newline PROC NEAR
	PUSH  AX
	PUSH  DX

	MOV   AH,2
	MOV   DL,10
	INT   21h
	MOV   DL,13
	INT   21h

	POP   DX
	POP   AX
	RET
newline ENDP

DispMsg:
    mov   AX,DataS              
    mov   DS,AX                   
        
	CALL  M1
menu_loop:
	mov   AH, 8                    
	int   21h
	cmp   AL, '8'                  
	JA    menu_loop
	CMP   AL, '0'
	JB    menu_loop

	MOV   AH,2                    		
	MOV   DL,AL
	INT   21h

	CMP   AL, '8'                  
	JE    exit

	CALL  newline

	mov   BL, AL                   
	sub   BL, '0'
	ADD   BL, BL
	mov   BH, 0
	CMP   BL, 2
	JNE   skip
	PUSH  X
skip:
	CALL  OFFM[BX]

	CMP   BL, 2
	JNE   NOT_READ
	MOV   X, AX
	JMP   menu_loop
NOT_READ:
	ADD   SP, 2
	JMP   menu_loop               


exit:	
        mov   AH,4Ch                   
        int   21h                      
Code    ENDS
        END   DispMsg
