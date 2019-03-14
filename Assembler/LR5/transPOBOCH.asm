TITLE         Ã«ﬂ  ÃŒƒ”À‹ 1 À¿¡Œ–¿“Œ–Õ¿ﬂ –¿¡Œ“¿ 2 

     SSTACK     SEGMENT PARA STACK  'STACK'
                DB   64 DUP('—“≈ ____')
     SSTACK     ENDS

     DSEG          SEGMENT  PARA PUBLIC 'DATA'
     X         DB      1,2,3,4,5,0,0,1,2,3,4,5,0,0,1,2,3,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
     N         DB      3
     R		   DB      7
     DSEG          ENDS

SUBTTL         Œ—ÕŒ¬Õ¿ﬂ œ–Œ√–¿ÃÃ¿
PAGE
     CSEG      SEGMENT PARA PUBLIC 'CODE'
               ASSUME CS:CSEG,DS:DSEG,SS:SSTACK

     START     PROC FAR
               MOV  AX,DSEG				
               MOV  DS,AX
	
	 PREP:     MOV AL, R
			   DEC AL
			   
			   MOV BX, OFFSET X
			   ADD BL, R
			   DEC BX
			   
	           MOV CL, N
	           ;DEC CL
	           
	 VNESS:	   PUSH CX
			   
			   MOV CL, AL
			   
			   MOV DI, 7
			   MOV SI, -1
     
     VNUS:     PUSH DI
			   ;ADD DI, SI
			   
			   MOV DL, [BX][SI]
			   XCHG DL, [BX][DI]
			   MOV [BX][SI], DL
 
			   POP DI
			   
			   DEC SI
			   ADD DI, 7
			   
			   LOOP VNUS
			   
			   DEC AL
			   ADD BX, 6
			   
			   POP CX
			   
			   LOOP VNESS
			   
				
     M6:       MOV  AH,4CH
               MOV  AL,0
               INT 21H
     START     ENDP

     CSEG      ENDS
               END  START
