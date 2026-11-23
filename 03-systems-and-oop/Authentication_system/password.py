import re 
import bcrypt


def validate_password(password):

    if len(password)< 10:
        return False, " password must contain at least 10 charecters"

    if not re.search(r"[A-Z]", password):
        return False ," password must contain an uppercase letter"

    if not re.search(r"[a-z]",password):
        return False ,"password must contain a lowercase letter"

    if not re.search(r"[@$!%*?&#]", password):
        return False ,"password must contain a special chrecter "
    
    if not re.search(r"[0-9]", password):
        return False ," password must contain a number" 

    return True ," such a strong password ! "


# check this function 
password = input("Enter password: ")

is_valid, message = validate_password(password)

print(message)


def validate_username(username):

    if len(username)<3:
        return False , " Username is too sort "

    if len(username)> 25:
        return False, "Username is too long "

    if not username.replace("_", "").isalnum():
        return False , "username can only contains letter ,number and underscore"

    return True , "Valid username"


# check username 
username = input("Enter username: ")

is_valid, message = validate_username(username)

print(message)




def validate_email(email):

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if re.match(pattern, email):
        return True, "Valid email"

    return False, "Invalid email"