"""
A script that prints total no of positive and negative numbers,
found in a series of input
"""
def main():
	c_pos = 0                                  #positive counter
	c_neg = 0                                  #negative counter

	while True:
	    n = raw_input("Enter number: ")		   #input no.  
	    if not n:
	    	break

	    if int(n)>=0:                          #if n positive  
	        c_pos+=1                           #increase positive counter
	    else:
	        c_neg+=1                           #increase negative counter

	return c_pos, c_neg

if __name__ == "__main__":
	pos, neg = main()
	print "Total positive: %d" % pos
	print "Total negative: %d" % neg
