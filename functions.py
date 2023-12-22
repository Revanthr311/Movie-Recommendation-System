import ast
from nltk.stem.porter import PorterStemmer



def genres_keywords(obj):
    List=[]
    for i in ast.literal_eval(obj):
        List.append(i['name'])
    return List 
    
def cast(obj):
    cast=[]
    counter=0
    for i in ast.literal_eval(obj):
        if counter!=5:
            cast.append(i['name'])
            counter+=1
        else:
            break
    return cast
    

def director_name(obj):
    name=[]
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            name.append(i['name'])
    return name 

def collapse(obj):
    L=[]
    for i in obj:
        L.append(i.replace(" ",""))
    return L


ps=PorterStemmer()

def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)