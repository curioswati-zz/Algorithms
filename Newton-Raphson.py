"""
The script finds a root of a quadratic equation,
It uses newton raphson method for the same.

It defines:
    -main
    -fn
    -dfn
Returns:
    -a float, i.e. the root. 
"""

def fn(x,equ):
    """
    The function takes a float or integer x as argument,
    and returns the value of the equation 'equ' at x.
    """
    return eval(equ);

def dfn(x,d_equ):
    """
    The function takes a float or integer x as argument,
    and returns the value of the equation 'equ' at x.
    """
    return eval(d_equ);

    
def main():
    equ = raw_input("Enter the equation: ")
    d_equ = raw_input("enter the differentiation equation of equ: ") 
    a = float(input("Enter lower range: "))
    b = float(input("Enter upper range: "))
    e = float(input("Enter error: "))
    n = input("Enter maximum allowed iterations: ")

    fa = fn(a,equ)                                       #value of function at a.  
    fb = fn(b,equ)                                       #value of function at b.

    if fa*fb > 0:                                        #both pts lie on either sides 
        print "Invalid interval;no roots between this"
        return    
    elif fa > fb:                                        #so as to choose the smaller function value point.
        x0 = b
    else:
        x0 = a

    print "i\tx0\t\tx1\t\tfx0\t\td_fx0\t\tx1-x0"
    for i in range(n):                                   #Iterate for maximum allowed times.

        fx0 = fn(x0,equ)         
        d_fx0 = dfn(x0,d_equ)

        x1 = x0 - ( fx0 / d_fx0 )                        #The intersection pt of tangeant
    
        if abs(x1 - x0) <= e:
            print "root: %f" % x1
            break

        print "%d\t%f\t%f\t%f\t%f\t%f" % (i,x0,x1,fx0,d_fx0,x1-x0)  
        x0 = x1                                          #set new x0 to the intersection
        
if __name__ == "__main__":
    main()
