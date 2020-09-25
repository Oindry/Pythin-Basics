import statistics
a=[1,2,3,4,5,6];
y=a;
x=len(a)
for item in range(0,x):
    z="%.2f"%a[item]
    y[item]=a[item]/x
    for item in range(0,x):
        s="%.2f"%y[item]
print(y)
print(s)
