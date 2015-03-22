# https://projecteuler.net/problem=327
import math

def roundUp(i):
    if i < 0:
        return 0
    else:
        return int(math.ceil(i))

'''
minimum number of cards required from the dispensing machine
to travel through R rooms
carrying up to a maximum of C cards at any time
'''
def M(C, R):
    ''' number of keys needed in the box in that room, backward '''
    B = [-C+1, ]
    ''' total keys needed to get out from that room, backward '''
    K = [0, ]
    ''' total keys needed '''
    result = 0
    ''' iterate through doors '''
    for i in range(1, R+2):
        B.append( (B[i-1]) + K[i-1] )
        K.append( 2 * roundUp( float(B[i]) / (C-2) ) + 1 )
        result += K[i]
    return result

def calc(a, b, R):
    result = 0
    for C in range(a, b+1):
        result += M(C, R)
    return result

if ( M(3, 6) != 123 ):
    raise Exception("Calculation failed on the example.")
if ( M(4, 6) != 23 ):
    raise Exception("Calculation failed on the example.")
if ( calc(3, 10, 10) != 10382 ):
    raise Exception("Calculation failed on the example.")
print "Result:", calc(3, 40, 30)

