"""
A script that prints no of occurences of integer above a particular range.
"""
def main(lower_limit):
	total_entries = int(raw_input("Enter the no of marks: "))
	passes=total_entries

	while total_entries:
	    entry = input("Enter marks: ")
	    if entry<50:
	        passes -= 1
	    total_entries-=1

	return passes

if __name__ == "__main__":
	lower_limit = input("Enter the lower limit above which the integer passes: ")
	passes = main(lower_limit)
	print "The total integers above %d are %s" % (lower_limit, passes)
