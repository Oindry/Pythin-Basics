import statistics
a=[1.00,2.00,3.00,4.00,5.00,6.00];
y=a;
x=len(a)
for item in range(0,x):
    y[item]=a[item]/x
    s=y
    s[item]="%.2f"%y[item]
    z=y
    z[item]="%.2f"%a[item]
    
print(s)
print(y)
print(z)
    

    
