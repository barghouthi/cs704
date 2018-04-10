from z3 import *

r = Int('r')
p = Int('p')
p1 = Int('p1')
p2 = Int('p2')

c1 = Implies(And(p > 100, r == p - 10), r >= 91)
c2 = Implies(And(p <= 100, p1 == p + 11, p2 >= 91, r >= 91), r >= 91)
c3 = Implies(r >= 91, r >= 91)


s = And(Implies(p <= 101, r == 91), Implies(p <= 111, r <= 101))
s1 = And(Implies(p1 <= 101, p2 == 91), Implies(p1 <= 111, p2 <= 101))
s2 = And(Implies(p2 <= 101, r == 91), Implies(p2 <= 111, r <= 101))

c1 = Implies(And(p > 100, r == p - 10), s)
c2 = Implies(And(p <= 100, p1 == p + 11, s1, s2), s)
c3 = Implies(s, Implies(p<=101,r==91))

solve(Not(c1))
solve(Not(c2))
solve(Not(c3))
