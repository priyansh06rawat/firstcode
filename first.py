def bisection_method(func, a, b, tol=1e-6, max=100):
    if func(a) * func(b) >= 0:
        raise ValueError("Function must have opposite signs at interval endpoints.")

    c = 0
    while (b - a) / 2 > tol and c < max:
        midpoint = (a + b) / 2
        if func(midpoint) == 0:
            return midpoint
        elif func(midpoint) * func(a) < 0:
            b = midpoint
        else:
            a = midpoint
        c += 1

    return (a + b) / 2
def f(x):
    return x**3 - 3*x + 1

root = bisection_method(f, -2, 2)
print("root:", root)
print("Value of f at the root:", f(root))