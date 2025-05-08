# List of users (initial data)
users = [
    {"id": 1, "name": "sannidhi", "email": "sannidhis.22.beis@acharya.ac.in"},
    {"id": 2, "name": "saloni", "email": "salonis.22.beis@acharya.ac.in"}
]
def create_user(user_id, name, email):
    new_user = {"id": user_id, "name": name, "email": email}
    users.append(new_user)
    print(f"User {name} added successfully!")
def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None
def update_user(user_id, name=None, email=None):
    user = get_user_by_id(user_id)
    if user:
        if name:
            user["name"] = name
        if email:
            user["email"] = email
        print(f"User with ID {user_id} updated successfully!")
    else:
        print(f"User with ID {user_id} not found.")
def delete_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        users.remove(user)
        print(f"User with ID {user_id} deleted successfully!")
    else:
        print(f"User with ID {user_id} not found.")
create_user(3, "Sakshi", "ksakshi33333@gmail.com")
create_user(4, "Ridham", "sharmaridham276@gmail.com")
user = get_user_by_id(2)
if user:
    print(f"User found: {user}")
else:
    print("User not found.")
update_user(3, name="samiksha", email="samikshas.22.beis@acharya.ac.in")
delete_user(4)
print("Final user list:")
print(users)
