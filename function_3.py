def add():
    a = input("enter 1st No.:")
    a = int(a)
    b = input("enter 2nd No.:")
    b = int(b)
    c = a + b
    print("Add A and B is", c)


# ============================================


def check():
    x= input("Enter no.:")
    x= int(x)
    if x%2==0:
        print("it is even No.")
    else:
        print("it is odd No.")


# ============================================



def area():
    r= input("enter the redius of circle")
    r=int(r)
    x=3.14*r*r
    print(x)


# ============================================
# Call Fun:
add()
print("===0===0===0===0===0===0===0===0===")
check()
print("===0===0===0===0===0===0===0===0===")
area()