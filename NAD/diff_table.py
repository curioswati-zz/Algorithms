#Difference table for Interpolation

def main(n, x, fx):

    diff_table = []

    for j in xrange(n-1):
        
        for i in xrange(n-1):
            if j == 0:
                diff_table.append( [fx[i]] )
                diff_table[i].append( fx[i+1] - fx[i] )
            else:
                try:
                    d1 = diff_table[i+1][j]
                    d2 = diff_table[i][j]
                    delta = d1 - d2
                    diff_table[i].append(delta)
                except IndexError as e:
                    pass
    diff_table.append([fx[-1]])
    return diff_table
    
if __name__ == '__main__':

    n = input("Enter the no of terms: ")
    x = (map(int,raw_input("Enter values for x: ").split()))
    fx = (map(int,raw_input("Enter values for f(x): ").split()))

    d_table = main(n, x, fx)
    print d_table

    for i in d_table:
        for j in i:
            print  j,
        print("\n")
