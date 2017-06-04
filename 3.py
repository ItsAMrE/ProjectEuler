number = 600851475143
number2 = number
factors = []
i = 2
while i <= number2:
    if number2%i==0:
        factors.append(i)
        number2 = number2 / i 
    else:
        i = i+1

largest = 0
for n in factors:
    print n
    if n > largest:
        largest = n

print "____"
print largest
