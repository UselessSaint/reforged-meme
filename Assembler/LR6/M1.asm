PUBLIC	M1

DataMenu   SEGMENT BYTE PUBLIC 'DATA'
	menu	db 13, 10
			db "'0' Print menu.", 13, 10
			db "'1' Enter number", 13, 10
			db "'2' __________", 13, 10
			db "'3' __________", 13, 10
			db "'4' __________", 13, 10
			db "'5' __________", 13, 10
			db "'6' __________", 13, 10
			db "'7' __________", 13, 10
			db "'8' Exit.", 13, 10
			db "Choose: "
			db "$"
DataMenu   ENDS

ASSUME	CS:CSEG, DS:DataMenu

CSEG	SEGMENT byte PUBLIC 'CODE'
	M1:
		;push AX
		;push DX
		
		;mov DX, offset menu
		;mov AH, 9
		;int 21h
		
		;pop DX
		;pop AX
		ret
CSEG	ENDS
	END