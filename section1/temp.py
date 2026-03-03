name = input("enter name: ")
age = input("enter age: ")
height = input("enter height: ")

#リストを作成
user_info = []
#リストにname変数を追加
user_info.append(name+"\n")
user_info.append(age+"\n")
user_info.append(height+"\n")
#TERMINALにLISTを表示
print(user_info)



with open("natsuki_info.txt", 'w') as file:
    file.writelines(user_info)

user_order = input("if you want to clean the text , Enter clean: ")

if user_order == "clean":
    with open("natsuki_info.txt", 'r') as file:
        natsuki = file.readlines()
    natsuki.clear()
    
    with open("natsuki_info.txt", 'w') as file:
        file.writelines(natsuki)



