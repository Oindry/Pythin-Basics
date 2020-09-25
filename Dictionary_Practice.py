Items={'Food':'Chicken','Game':'Workout'}
Items['Man']='Not Mark'
print(Items.keys())
#We can merge (i.e. concatenate) one dictionary with another dictionary
fw1={"pink":"rose","orange":"orange","red":"rouge","yellow":"jaune"}
fw2={"green":"vert","blue":"bleu","purple":"violet","black":"noir"}
fw3=fw1.update(fw2)
#fw3=fw1.copy()
#fw3.update(fw2
french_words={"fw1": fw1, "fw2": fw2}
print(french_words["fw1"]["yellow"])
print("fw1",fw1.keys())
print("fw3",fw3.keys())
