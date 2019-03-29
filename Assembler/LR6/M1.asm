PUBLIC M1

DataS   SEGMENT PUBLIC
	MENU DB "'0' Print menu", 13, 10
	     DB "'1' Enter number", 13, 10
	     DB "'2' Some action", 13, 10
		 DB "'3' ___________", 13, 10
		 DB "'4' ___________", 13, 10
		 DB "'5' ___________", 13, 10
		 DB "'6' ___________", 13, 10
		 DB "'7' ___________", 13, 10
		 DB "'8' Exit", 13, 10
		 DB "Choose action"
	     DB "$"
DataS   ENDS

ASSUME  CS:Code, DS:DataS
Code    SEGMENT BYTE PUBLIC 'CODE'
     M1: 
		PUSH  AX
		PUSH  DX

		mov   DX,OFFSET MENU
		mov   AH,9
		int   21h 

		POP   DX
		POP   AX
		RET
Code    ENDS
	END