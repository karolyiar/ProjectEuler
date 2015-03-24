# https://projecteuler.net/problem=52

''' Counts the number of 0-s at result[0].. '''
def digits(num):
    result = [0] * 10
    while num > 0:
        result[ num%10 ] += 1
        num /= 10
    return result


found = False
i = 1
while not found:
    i += 1
    digitsI = digits(i)
    if digitsI == digits(6*i):
        if digitsI == digits(5*i):
            if digitsI == digits(4*i):
                if digitsI == digits(3*i):
                    if digitsI == digits(2*i):
                        print i
                        found = True
