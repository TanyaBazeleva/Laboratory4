
n = int(input())
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def proste(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(factorial(n))
print(proste(n))

