names1=['Ross','Ann','Zoe','Hal']
names2=('Ross','Ann','Zoe','Hal')
names3={'Ross','Ann','Zoe','Hal'}
names1.append('Rome')#Can Add only one item to the end of the list
names3.add('Rome')#Can Add only one item to the set
names3.add('Roe')
print(names1)
print(names3)
if'Rome'in names1:
    names1.append('OT')
print('Is Rome in tcity?','Rome'in names2)
print('Is Rome in scity?','Rome'in names3)
print(names1)
