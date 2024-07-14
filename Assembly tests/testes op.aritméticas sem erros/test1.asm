.section .data
x: .int 5
y: .float 3.0
t1: .float 0
a: .float 0
t2: .float 0
b: .float 0
t3: .float 0
c: .float 0
t4: .float 0
d: .float 0

.section .text
.globl main
main:
    movl (float) x, %eax
    imull y, %eax
    movl %eax, t1
    movl t1, a
    movl (float) x, %eax
    addl y, %eax
    movl %eax, t2
    movl t2, b
    movl (float) x, %eax
    subl y, %eax
    movl %eax, t3
    movl t3, c
    movl (float) x, %eax
    cdq
    idivl y
    movl %eax, t4
    movl t4, d

; Exit the program
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
