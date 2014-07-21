def dec(no):
    res=0
    i=len(no)-1
    for digit in no:
        res += int(digit) * 2**i
        i-=1
    return res    

def comp(bin_no):
    no = list(bin_no)
    for i in range(0,len(bin_no)):
        if no[i] == 1:
            no[i]='0'
            print no[i] ,
        else:
            no[i]='1'        
    return ''.join(no)         
print comp('101')

bin_no = raw_input("Enter a binary no: ")
if bin_no[0] == '0':
    sign = '+'
    magnitude = dec(bin_no)

else:
    sign = '-'
    magnitude = dec(comp(bin_no))
print sign+magnitude    
