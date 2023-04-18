def quadratic_equation_value(a, x, b, c):
	result = a * x*x + b * x + c
	return result

a, x, b, c = input().split()
a, x, b, c = int(a), int(x), int(b), int(c)

print(quadratic_equation_value(a, x, b, c))