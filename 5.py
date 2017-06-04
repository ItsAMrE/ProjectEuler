lcm = 1
for a in range(2, 20):
    if lcm != a:
        if a > lcm:
            dividend = a
            divisor = lcm
        else:
            dividend = lcm
            divisor = a
        remainder = 1
        while remainder != 0:
            quotient = dividend / divisor
            remainder = dividend % divisor
            if remainder != 0:
                dividend = divisor
                divisor = remainder
        lcd = divisor
        lcm = (lcm * a) / lcd
print lcm
