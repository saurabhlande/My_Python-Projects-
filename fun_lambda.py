
#Not using Lambda in this program:
def even (x):
    temp =[]
    for z in x:
        if z%2 ==0:
            temp.append(z)
    return temp
x=[11,12,13,14,15,16,17,18,19,20]
y =even(x)
print(y)


#using Lambdfa Fun:
a=[11,12,13,14,15,16,17,18,19,20]
b=list(filter(lambda x:x%2==0,a))
print(b)
