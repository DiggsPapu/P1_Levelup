#Proyecto1 Level Up Diego Andres Alonzo Medinilla  
dic = {'ho':"hola", 'b':2, 'c':3, 1:[1,2,3,4,5]}
key_list = []
value_list = []
for x in dic.items():
    key_list.append(str(x[0]))    
    value_list.append(str(x[1]))

key_list.sort()
value_list.sort()
print(key_list)
print(value_list)
