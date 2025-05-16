#姓名：王薪洋，学号：24210227016，日期，25.4.22
flag=True
while flag:
    x=input('请输入学号')
    if len(x)!=11:
        print("输入错误，请重新输入")
    else:
        flag=False
X=x[4:8]
if X=='0812':
    print(f'学号为{x}的学生是人工智能的学生')
else:
    print ("不认识")