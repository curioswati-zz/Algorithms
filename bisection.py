def f(x):
    return (x*x - x - 1);

def main():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))          
    e = float(input("Enter the precision: "))
             
    fa = f(a)
    fb = f(b)
    p = fa * fb
    if p > 0:
        print "Invalid interval, roots do not exist between %f and %f" % (a,b)
    else:
        i = 1;
        m = (a + b) / 2;
        fm = f(m);
        while (abs(fm) >= e):
            print "\n%d\t%f\t%f\t%f\t%f\t%f" %(i,a,b,m,fm,fa*fm)
            p = fa * fm;
            if p > 0:
                a = m;
                fa = f(a);
            else:
                b = m;
                fb = f(b);
            m = (a + b) / 2;
            fm = f(m);
            i += 1;
        print "root: %f" % m;

print "Call main()"        
