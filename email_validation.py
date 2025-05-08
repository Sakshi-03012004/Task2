import re
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        return True
    else:
        return False
print(is_valid_email("Sakshi123@gmail.com"))  
print(is_valid_email("sakshi_10 @gmail"))
