

def get_age(year_of_birth,current_year=2026):
    if year_of_birth < 2000:
        age = current_year - 2000
        extra_num = 2000 - year_of_birth
        age += extra_num
    else:
        age = current_year - year_of_birth
    return age



birth = int(input("Please enter your date of birth in the Gregorian calendar. : "))
print(get_age(birth))