CSEG SEGMENT
ASSUME CS:CSEG, DS:CSEG, SS:CSEG
ORG 100h

inicio:
    jmp juego_main


ancho           db 80
alto            db 25
dir             db 1    
snake_lon       dw 3    
snake_pos       dw 1000, 998, 996, 197 dup(0) 
comida_pos      dw 1200
msg_gameover    db " GAME OVER - press esc to leave"


juego_main:
    mov ax, 0003h
    int 10h

    mov ah, 01h
    mov cx, 2607h
    int 10h

game_loop:
    mov ah, 01h
    int 16h
    jz mover_serpiente  

    mov ah, 00h         
    int 16h

    cmp ah, 48h         ; up
    je set_arriba
    cmp ah, 4Dh         ; right
    je set_derecha
    cmp ah, 50h         ; down
    je set_abajo
    cmp ah, 4Bh         ; left
    je set_izquierda
    cmp al, 27          ; ESC
    je ir_a_salir
    jmp mover_serpiente

ir_a_salir:
    jmp salir

set_arriba:    
    mov [dir], 0 
    jmp mover_serpiente
set_derecha:   
    mov [dir], 1 
    jmp mover_serpiente
set_abajo:     
    mov [dir], 2 
    jmp mover_serpiente
set_izquierda: 
    mov [dir], 3

mover_serpiente:
    mov cx, [snake_lon]
    dec cx              
    mov si, cx
    shl si, 1           

actualizar_cuerpo_loop:
    mov ax, [snake_pos + si - 2]
    mov [snake_pos + si], ax
    sub si, 2
    loop actualizar_cuerpo_loop

    mov ax, [snake_pos] 
    mov bl, [dir]
    
    cmp bl, 0
    je mov_arriba
    cmp bl, 1
    je mov_derecha
    cmp bl, 2
    je mov_abajo
    cmp bl, 3
    je mov_izquierda
    jmp verificar_comida

mov_arriba:    
    sub ax, 160 
    jmp verificar_comida 
mov_derecha:   
    add ax, 2   
    jmp verificar_comida 
mov_abajo:     
    add ax, 160 
    jmp verificar_comida
mov_izquierda: 
    sub ax, 2

verificar_comida:
    mov [snake_pos], ax 

    mov bx, [comida_pos]
    cmp ax, bx
    jne dibujar_todo

    inc word [snake_lon]
    add word [comida_pos], 444
    cmp word [comida_pos], 3800 
    jl dibujar_todo
    sub word [comida_pos], 3000

dibujar_todo:
    mov ax, 0B800h
    mov es, ax

    mov cx, 2000
    xor di, di
    mov ax, 0020h 
limpiar_loop:
    mov es:[di], ax
    add di, 2
    loop limpiar_loop

   
    mov di, [comida_pos]
    mov ax, 0C0Fh
    mov es:[di], ax

    mov cx, [snake_lon]
    xor si, si
    mov ax, 0A02h
dibujar_snake_loop:
    mov di, [snake_pos + si]
    mov es:[di], ax
    add si, 2
    loop dibujar_snake_loop

    ; Delay
    mov ah, 86h
    mov cx, 0001h       
    mov dx, 8480h       
    int 15h

    jmp game_loop       

gameover:
    mov ax, 0003h
    int 10h
    mov ah, 09h
    mov dx, offset msg_gameover
    int 21h

esperar_esc:
    mov ah, 00h
    int 16h
    cmp al, 27
    jne esperar_esc

salir:
    mov ax, 0003h
    int 10h
    mov ax, 4C00h
    int 21h

CSEG ENDS
END inicio