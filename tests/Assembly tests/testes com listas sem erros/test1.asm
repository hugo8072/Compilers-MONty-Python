.section .data
t1: .int 0
t2: .int 2
t3: .float 0
t4: .float 0.0
t5: .int 0
t6: .float 0
array.length: .int 4
array: .float 1.0, 2.0, 5.3, 9.5
.section .text
.globl main
main:
    movl array.length, t1
    cmpl $0, t2
    jle L3
    cmpl $0, t2
    jle L3
L1:
    cmpl $0, t2
    jle L2
    movl t2, %eax
    addl 1, %eax
    movl %eax, t3
    movl t4, array[t2]
    jmp L1
L2:
    movl array.length, t5
    movl t5, %eax
    subl 1, %eax
    movl %eax, t6
    movl t6, array.length
    jmp L2
L3:

; Exit the program
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
