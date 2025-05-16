#姓名：王薪洋，学号：24210227016，日期，25.4.8
print(f"--------------------------\n{"注册界面".center(30)}")
name=input("请输入您的注册姓名：")
key=input("请输入您的注册密码:")
print('恭喜你！注册成功！')
print(f"--------------------------\n{"登录界面".center(30)}")
name_n=input("请输入您的登录姓名：")
key_n=input("请输入您的登录密码:")
if name==name_n and key==key_n:
    print('登录成功')
else:
    print('登录失败')
