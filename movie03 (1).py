def movie03py():
  a=int(input("Enter the number of persons 4 years old and younger?"))
  b=int(input("Enter the number of persons 5 to 11 year old?"))
  c=int(input("Enter the number of persons 12 year old and older?"))
  A=0.00
  B=7.50
  C=10.00
  total= a*A+b*B+c*C
  print("Persons  Ages                Cost/ticket Total Cost")
  print(a,f"       4 years and younger      Free     $""{:.2f}".format(a*A))
  print(b,f"       5 to 11 years old        7.50    $""{:.2f}".format(b*B))
  print(c,f"       12 years old and older  10.00    $""{:.2f}".format(c*C))
  print("                                    Total $""{:.2f}".format(total))
  return total

if __name__ == '__main__':
    u=movie03py()
