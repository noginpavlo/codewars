from abc import ABC, abstractmethod

"""
Let's define some properties that a device needs to have:
is_hardware, call, sms, web-search

>>> Now let's creat interfaces that will be a base for creating devices that
have those properties.
"""


class hardware(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class can_call(ABC):

    @abstractmethod
    def call(self):
        pass


class can_sms(ABC):

    @abstractmethod
    def sms(self):
        pass


class can_web_search(ABC):

    @abstractmethod
    def web_search(self):
        pass


"""
Now let's create devices:
"""


class old_phone(hardware, can_call, can_sms):

    def __init__(self, imei: int):
        self.imei: int = imei

    def turn_on(self):
        print("I have been turned on")

    def turn_off(self):
        print("I have been turned off")


class new_phone(hardware, can_call, can_sms, can_web_search):

    def __init__(self, imei: int):
        self.imei: int = imei

    def turn_on(self):
        print("I have been turned on")

    def turn_off(self):
        print("I have been turned off")

    def can_sms(self):
        print("Hey, I can send you an sms!")

    def can_web_search(self):
        print("What do you want me to search?")


class tablet(hardware, can_web_search):

    def __init__(self, imei: int):
        self.imei: int = imei

    def turn_on(self):
        print("I have been turned on")

    def turn_off(self):
        print("You have turned me off")

    def can_web_search(self):
        print("What do you want me to search?")


"""
So this was multiple inheritance.
By using that we created devices that are all hardware, but have different
properties like sms, call, web-search etc.
"""
