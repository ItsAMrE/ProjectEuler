fib1 = 1
fib2 = 2
total = 0
while fib1 <= 4000000 or fib2 <= 4000000:
    if fib1%2==0 and fib1 <=4000000:
        total += fib1
    if fib2%2==0 and fib2 <=4000000:
        total += fib2
    fib1 += fib2
    fib2 += fib1

print total
