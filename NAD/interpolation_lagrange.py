"""
Interpolation by Newton and gragory's backward interpolation formula.
                         n   _        _
         n            prod  | (X-x[j]) |
f(x) = sum( f(x[i]) * j!=i  |--------- | )
       i=1             j=1  |(x[i]-x[j]|
                             -        -
where X > input argument; whose function value is to find
      x > input arguments, with known function values
      n > no of terms
"""
#Taking input
###---------------------------------------------------------
n = input("Enter no of terms: ")
x = map(int,raw_input("Enter values for x: ").split())
fx = map(int,raw_input("Enter values for f(x): ").split())
X = input("Enter x for which you want f(x): ")
###---------------------------------------------------------

#Calculating the value using formula
s = 0
for i in xrange(n):
    
    prodfunc = 1
    for j in xrange(n):
        if i!= j:
            numerator = X-x[j]
            denominator = float(x[i] - x[j])
            prodfunc = prodfunc * numerator / denominator
    s = s + fx[i] * prodfunc
    
#The answer
print 'f(%f): %f' % (X,s)
