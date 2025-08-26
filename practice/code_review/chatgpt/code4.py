def read_numbers_from_file(path: str, default: list[int] | None = None) -> list[int]:
    default = default or []

    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    if lines:
        return [int(line.strip()) for line in lines]
    return default


print(read_numbers_from_file("numbers1.txt"))
print(read_numbers_from_file("numbers2.txt"))
