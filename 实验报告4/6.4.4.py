#姓名：王薪洋，学号：24210227016，日期，25.6.4
chinese_numerals = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]

def arabic_to_chinese(num):
    if isinstance(num, int):
        if num == 0:
            return chinese_numerals[0]
        elif num > 0:
            result = ""
            while num > 0:
                digit = num % 10
                result = chinese_numerals[digit] + result
                num //= 10
            return result
        else:
            return "输入的数字必须是正整数"
    elif isinstance(num, str):
        if num.isdigit():
            num = int(num)
            return arabic_to_chinese(num)
        else:
            return "输入的字符串不是数字"
    else:
        return "输入类型不支持"

input_num = input("请输入一个阿拉伯数字：")
print(f"转换为中文大写数字是：{arabic_to_chinese(input_num)}")