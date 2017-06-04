palindromes = []
for a in range(999,100,-1):
    for b in range(999,100,-1):
        x = a*b
        
        x_string = str(x)
        if x_string == x_string[::-1]:
            palindromes.append(x)

largest = 0
for i in palindromes:
    if i > largest:
        largest = i

print largest
