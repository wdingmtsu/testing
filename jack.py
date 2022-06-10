def factorial(n):
    assert(isinstance(n, int) and n>=0)
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("enter an integer to take the factorial of!")
print(factorial(int(input())))
