#姓名：王薪洋，学号：24210227016，日期，25.6.4
def display_friends(friends):
    if friends:
        for index, friend in enumerate(friends, 1):
            print(f"{index}. {friend}")
    else:
        print("好友列表为空")

def add_friend(friends):
    name = input("请输入要添加的好友的姓名：")
    friends.append(name)
    print("好友添加成功")

def delete_friend(friends):
    name = input("请输入要删除好友的姓名：")
    if name in friends:
        friends.remove(name)
        print("删除成功")
    else:
        print("好友不存在")

def remark_friend(friends):
    name = input("请输入要修改的好友姓名：")
    if name in friends:
        new_name = input("请输入修改后的好友姓名：")
        friends[friends.index(name)] = new_name
        print("备注成功")
    else:
        print("好友不存在")

def main():
    friends = []
    while True:
        print("\n欢迎使用好友管理系统")
        print("1: 添加好友")
        print("2: 删除好友")
        print("3: 备注好友")
        print("4: 展示好友")
        print("5: 退出")

        choice = input("请输入您的选项：")
        if choice == '1':
            add_friend(friends)
        elif choice == '2':
            delete_friend(friends)
        elif choice == '3':
            remark_friend(friends)
        elif choice == '4':
            display_friends(friends)
        elif choice == '5':
            print("退出系统")
            break
        else:
            print("无效的选项，请重新输入")
if __name__ == "__main__":
    main()