
import random, string

feet_inches = input("Enter feet and inches:")

def convert(feet_inches):
    nums = feet_inches.split(" ")
    feet = float(nums[0])
    inches = float(nums[1])

    meters = feet * 0.3048 + inches * 0.0254


    return feet,inches,meters

feet,inches,meters = convert(feet_inches)
print("You need to be 2 meters tall to ride this slide.")
if meters < 2:
    print(f"You're meter equal to {meters},you are {2-meters} meters short.")
else:
    print(f"{feet} feet and {inches} inches is equal to {meters} meters.")



# 長さ n のランダムな英数字文字列（大文字・小文字のアルファベット＋数字）を返します。
# 文字は重複ありでランダムに選ばれます（復元抽出）。
# def randomname(n):
#    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))


# num = int(input("choose num: "))
# print(randomname(num))