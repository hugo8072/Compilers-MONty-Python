.section .data
x1: .float 1.0
y1: .float 1.5
z1: .int 5
g1: .float 4.0
x: .float 1.0
d1: .float 3.6
l1: .float -3.5
p1: .int 3
b1: .int -2
q1: .float 300.0
n1: .float -230000.0
v1: .float 0.02
w1: .float 300.0
a2: .int 0
s1: .int 0
f1: .int 0
h1: .float 0.0
j1: .float 0.0
k1: .float 0.0

.section .text
.globl main
main:

; Exit the program
    movl $1, %eax
    xorl %ebx, %ebx
    int $0x80
