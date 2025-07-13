dic = {"apple" : "fruit",
       "tomato" : "vegtable"}
print(dic["apple"])
dic1 = {
    400 : "robin",
    533 : "johin"
}
print(dic1[533])
print(dic["apple"])#if its not avaiable we get error
print(dic.get("tomato"))#but in this we get 'none'
print(dic.keys())#printing all keys
for key in dic.keys():
       print(f"The values corresponding to the keys {key} is {dic[key]}")#to print values
print(dic.items())