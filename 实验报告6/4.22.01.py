#姓名：王薪洋，学号：24210227016，日期，25.4.22
def jjcc(a,b,c):
    d = 0
    if c == "+":
        d = a+b
        return(d)
    elif c == "-":
        d = a-b
        return(d)
    elif c == "*":
        d = a*b
        return(d)
    else:
        d = a/b
        return (d)
print("请依次输入数字，运算符，数字")
a=float(input())
w=input()
b=float(input())
c=jjcc(a,b,w)
print(c)