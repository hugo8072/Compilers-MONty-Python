.section .data
a: .int 5
b: .float 6.2
c: .int -4
d: .float 5.3
t1: .float 0
t2: .float 0
t3: .float 0
t4: .float 0
t5: .float 0
t6: .float 0
t7: .float 0
t8: .float 0
t9: .float 0
t10: .float 0
t11: .float 0
t12: .float 0
t13: .float 0
z: .float 0

.section .text
.globl main
main:
    movl b, %eax
    imull (float) c, %eax
    movl %eax, t1
    movl a, %eax
    addl t1, %eax
    movl %eax, t2
    movl (float) a, %eax
    addl b, %eax
    movl %eax, t3
    movl t2, %eax
    cdq
    idivl t3
    movl %eax, t4
    movl 45, %eax
    cdq
    idivl 22
    movl %eax, t5
    movl t5, %eax
    imull c, %eax
    movl %eax, t6
    movl t6, %eax
    imull a, %eax
    movl %eax, t7
    movl t7, %eax
    imull d, %eax
    movl %eax, t8
    movl c, %eax
    addl c, %eax
    movl %eax, t9
    movl t9, %eax
    addl d, %eax
    movl %eax, t10
    movl t10, %eax
    addl a, %eax
    movl %eax, t11
    movl t8, %eax
    cdq
    idivl t11
    movl %eax, t12
    movl t4, %eax
    addl t12, %eax
    movl %eax, t13
    movl t13, z

; Exit the program
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
