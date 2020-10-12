#Quiz "Reading and writing files", Q3, ICTPGR407
#Lucas Chung, ID:103019274, 12/10/20

#Open "names", create "names-formatted"
names = open("names.txt", "r")
names2 = open("names-formatted.txt", "w")

#I know ethere's a better way, I just don't know how, so I put the whole thing into memory.
names3=names.read()

#Capitalise each word
x=names3.title()

#write to "names-formatted"
names2.write(x)

#is it really neccessary to close?
names.close()
names2.close()





