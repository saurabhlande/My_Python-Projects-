# W.A.P. to convert a list of muliple integers into a single integer
# list=[11,33,50]
# output= 113350

list = [11, 33, 50]
print(list)
x = int("".join(map(str,list)))
print(x)


# list=['q','p']
# n=4
# nlist=['{}''{}'.format(x,y)for y in range(1,n+1)for x in list]
# print(nlist)