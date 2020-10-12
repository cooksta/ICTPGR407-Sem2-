#Quiz "Reading and writing files", Q2, ICTPGR407
#Lucas Chung, ID:103019274, 5/10/20


name=None
people=open("people.txt", "w")

while name != "":
    name=input("Please enter a name: ")
    people.write(name+"\n")
people.close





