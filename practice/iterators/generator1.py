"""MODULE DOES: Finds users based on their names and prints all users and their age."""


def find_user_age(users: list[dict], target_name: str) -> str:
    return next((user["age"] for user in users if user["name"] == target_name), "Not found")


def print_users(users: list[dict]) -> None:
    for user in users:
        print(f"User: {user["name"]}, Age: {user["age"]}")


my_users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 40},
    {"name": "Alice", "age": 31},
]

print("Alice age:", find_user_age(my_users, "Alice"))
print("Bob age:", find_user_age(my_users, "Bob"))
print_users(my_users)
