from z3 import *
from itertools import combinations

def isValid(phi):
    s = Solver()
    s.add (Not(phi))
    if s.check() == sat:
        return False
    else:
        return True

def isSAT(phi):
    s = Solver()
    s.add (phi)
    return s.check() == sat


############################
# predicate abstraction

def abstract(phi, preds):
    res = And(True)

    for p in preds:
        if isValid(Implies(phi,p)):
            res = And(res,p)
        if isValid(Implies(phi, Not(p))):
            res = And(res, Not(p))

    return simplify(res)

def booleanAbstract(phi, preds):
    res = And(False)
    negpreds = map (lambda x: Not(x), preds)

    for ps in combinations(preds+negpreds, len(preds)):
        if isSAT(And(phi, *ps)):
            res = Or(res, And(*ps))

    return simplify(res)

def fixpoint(oldInv,inv):
    return isValid (Implies(inv,oldInv))

###########################
# example

x = Int('x')
y = Int('y')
z = Int('z')
lock = Int('lock')
old = Int('old')
new = Int('new')

xp = Int('x\'')
yp = Int('y\'')
zp = Int('z\'')
lockp = Int('lockp')
oldp = Int('oldp')
newp = Int('newp')

varMap = [(x,xp), (y,yp), (z,zp), (lock,lockp), (old,oldp), (new,newp)]
varMapRev = map(lambda v: (v[1], v[0]), varMap)


###ex1
init = And(x == 0, y == 0)
trans = And(xp == x + 1, yp == y + 1)
post = Implies (y == 10, x == 10)

preds = [x > 0]
# preds = [x >= 0]
# preds = [x >= y, x <= y]
# preds = [x == 0, y == 0, y == 1, x == 1, x == 2, y == 2]

###ex2
init = And(x == 10, y == 10)
trans = And(x + y > 0, xp == x - 1, yp == y - 1, zp == xp + yp)
post = Implies (x + y <= 0, z == 0)

preds = [x >= 0, x == y]
#preds = [x > 0, x >= 0, x == y, z == x + y]

###ex3
init = And(x == y)
trans = And(xp == x + 1, yp == y + 1)
post = Or(And(x % 2 == 0, y % 2 == 0), And(x % 2 != 0, y % 2 != 0))

preds = [x % 2 == 0, y % 2 == 0]

###ex4
init = And(lock == 0, new != old)

trans = And(new != old, oldp == new,
            Or(And(lockp == 0, newp == new + 1),
                And(lockp == 1, newp == new)))

post = Implies(new == old, lock != 0)

preds = [lock == 0, new == old]


#####################################

predsprime = map(lambda p: substitute(p,*varMap), preds)

oldInv = False
inv = booleanAbstract(init, preds)

i = 0
while not fixpoint(oldInv,inv):
    print "\nInv at ", i, ": ", inv
    i = i + 1

    # existential quantifer??
    onestep = booleanAbstract(And(inv, trans), predsprime)
    onestep = substitute(onestep, varMapRev)
    oldInv = inv
    inv = simplify(Or(inv, onestep))

print "\n"

if isValid(Implies(inv,post)):
    print ">>> SAFE\n\n"
else:
    print ">>> MAYBE?!?!\n\n"
