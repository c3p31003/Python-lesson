import webbrowser

# user_term = input("Enter a search term: ").split()

# def split_str(arr):
#     sum_str = ""
#     for i,val in enumerate(arr):
#         if not(i == len(arr)-1):
#             sum_str += val+"+"
#         else:
#             sum_str += val
#     return sum_str

# webbrowser.open(f"https://www.google.com/search?q={split_str(user_term)}")


user_term = input("Enter a search term: ").replace(" ","+")


webbrowser.open(f"https://www.google.com/search?q={user_term}")