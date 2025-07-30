import string

"""
The coding challenge comes from this video:
https://www.youtube.com/watch?v=eVNtrNWdha0

"""

alphabet_string = string.ascii_lowercase

encription_dict = dict(enumerate(alphabet_string))
print(encription_dict)


def encript(string: str) -> list[int]:
    return [
        key
        for letter in string
        for key, value in encription_dict.items()
        if value == letter
    ]


def decode(some_list: list[int]) -> list[str]:
    return [
        value
        for digit in some_list
        for key, value in encription_dict.items()
        if key == int(digit)
    ]


encripted_data = encript("cat")
print(f"Encoded data: {encripted_data}")

decoded_data = decode(encripted_data)
print(f"Decoded data: {"".join(decoded_data)}")
