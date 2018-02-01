# mainly from http://matt.might.net/articles/implementation-of-recursive-fixed-point-y-combinator-in-javascript-for-memoization/
# and
# http://matt.might.net/articles/python-church-y-combinator/

U = lambda x: x(x)
fact = lambda h: lambda x: 1 if x == 0 else x * (h (h))(x-1)
factu = U (fact)

# doesn't work yet
Y = lambda F: F (Y (F))
# Y(lambda f: lambda n: 1 if n <= 0 else n*f(n-1))

# now this works, but it's recursive
Y = lambda F: F(lambda x:Y(F)(x))
# Y(lambda f: lambda n: 1 if n <= 0 else n*f(n-1))(5)

# look, no recursion!
Y = U(lambda h: lambda F: F(lambda x:U(h)(F)(x)))

Y = ((lambda h: lambda F: F(lambda x:h(h)(F)(x))) (lambda h: lambda F: F(lambda x:h(h)(F)(x))))

# fibonacci
fib = lambda f: lambda n: n if n==0 or n == 1 else f(n-1) + f(n-2)

# caching y combinator
def Ymem(F, cache=None):
    if cache is None:
        cache = {}

    def fun(arg):
        if arg in cache:
            return cache[arg]

        res = (F(lambda n: (Ymem(F,cache))(n)))(arg)
        cache[arg] = res
        return res
    return fun
