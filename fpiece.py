def fpiece(x):
    import math
    import statistics
    a=x
    n=len(x)
    b= statistics.mean(x)
    for i in range(0,n):
        if x[i]<0:
            a[i]=(2*math.sin(math.radians(x[i])))
        elif x[i]>0 and x[i]<=1:
            a[i]=5*math.sqrt(x[i])
        elif x[i]>1 and x[i]<7:
            a[i]=1/(math.factorial(math.floor(x[i])))
        elif x[i]>=7:
            a[i]=20*math.log10(x[i])
    print(a)
    c= max(x)
    #b= statistics.mean(x)
    print(b)
    print(c)
    
