print("simple Code NOT using Lambda Fun:")
def even (x):
    temp=[]
    for s in x:
        temp.append(s*s)
    return temp
x=[11,12,13,14,15,16,17,18,19,20]
y= even(x)
print(y)

print("==============================")

print("USING LAMBDA Fun")
x=[11,12,13,14,15,16,17,18,19,20]
a= list(map(lambda s:s*s,x))
print(a)