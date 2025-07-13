#dic_methos
emp = {122: 45, 123: 89 ,670: 435
}
emp2 = {222: 45, 443: 431}
emp.update(emp2)
print(emp)
#ep1.clear()##it clear all the elements and print empty dic(you will get empty set)
emp.pop(122)#delets the first
print(emp)
emp.popitem()#delets the last element
print(emp)
#del emp ##delets the entire set (if you try to print you get error)
del emp[123]
print(emp)