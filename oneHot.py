import pandas as pd
import random
def CustomeGetDummies(list_item):
    column=list()
    result = []
    for i in range(len(list_item)):
        if not column.__contains__(list_item[i]):
            column.append(list_item[i])
    result.append(column)
    for i in range(len(list_item)):
        item = ['0']*len(column)
        item[column.index(list_item[i])]=1
        result.append(item)
    return result
        
        
    


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
tt= pd.get_dummies(data['whoAmI'])

print (tt)
print(CustomeGetDummies(lst))

