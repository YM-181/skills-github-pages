#姓名：王薪洋，学号：24210227016，日期，25.6.6
class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("请输入联系人的姓名: ")
        if name in self.contacts:
            print("该联系人已存在")
            return
        phone = input("请输入联系人的手机号: ")
        email = input("请输入联系人的邮箱: ")
        address = input("请输入联系人的地址: ")
        self.contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("保存成功")

    def view_contacts(self):
        if not self.contacts:
            print("通讯录无信息")
            return
        for name, info in self.contacts.items():
            print(f"姓名: {name}, 手机号: {info['phone']}, 邮箱: {info['email']}, 地址: {info['address']}")

    def delete_contact(self):
        name = input("请输入要删除的联系人姓名: ")
        if name in self.contacts:
            del self.contacts[name]
            print("删除成功")
        else:
            print("该联系人不在通讯录中")

    def modify_contact(self):
        name = input("请输入要修改的联系人姓名: ")
        if name not in self.contacts:
            print("通讯录无信息")
            return
        new_name = input("请输入新的姓名: ")
        new_phone = input("请输入新的手机号: ")
        new_email = input("请输入新的邮箱: ")
        new_address = input("请输入新的地址: ")
        self.contacts[new_name] = {
            "phone": new_phone,
            "email": new_email,
            "address": new_address
        }
        if new_name != name:
            del self.contacts[name]
        print("修改成功")

    def find_contact(self):
        name = input("请输入要查找的联系人姓名: ")
        if name in self.contacts:
            info = self.contacts[name]
            print(f"姓名: {name}, 手机号: {info['phone']}, 邮箱: {info['email']}, 地址: {info['address']}")
        else:
            print("该联系人不在通讯录中")

    def exit_book(self):
        print("退出通讯录")
        exit()

def main():
    contact_book = ContactBook()
    while True:
        print("\n欢迎使用通讯录:")
        print("1. 添加联系人")
        print("2. 查看通讯录")
        print("3. 删除联系人")
        print("4. 修改联系人")
        print("5. 查找联系人")
        print("6. 退出")
        choice = input("请输入功能序号: ")

        if choice == '1':
            contact_book.add_contact()
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            contact_book.delete_contact()
        elif choice == '4':
            contact_book.modify_contact()
        elif choice == '5':
            contact_book.find_contact()
        elif choice == '6':
            contact_book.exit_book()
        else:
            print("无效的选项，请重新输入。")

if __name__ == "__main__":
    main()