import hashlib
users = {}

def register(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[username] = hashed_password
    print(f"User {username} registered successfully!")

def login(username, password):
    if username in users:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        if users[username] == hashed_password:
            print("Login Successful.")
        else:
            print("Invalid password.")
    else:
        print("Username not found.")

register("sakshi", "Acharya12")  
login("sakshi", "Acharya12")     
login("sakshi", "Acharya012")  
