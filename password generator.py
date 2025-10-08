import random
def passwordgenerator():
    length = int(input("Enter the length of the password: "))
    if length < 8:
        print("Password length should be atleast 8 characters.")
        return ""
    chars = {
        "lowerchars": list("abcdefghijklmnopqrstuvwxyz"),
        "upperchars": list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        "specialchars": list("!@#$%^&*-_|"),
        "numericchars": list("0123456789")
    }



    password = [
        random.choice(chars["lowerchars"]),
        random.choice(chars["upperchars"]),
        random.choice(chars["specialchars"]),
        random.choice(chars["numericchars"])
    ]


    allchars = []
    for group in chars.values():
        allchars += group


    password += random.choices(allchars, k=length - 4)


    random.shuffle(password)    




    return ''.join(password)
print("Your password is: " + passwordgenerator())