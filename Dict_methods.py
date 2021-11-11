

# create a dict
d1={1:'A',2:100,'c':300}

print(d1[2])
print(d1['c'])


print("=========== Dict Methods==========")
d2={1:'a', 2:'b', 3:'c', 4:'d'}

print("=========== Dict Methods 1.Keys:-==========")
karr=d2.keys()
print(type(d2))
for k in karr:
    print(k)


print("=========== Dict Methods 2.Values:-==========")
varr=d2.keys()
print(type(d2))
for v in varr:
    print(v)


print("=========== Dict Methods 3.Get:-==========")
print(d2.get('c'))
print(d2.get(2))


print("=========== Dict Methods 4.Items:-==========")
kvarr=d2.items()
for k,v in kvarr:
    print(k,v)


print("=========== Dict Methods 5.POP:-==========")
print(d2)
d2.pop(3)
print(d2)


print("=========== Dict Methods 6.Popitem:-==========")
d2.popitem()
print(d2)

print("=========== Dict Methods 7.Update:-==========")
print(d2)
d2[2]='xyz'
print(d2)

d3={4:'abc'}
d2.update((d3))
print(d2)

print("=========== Dict Methods 8.Copy:-==========")
print(d2)
d4=d2.copy()
print(d4)
print(id(d2))
print(id(d4))

print("=========== Dict Methods 9.Clear:-==========")
d2.clear()
print(d2)