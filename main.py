def get_fullname(first_name, last_name, middle_name = ""):
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"
first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your last name: "))
middle_name = str(input("Enter your middle name: "))
get_fullname(first_name, last_name, middle_name)#fixed
    