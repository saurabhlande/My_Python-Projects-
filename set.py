s1= {10,20,30,40,50,"ab",1.2,(1,2)}
print(s1)

print("==============create empty SET=================")
s2=set()
print(type(s2))

print("==============create Set by use set Fun=================")
s3= set([1,2,3])
print(s3)
print(type(s3))

print("==============Set Methods=================")
s4={1,2,3}
print(s4)

print("============== SET ADD =================")
s4.add(10)
s4.add(15)
print(s4)

print("============== Update SET (multi ele. Add) =================")
s4.update([80,90])
s4.update([20,25],[30,35])
print(s4)

print("============== remove/discard SET=================")
s4.remove(2)
s4.discard(25)
s4.discard(225)
print(s4)

print("==============Pop SET=================")
s4.pop()
print(s4)
# If you use pop then delete randam item

print("==============Clear SET=================")
s4.clear()
print(s4)