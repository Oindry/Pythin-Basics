def Cypher(Str,cd):
    x1={'a': 'v', 'b': 't', 'c': 'm', 'd': 'j', 'e': 'w', 'f': 'i'}
    x2={'g': 'b', 'h': 'n', 'i': 'f', 'j': 'z', 'k': 'h', 'l': 'r'}
    x3={'m': 'o', 'n': 'g', 'o': 'p', 'p': 'd', 'q': 'k', 'r': 'l'}
    x4={'s': ' ', 't': 'a', 'u': 'q', 'v': 'x', 'w': 'e', 'x': 'c'}
    x={}
    x5={'y': 'u', 'z': 'y', ' ': 's'}
    for d in (x1,x2,x3,x4,x5):
        x.update(d) #Merge dictionaries for Coding a string
    y1={'v': 'a', 't': 'b', 'm': 'c', 'j': 'd', 'w': 'e', 'i': 'f'}
    y2={'b': 'g', 'n': 'h', 'f': 'i', 'z': 'j', 'h': 'k', 'r': 'l'}
    y3={'o': 'm', 'g': 'n', 'p': 'o', 'd': 'p', 'k': 'q', 'l': 'r'}
    y4={' ': 's', 'a': 't', 'q': 'u', 'x': 'v', 'e': 'w', 'c': 'x'}
    y5={'u': 'y', 'y': 'z', 's': ' '}
    y={}
    for d in (y1,y2,y3,y4,y5):
        y.update(d)
    Phase=Str.lower()
    Out=''
    if cd==0:
        if Phase in x:
            Out+=x[Phase]
    elif cd==1:
        if Phase in y:
            Out+=y[Phase]
    return(Out)

    
