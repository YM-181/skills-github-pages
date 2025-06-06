#姓名：王薪洋，学号：24210227016，日期，25.6.6
def identify_day(first_letter, second_letter=None):
    days = {
        'm': ['Monday', 'Wednesday', 'Friday'],
        't': ['Tuesday', 'Thursday'],
        'w': ['Wednesday'],
        'f': ['Friday'],
        's': ['Saturday'],
        'h': ['Thursday'],
        'a': ['Saturday', 'Sunday'],
        'u': ['Sunday']
    }

    if first_letter in days:
        if len(days[first_letter]) == 1:
            return days[first_letter][0]
        elif second_letter and second_letter in days[first_letter][0]:
            return days[first_letter][0]
        else:
            return "请根据提示输入第二个字母"
    else:
        return "请输入正确的字母"


first_input = input("请输入第一个字母: ")
result = identify_day(first_input)
if result == "请根据提示输入第二个字母":
    second_input = input("请输入第二个字母: ")
    result = identify_day(first_input, second_input)
print(result)