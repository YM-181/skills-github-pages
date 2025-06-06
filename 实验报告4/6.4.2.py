#姓名：王薪洋，学号：24210227016，日期，25.6.4
prices = [399, 4369, 539, 288, 109, 749, 235, 190, 99, 1000]

max_price = int(input("请输入最大价格："))
min_price = int(input("请输入最小价格："))

filtered_prices = [price for price in prices if min_price <= price <= max_price]

sort_order = input("请选择排序方式（1：升序，2：降序）：")

if sort_order == '1':
    sorted_prices = sorted(filtered_prices)
elif sort_order == '2':
    sorted_prices = sorted(filtered_prices, reverse=True)
else:
    print("输入的排序方式不正确，程序将使用默认升序排序。")
    sorted_prices = sorted(filtered_prices)

print("排序后的价格区间内的商品价格如下：")
for price in sorted_prices:
    print(price)