x = 2
primes = 1
while primes < 10001:
    z = 0
    x += 1
    for y in range(2, x):
        if x%y==0:
            z = 1
            break

    if z == 0:
        primes += 1
        

print x
