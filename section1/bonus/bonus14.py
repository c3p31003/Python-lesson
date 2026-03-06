# from bonus.parsers14 import parse
from parsers14 import parse
from convert14 import convert
#5 6.142

feet_inches = input("Enter feet and inches:")


nums = feet_inches.split(" ")
f,i = parse(nums)


result = int(convert(f,i) * 100)
print(result,"cm")
if result < 1:
    print("Kid is too small.")
else:
    print("kid can use the slide.")



# 長さ n のランダムな英数字文字列（大文字・小文字のアルファベット＋数字）を返します。
# 文字は重複ありでランダムに選ばれます（復元抽出）。
# def randomname(n):
#    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))


# num = int(input("choose num: "))
# print(randomname(num))