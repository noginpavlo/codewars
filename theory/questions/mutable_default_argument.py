"""
Чому використання змінних об'єктів як параметрів за замовчуванням погана
практика⚑

Функція створюється один раз під час завантаження модуля. Іменовані параметри
і їх значення за замовчуванням також створюються один раз і зберігаються в
одному з полів об'єкта-функції (__defaults__). Це стосується списків, множин і
словників.
"""

"""
This function defines a default value of def_list as a mutable type variable (list)
"""


def test_fucntion(def_list=[]):
    def_list.append("Change introduced")
    return def_list


"""
The def_list is a mutable type default value object that is stored somewhere
in memory.
The link to the object (def_list) is saved in __defaults__ atribute.
So the thing is every time any changes is applied to the mutable object
(def_list). It changed the default value (remember __defaults__ only contain
the link to the object, it means change the object, it changes __defaults__.
Nevertheles the declaration of the def_list is (def_list = []) which assumes
that it is empty.
This way the __defaults__ save any changes to the list and declaration says
that it is empty list. This is confusing and to be avoided.
"""

print(
    f"See the __defaults__ before performing .append on def_list:\n{
        test_fucntion.__defaults__}"
)

function_call1 = test_fucntion()
print(
    f"See the __defaults__ after the first .append performed on def_list:\n{
        test_fucntion.__defaults__}"
)

function_call2 = test_fucntion()
print(
    f"See the __defaults__ after the second .append performed on def_list:\n{
        test_fucntion.__defaults__}"
)

"""
Operations that test_function performs on def_list accumulate in __defaults__,
whearas declaration (def_list = []) says that the list is empty.
"""
