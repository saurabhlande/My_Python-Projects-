#creting dictionary
d1={1:'A',2:100,2:300}
print(type(d1))
print(d1)

#key can immutable datatypes
#(int, tuple, str)
d2={1:'a', (101,20):'B','c':100}
print(d2)

#key can not be mutable
d3={[10,20]:150}
print(d3)