"""
The script finds a root of a quadratic equation,
It uses false position method for the same.
In this method we draw a chord from function value of a to function value of b.
Then find the intersection of that chord and assign a new valid interval for a and b.
Iteratively following the procedure, we converge to the root.

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
    if p > 0:
        print "Invalid interval, roots do not exist between %f and %f" % (a,b)
    else:
        i = 1;
        m = (a * fb - b * fa) / (fb - fa);                         #finding the intersection of the chord at x-axis.
        fm = f(m,equ);
        print "\ni\ta\t\tb\t\tm\t\tfm\t\tfa*fm"
        while (abs(fm) >= e):                                      #while we reach to minimum error.
            print "\n%d\t%f\t%f\t%f\t%f\t%f" %(i,a,b,m,fm,fa*fm)
            p = fa * fm;
            if p > 0:
                a = m;                                             #reducing the interval. 
                fa = f(a,equ);
            else:
                b = m;
                fb = f(b,equ);
            m = (a * fb - b * fa) / (fb - fa);
            fm = f(m,equ);
            i += 1;
        print "root: %f" % m;

if __name__ == "__main__":
    main()
