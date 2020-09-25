case1=int(input("Enter the number of persons 4 years old and younger?"))
case2=int(input("Enter the number of persons 5 to 11 years old?"))
case3=int(input("Enter the number of persons 12 year old and older?"))

cost2=float(7.50*case2)
cost3=int(10.00*case3)
total=cost2+cost3
print("Persons","\tAges","\t\t   Cost/ticket Total Cost")
print(case1,"\t\t4 years and younger","\tFree","\t","$"+"0.00")
print(case2,"\t\t5 to 11 year old","\t7.50","\t $""%.2f"%cost2)
print(case3,"\t\t12 years old and older 10.00","\t $""%.2f"%cost3)
print("\t\t\t\t\t   Total $""%.2f"%total)

