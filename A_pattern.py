g=3
for i in range (1,5):
    k=0
    while k<g:
        print(" ",end='')
        k=k+1
    for j in range(1,i+1):
            print("  *",end='')
    print("")
    g=g-1