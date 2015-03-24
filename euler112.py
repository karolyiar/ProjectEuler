# https://projecteuler.net/problem=112

''' Returns True if the number is bouncy '''
def bouncy(n):
    bounce = False
    num = str(n)
    ''' Under 100 cant be bouncy '''
    if n < 100:
        return False
    j = 1
    ''' The equivalent digits arent important '''
    while n/10%10 == n%10 and n>10:
        n /= 10
    ''' Checks if the left side increasing '''
    inc = n/10%10 > n%10
    
    if inc:
        ''' Deletes the digits until a decrease '''
        while n > 9:
            if n/10%10 < n%10:
                return True
            n /= 10
    else:
        ''' Deletes the digits until an increase '''
        while n > 9:
            if n/10%10 > n%10:
                return True
            n /= 10
    return False


numerator = 0
denominator = 0
while True:
    denominator += 1
    if bouncy(denominator):
        numerator += 1
    if 100*numerator/denominator == 99:
        break
    
print numerator, '/', denominator, '=', 100*numerator/denominator, '%'
print 'Solution:', denominator

