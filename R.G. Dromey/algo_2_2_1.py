"""
A script that prints no of occurences of integer above a particular range.
Also prints their frequency and the rate of favours among total.
"""
def main(lower_limit):
	passes=0
	number_of_entries=0

	while True:
	    entry = raw_input("Enter number: ")
	    if not entry:
	    	break

	    elif int(entry)>=lower_limit:
	        passes+=1

	    number_of_entries+=1

	pass_rate = float(passes) / number_of_entries * 100
	return number_of_entries, passes, pass_rate

if __name__ == "__main__":
	lower_limit = input("Please enter the lower limit above which the integer passes: ")
	ne, passes, pass_rate = main(lower_limit)
	print "Total entries: ", ne
	print "Total passing entries: ", passes
	print "Passing rate: ", pass_rate
