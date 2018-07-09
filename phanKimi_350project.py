# Programmer: Kimi Phan
# ID: 1146643
# Class: CptS 350, Fall 2017
# Description: Graph/Pyeda Project

from pyeda.inter import *

# Node: A, B, C, D, E, F, G, H
# Edges: A->B, B->C, C->D, D->H, H->G, G->F, F->E, E->A, A->G, D->E, G->C

# Nodes:
# A = 000
# B = 001
# C = 010
# D = 011
# E = 100
# F = 101
# G = 110
# H = 111

# setting the variables
x1 = exprvar('x1')
x2 = exprvar('x2')
x3 = exprvar('x3')
y1 = exprvar('y1')
y2 = exprvar('y2')
y3 = exprvar('y3')
z1 = exprvar('z1')
z2 = exprvar('z2')
z3 = exprvar('z3')

# setting the edges to a boolean function
# A->B = 000->001
AB = ~x1 & ~x2 & ~x3 & ~y1 & ~y2 &  y3
# B->C = 001->010
BC = ~x1 & ~x2 &  x3 & ~y1 &  y2 & ~y3
# C->D = 010->011
CD = ~x1 &  x2 & ~x3 & ~y1 &  y2 &  y3
# D->H = 011->111
DH = ~x1 &  x2 &  x3 &  y1 &  y2 &  y3
# H->G = 111->110
HG =  x1 &  x2 &  x3 &  y1 &  y2 & ~y3
# G->F = 110->101
GF =  x1 &  x2 & ~x3 &  y1 & ~y2 &  y3
# F->E = 101->100
FE =  x1 & ~x2 &  x3 &  y1 & ~y2 & ~y3
# E->A = 100->000
EA =  x1 & ~x2 & ~x3 & ~y1 & ~y2 & ~y3
# A->G = 000->110
AG = ~x1 & ~x2 & ~x3 &  y1 &  y2 & ~y3
# D->E = 011->100
DE = ~x1 &  x2 &  x3 &  y1 & ~y2 & ~y3
# G->C = 110->010
GC =  x1 &  x2 & ~x3 & ~y1 &  y2 & ~y3

# setting boolean formula R for the graph
R = AB | BC | CD | DH | HG | GF | FE | EA | AG | DE | GC

# converting the boolean formula to a BDD and composing them
def compose(A, B):
    A = A.compose({y1: z1, y2: z2, y3: z3})
    B = B.compose({x1: z1, x2: z2, x3: z3})

    R2 = A & B
    R2 = R2.smoothing(z1).smoothing(z2).smoothing(z3)
    return R2

# seeing which nodes can reach other nodes in the graph
R2 = compose(R, R) | R
R3 = compose(R2, R) | R2
R4 = compose(R3, R) | R3
R5 = compose(R4, R) | R4

R5 = R5.simplify()
R5 = list(R5.satisfy_all())

# Checking if A can reach E within 5 steps
found = False
for val in R5:
    if val[x1] == 0 and val[x2] == 0 and val[x3] ==  0 and \
            val[y1] == 1 and val[y2] == 0 and (y3 not in val or val[y3] == 1):
        found = True
print (found)
