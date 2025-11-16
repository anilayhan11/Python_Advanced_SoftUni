def say_hi(num):
    if num <= 0:
        return
    print("Hi!")
    say_hi(num - 1)


say_hi(10)


# Factorial
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))
