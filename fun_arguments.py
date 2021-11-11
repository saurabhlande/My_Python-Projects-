# Fix Argument's
def add(a, b):
    c = a - b
    print("Addition is", c)


add(10, 20)
add(-20, 30)


# =======================================
#Fix Argument's

def area(r):
    a = 3.14 * r * r
    print("area is", a)


area(10)


# =========================================
# Defoult Argument's
def add(a=10, b=30):
    c = a + b
    print("Addition is ", c)


add()
add(5)
add(100, 200)


# =========================================
# Named Argument's

def add(x, y):
    print("x is ", x)
    print("y is ", y)
    print("Addition od X and Y is ", x + y)
    add(100, 200)
    print("hello", "world", end='', sep='@')
    print("hello")


# =========================================
# Veriable Argument's

def show(*names):
    for x in names:
        print(x)

show('a')
show('a', 'b')
show('a','b','c')


# =========================================
# Returning Argument's