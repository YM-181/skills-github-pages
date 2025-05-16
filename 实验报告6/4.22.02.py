#姓名：王薪洋，学号：24210227016，日期，25.4.22
def fibonacci (n):
    if n==1 or n==2:
        return 1
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
num=0
flag=True
while flag:
    num=int(input("请输入一个大于0的整数"))
    if num<=0:
        print ('输入错误，请重新输入')
    else:
        flag=False
J=fibonacci(num)
print(f"第{num}个斐波那契数为{J}")