l = [5,2,8,3,7,3]
print(l)
l.append(4)#add a num in last           
print(l)
l.reverse()#reverse a list  
print(l)
l.sort(reverse=True)#desending order
print(l)
print(l.index(3))#print a specif num in a list      
print(l.count(3))#how many times a num repeated
m = l.copy()#duplicating
print(m)
l.insert(0 , 32)#inserting a specific num at specific place
print(l)
n = [400,500,600]
l.extend(n)#insering a list at ecd of exsting set
print(l)
k = l + m#adding two lists in a new list
print(k)


