# Author：zhaoyanqi

shopping_list = []
product_list = []
money_list = open("money","r")
f_shoppinglist = open("shoppinglist","r",encoding="utf-8")
shopping_list.append(f_shoppinglist.read())
f_shoppinglist.close()

money_str = str(money_list.read())
if len(money_str) > 0:
    money = money_str
else:
    money = input('请输入你的工资：')
money_list.close()
f_shoppinglist2 = open("shoppinglist","w",encoding="utf-8")
money_list2 = open("money","w")



list = open("product","r",encoding="utf-8")

for line in list:
    product_line = line.strip().split()
    product_line[1] = int(product_line[1])
    product_line = tuple(product_line)
    product_list.append(product_line)

if money.isdigit():
    money = int(money)
    while True:
        for index, i in enumerate(product_list):
            print(index, i)
        Number = input("请输入商品编号，按q退出:")
        if Number.isdigit():
            Number = int(Number)
            if Number < len(product_list) and Number >= 0:
                p_item = product_list[Number]
                if money > p_item[1]:
                    money -= p_item[1]
                    shopping_list.append(p_item)
                    print("你的余额还剩\033[31;1m[%s]\033[0m"%money)
                else:
                    print("你就剩\033[31;1m[%s]\033[0m了，还买个毛线啊"% money)
            else:
                print("没有这个商品")
        elif Number == 'q':
            for i3 in shopping_list:
                print(i3)
                f_shoppinglist2.write(str(i3))
            f_shoppinglist2.close()
            print('您的余额还剩[%s]'% money)
            money_list2.write(str(money))
            money_list2.close()
            exit()
        else:
            print("请正确输入")

else:
    print('请输入数字')