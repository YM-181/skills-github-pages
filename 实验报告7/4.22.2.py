

with open('city.txt','w+',encoding='utf-8')as f:
    line=f.readlines()
for i in line:
    list=i.replace('\n','')
    print(list)