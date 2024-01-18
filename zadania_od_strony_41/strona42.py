def name_plus_surname():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    capitalized_name = name.title()
    capitalized_surname = surname.title()

    full_name = capitalized_name + " " +capitalized_surname

    print(f"Your full name is {full_name}")
    return full_name

name_plus_surname()