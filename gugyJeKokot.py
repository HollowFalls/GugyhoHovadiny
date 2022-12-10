"""
UDP  2019/2020 - cviceni 4
"""

def check_login(users, user_name, user_password):
    for user in users:
        if user["name"] == user_name:
            if user["password"] == user_password:
                return True
            else:
                return False
    return False

def inverse_dict(in_dict):
    keys = list(in_dict.keys())
    new_dict = {}
    for key in keys:
        new_dict[in_dict[key]] = key

    return new_dict

username = "user1"
password = "pass1"

users = [
        {"name": "user1", "password": "pass1"}
        ]

print(check_login(users, username, password))
in_dict = {"kys": "kokote", "kokotí": "zmrde"}
print(in_dict)
print(inverse_dict(in_dict))

