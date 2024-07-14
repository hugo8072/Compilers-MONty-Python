.section .data
t1: .int 0
t2: .int 2
t3: .float 0
t4: .float 0.0
t5: .int 0
t6: .float 0
list.length: .int 5
list: .float 1.3, 7.5, 3.1, 9.5, 1.0
.section .text
.globl main
main:
    movl list.length, t1
    movl t1, %eax
    subl 1, %eax
    movl %eax, t3
L1:
    cmpl $0, t3
    jle L2
    movl t4, list[t3 + 1]
    jmp L1
L2:
    movl list.length, t5
    movl t5, %eax
    addl 1, %eax
    movl %eax, t6
    movl t6, list.length

; Exit the program
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
