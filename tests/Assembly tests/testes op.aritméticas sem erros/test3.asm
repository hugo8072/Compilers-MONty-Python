.section .data
a: .int 5
b: .float 6.2
c: .int -4
d: .float 5.3
t1: .float 0
t2: .float 1.0
t3: .float 99.0
t4: .float 0
t5: .float 0
t6: .float 1.0
t7: .float 0
t8: .float 0
t9: .float 0
z: .float 0

.section .text
.globl main
main:
    movl 1, %eax
    addl b, %eax
    movl %eax, t1
    movl c, t4
L1:
    cmpl $0, t3
    jle L2
    movl t2, %eax
    imull t4, %eax
    movl %eax, t2
    movl t3, %eax
    subl 1, %eax
    movl %eax, t3
    jmp L1
L2:
    movl t1, %eax
    addl t2, %eax
    movl %eax, t5
    movl a, t7
    movl d, t8
    cmpl $0, t7
    jle L4
L3:
    cmpl $0, t7
    jle L7
    movl t6, %eax
    imull t8, %eax
    movl %eax, t6
    movl t7, %eax
    subl 1, %eax
    movl %eax, t7
    jmp L3
L4:
L5:
    cmpl $0, t7
    jle L6
    movl t6, %eax
    imull t8, %eax
    movl %eax, t6
    movl t7, %eax
    subl 1, %eax
    movl %eax, t7
    jmp L5
L6:
    movl 1, %eax
    cdq
    idivl t6
    movl %eax, t6
L7:
    movl t5, %eax
    addl t6, %eax
    movl %eax, t9
    movl t9, z

; Exit the program
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
