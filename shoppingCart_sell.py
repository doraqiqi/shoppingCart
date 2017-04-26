# Author：zhaoyanqi

list = open("product","r",encoding="utf-8")

product_list = []


while True:
    for line in list:
        product_line = line.strip().split()
        product_line[1] = int(product_line[1])
        product_line = tuple(product_line)
        product_list.append(product_line)
    for index, i in enumerate(product_list):
        print(index, i)
    print("-------------------------------")
    choice_list = ["添加", "删除", "退出"]
    for index2, i2 in enumerate(choice_list):
        print(index2 + 1, i2)
    choice = input("请输入你的选择：")
    if choice == "1":
        input_product = input("请输入商品名：")
        input_price = input("请输入价格：")
        f_product = open("product","a",encoding="utf-8")
        f_product.write(input_product)
        f_product.write(" ")
        f_product.write(input_price)
        f_product.write("\n")
        f_product.close()
        print("已成功添加")
    elif choice =="2":
        input_del = input("请输入要删除的商品编号")
        if input_del.isdigit():
            input_del = int(input_del)
            product_list.pop(input_del)
            list_new = open("product", "w", encoding="utf-8")
            for line in product_list:
                list_new.write(line[0] + " " + str(line[1]) + "\n")
        else:
            print("请输入数字！")

    elif choice == "3":
        exit()
    else:
        print("请输入正确选项！")
