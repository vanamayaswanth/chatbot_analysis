str1 = "Haveing beautful place place something the the this it the it it it"

lst = str1.split()

dic = {}

for i in lst:
    if i in dic:
        dic[i] += 1
        
    else:
        dic[i] = 1
        
Keymax = max(zip(dic.values(), dic.keys()))[1]

print(len(Keymax))