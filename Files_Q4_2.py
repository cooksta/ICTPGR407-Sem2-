#Quiz "Reading and writing files", Q4, ICTPGR407
#Lucas Chung, ID:103019274, 12/10/20


#import math function for factorials
import math

#create new text file to write outputs
txt=open("factorials.txt", "w")

#define value/list
numbers = 1


#loop for n+1 of value to be factorised(?)
 
while (numbers < 10): 
    numbers=numbers+1
    fact=math.factorial(numbers)
    txt.write(str(fact))
    txt.write("\n")
txt.close()

