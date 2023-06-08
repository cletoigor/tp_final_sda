from math import sqrt

C = 0
h = 0
R0 = 0
R1 = 0
H = 0
u = 0

pi = 3.14
alfa = R1 - R0/H
qout = C * sqrt(h)
hponto = [qout/pi * (R0 + alfa * h)^2] + [1/pi * (R0 + alfa * h)^2] * u