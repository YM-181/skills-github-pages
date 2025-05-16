#姓名：王薪洋，学号：24210227016，日期，25.4.22
def jc(n):
    if n==1 or n==0:
        return 1
    else:
        return jc(n-1)*n
num=int(input('请输入要求阶乘的整数'))
jg=jc(num)
print(f"结果为{jg}")