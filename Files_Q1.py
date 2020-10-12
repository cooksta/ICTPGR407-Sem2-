#Quiz "Reading and writing files", Q1, ICTPGR407
#Lucas Chung, ID:103019274, 5/10/20

File1=open("Files_Q1.txt", "w")

print(File1)
x=int(input("Enter a number: "))
y=int(input("Enter another number: "))
z=x+y

File1.write(str(z))
File1.close()


