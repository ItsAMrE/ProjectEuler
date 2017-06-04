sumSquares = 0
squareSums = 0
for x in range(1, 101):
    sumSquares = sumSquares + pow(x, 2)
    squareSums = squareSums + x

#print squareSums
squareSums = pow(squareSums, 2)
#print squareSums
#print sumSquares

difference = squareSums - sumSquares
print difference
