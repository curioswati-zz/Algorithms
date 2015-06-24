"""
Interpolation by Newton and gragory's backward interpolation formula.
                  u           u*(u-1)            u*(u-1)*(u-2) 
f(a+uh) = f(a) + ---*d_f(a) + -------*d^2_f(a) + -------------*d^3_f(a)+....
                  1!             2!                   3!
where a   > last input argument
      f(a)> function value of a
      u   > constant multiplier of h
      h   > interval difference
      d_  > nebla operator defined as:
              /\f(a) = f(a) - f(a-h)
"""
import diff_table

#Creating difference table
#---------------------------------------------------------
n = input("Enter no of terms: ")
x = map(int,raw_input("Enter values for x: ").split())
fx = map(int,raw_input("Enter values for f(x): ").split())
#---------------------------------------------------------

#printing difference table
#---------------------------------------------------------
D = diff_table.main(n,x,fx)
print("The difference table ")
for i in D:
    for j in i:
        print j,
    print "\n"
#---------------------------------------------------------

#Defining constants for use in formula
#---------------------------------------------------------
X = input("Enter x for which you want f(x): ")
a = x[-1]
h = float(x[1] - x[0])
u = (X-a) / h
#---------------------------------------------------------

#Calculating the value using formula
s = D[0][0]
fact = 1.0
i = 1
for fa in D[0][1:]:
    index = D[0].index(fa)
    for i in xrange(1,index):
        u *= u - i

    s = s + (u *fa / fact)
    fact = fact * (i + 1)
    i += 1
    
#The answer
print 'f(%d): %f' % (X,s)
