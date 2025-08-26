def add_friend(friends=None, person=None, friend=None) -> dict[str, list[str]]:
    friends = friends or {}
    friends.setdefault(person, []).append(friend)
    return friends


all_friends = add_friend(person="Alice", friend="Bob")
all_friends = add_friend(person="Alice", friend="Charlie")
print(all_friends)
