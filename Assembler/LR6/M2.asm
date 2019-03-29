PUBLIC M2				;returns number through AX

ASSUME  CS:Code
Code    SEGMENT BYTE PUBLIC 'CODE'
	M2: 
		PUSH   BX
		PUSH   DX
		PUSH   SI

		MOV    AX, 0
		MOV    BX, 0
		
		MOV    AH, 2
		MOV    DL, 10
		INT    21h
		MOV    DL, 13
		INT    21h
		MOV    DX, 0

	INP_LOOP:
		MOV    AH, 1
		INT    21h

		CMP    AL, 13
		JE     exit
		
		CMP    AL, 2Dh                   ;if symbol equals '-'
		JNE    READ_DIGIT
		MOV    SI, 1
		JMP    INP_LOOP

	READ_DIGIT:
		SUB    AL, '0'
		MOV    AH, 0
		XCHG   BX, AX
		MOV    DX, 10
		MUL    DX	
		ADD    BX, AX                    ;BX = current digit * 10 + old number
		JMP    INP_LOOP	

	exit:
		MOV    AX, BX
		CMP    SI, 1
		JNE    POSITIVE
		NEG    AX
		
	POSITIVE:
		POP    SI
		POP    DX
		POP    BX
		PUSH   AX                        ;save number to AX
		PUSH   DX

		MOV    AH, 2
		MOV    DL, 10
		INT    21h
		MOV    DL, 13
		INT    21h

		POP    DX
		POP    AX
		
		RET
Code    ENDS
	END