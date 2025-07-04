import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
         users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)

def filter_users_by_age(min_age):
    with open("users.json", "r") as file:
         users = json.load(file)
    filtered_user = [user for user in users if user["age"] >= min_age]

    for user in filtered_user:
        print(user)

def filter_by_email(target_email):
    with open("users.json", "r") as file:
         users = json.load(file)
    filtered_user=[user for user in users if user.get("email") == target_email]

    for user in filtered_user:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, 'name','age' and 'email' are supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
         min_age = int(input("Enter an age to filter users: ").strip())
         filter_users_by_age(min_age)
    elif filter_option == "email":
         email_to_search = input("Enter an email to filter users: ").strip()
         filter_by_email(email_to_search)


    else:
        print("Filtering by that option is not yet supported.")
