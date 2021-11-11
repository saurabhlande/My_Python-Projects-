def outer():
    x=100
    def inner ():
        nonlocal x
        x=200
        print("In inner",x)
    inner()
    print()
    print("outer",x)
outer()