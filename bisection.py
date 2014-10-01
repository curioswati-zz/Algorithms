"""
The script finds a root of a quadratic equation,
It uses bisection method for the same.
It defines:
    -main
    -f
Returns:
    -a float, i.e. the root. 
"""

def f(x,equ):
    """
    The function takes a float or integer x as argument,
    and returns the value of the equation 'equ' at x.
    """
    return eval(equ);

def main():
    equ = raw_input("Enter the equation: ")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))          
    e = float(input("Enter the precision: "))                      #allowed error.
             
    fa = f(a,equ)                                                  #value of function at a
    fb = f(b,equ)                                                  #value of function at b
    p = fa * fb                                             
    if p > 0:                                                      #root will always lie between a negative and a positive value.
        print "Invalid interval, roots do not exist between %f and %f" % (a,b)
    else:
        i = 1;
        m = (a + b) / 2;                                           #finding the mid value of interval.
        fm = f(m,equ);
        print "\ni\ta\t\tb\t\tm\t\tfm\t\tfa*fm"
        while (abs(fm) >= e):
            print "\n%d\t%f\t%f\t%f\t%f\t%f" %(i,a,b,m,fm,fa*fm)
            p = fa * fm;
            if p > 0:
                a = m;                                             #taking the half of the original interval as new interval. 
                fa = f(a,equ);
            else:
                b = m;
                fb = f(b,equ);
            m = (a + b) / 2;     
            fm = f(m,equ);
            i += 1;
        print "root: %f" % m;

if __name__ == "__main__":
    main()
