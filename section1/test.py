# def greet(name):
#     message = "hello"
#     # new_message = message.capitalize()
#     return f"{name}さん！{message}"

# input_name = input('Please Enter your name: ')
# greeting = greet(name=input_name)

# print(greeting.capitalize())

# check_isdigit = []
# check = {"length":False,"upper":False,"digit":False}

# def strength(password):
#     if len(password) >= 8:
#         check["length"] = True
#     if password.islower() == False:
#         check["upper"] = True
#     for n in password:
#         if n.isdigit() == True:
#             check_isdigit.append("True")
#             # check["digit"]=True
#     if True in check_isdigit:
#         check["digit"] = True
    
#     return check
    
# # print(strength("aaaa"))

# c_num = list(check.values()).count("True")

# if c_num != 3:
#     print("Weak Password")


def speed(time,distance,):
    return distance / time
    
print(speed(5, 300))
    
