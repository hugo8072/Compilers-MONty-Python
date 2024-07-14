.section .data
x: .int 3
t1: .float 0
t2: .float 0
t3: .float 0
t4: .float 0
t5: .float 1.0
t6: .float 100.0
t7: .float 0

.section .text
.globl main
main:
    movl x, %eax
    imull x, %eax
    movl %eax, t1
    movl t1, %eax
    imull x, %eax
    movl %eax, t2
    movl t2, %eax
    imull x, %eax
    movl %eax, t3
    movl t3, %eax
    imull x, %eax
    movl %eax, t4
    movl t4, x
    movl x, t7
L1:
    cmpl $0, t6
    jle L2
    movl t5, %eax
    imull t7, %eax
    movl %eax, t5
    movl t6, %eax
    subl 1, %eax
    movl %eax, t6
    jmp L1
L2:
    movl t5, x

; Exit the program
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
