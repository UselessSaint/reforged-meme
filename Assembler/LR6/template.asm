StkSeg  SEGMENT PARA STACK 'STACK'
        DB      200h DUP (?)
StkSeg  ENDS
;
DataS   SEGMENT WORD 'DATA'

DataS   ENDS
;
Code    SEGMENT WORD 'CODE'
        ASSUME  CS:Code, DS:DataS


Code    ENDS
        END   DispMsg