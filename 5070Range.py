#Written by Lucas Chung, StudentID:103019274, 18_08_20
#Answer to Q3 "Selection Quiz"

number=int(input("Please enter a number: "))

while number<50 or number>70:
    number=int(input("Wrong number. Enter another number: "))
if number>=50 or number<=70:
    print("Number is within range.")

