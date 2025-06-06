#姓名：王薪洋，学号：24210227016，日期，25.6.4
lottery = ["谢谢惠顾", "一等奖", "二等奖", "三等奖", "谢谢惠顾", "三等奖", "二等奖", "谢谢惠顾"]
prize_index = int(input("请输入您要刮开的兑奖区编号（1~8）："))
if 1 <= prize_index <= 8:

    prize_info = lottery[prize_index - 1]
    print(f"您刮开的兑奖区{prize_index}的兑奖信息是：{prize_info}")
else:
    print("输入的位置不合规，请重新输入1到8之间的数字。")
