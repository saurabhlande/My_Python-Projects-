sqr =lambda i: i*i
c= sqr (8)
print(c)

print("=======================================")

sqr =(lambda i: i*i)(5)
print(sqr)

print("========================================")

sqr =(lambda x,y=110: x+y)(5)
print(sqr)

print("=======================================")

x = lambda i,j: i+j
a= x (100,200)
print("addition is", a)

print("========================================")

check = lambda x: 'even' if x%2==0 else'odd'
print(check(12))