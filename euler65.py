# https://projecteuler.net/problem=65

def digitSum(a):
    result = 0
    while (a > 0):
        result += a % 10
        a /= 10
    return result

def calc( iterations ):
    print 'Calc with ', iterations, ' iterations:'
    a = 1
    b = 1
    for i in range(iterations-1, 1, -1):
        if i % 3 == 0:
            a += b * i / 3 * 2
        else:
            a += b
        a, b = b, a
    a += b*2

    print 'a =', a
    print 'b =', b
    print 'e =', float(a)/b
    print 'digitsum =', digitSum(a)
    print ''
    return digitSum(a)

if ( calc(10) != 17):
    raise Exception("Calculation failed on the example.")
calc(100)
