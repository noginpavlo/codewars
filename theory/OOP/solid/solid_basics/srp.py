"""
SINGLE RESPONSIBILITY PRINCIPLE
=============================================================================================

is:
=> A class should have only one reason to change,
meaning it should have only one job or responsibility.
"""


# let's defined a BAD class that handles 3 things at a time
class BadClass:
    def __init__(self, data):
        self.bad_data = data

    def do_first_thing(self):
        pass

    def do_second_thing(self):
        pass

    def do_third_thing(self):
        pass


"""
Such bad class as above invokes following problems potentially:
1. Can couple functionality unintentionally.
2. Makes it harder to test.
3. Less readable code.
"""


# now let's create a classes that follow SRP
class GoodClass:
    def __init__(self, data):
        self.good_data = data


class DoFitstThing:
    """
    In this function good_class expects an instance of
    GoodClass to pass it as an argument
    """
    def do_the_thing(self, good_class: GoodClass):
        pass


class DoSecontThing:
    def do_the_thing(self, good_class: GoodClass):
        pass


class DoThirdThing:
    def do_the_thing(self, good_class: GoodClass):
        pass


"""
This code follows SRP
"""
