numbs=[1,2,3,4,5,6,7,8,9,10]
square=numbs.copy()
for i in numbs:
    print(numbs[i])
    square[i] = numbs[i]**2
    print(square[i])
print("s",square)
