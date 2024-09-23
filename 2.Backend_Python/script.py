import re
import json

# Task data are not valid, before created new list need fixed data
users = """[{"name": "Kamil", "country":"Poland", {"name":"John", "country": "USA"}, {"name":"Yeti"}]"""
print("Input data:", users)




def replace_pattern(data_str):
    # complete the specialized symbol like "{" and "}"
    pattern = r'"[^"]{0,3}"name'
    result = re.sub(pattern, '"}, {"name', data_str)

    return result

def validate_and_fix_user_list(users):
    fixed_users = []
    for user in users:
        # Checking if an element is a dictionary
        if not isinstance(user, dict):
            print(f"Invalid entry: {user} - not a valid dictionary")
            continue

        # Completing missing keys if 'name' or 'country' is missing
        if "name" not in user:
            user["name"] = "Unknown"
        if "country" not in user:
            user["country"] = "Unknown"

        fixed_users.append(user)

    return fixed_users

def filter_by_country(users, country):
    filtered_users = []
    for user in users:
        if user["country"] == country:
            filtered_users.append(user)
    return filtered_users



# 1. Calling the pattern replacement function
modified_data = replace_pattern(users)
print("Modified data:", modified_data)

# 2. Converting (deserializing) modified text to a Python list
try:
    users_list = json.loads(modified_data)
except json.JSONDecodeError as e:
    print(f"Error parsing JSON: {e}")
    users_list = []

# 3. Calling the function that repairs the list
fixed_users = validate_and_fix_user_list(users_list)
print("Fixed list:", fixed_users)

# 4. Filtering users from Poland
polish_users = filter_by_country(fixed_users, "Poland")
print("Polish users:", polish_users)
