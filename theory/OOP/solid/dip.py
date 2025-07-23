from abc import ABC, abstractmethod
"""
D — Dependency Inversion Principle (DIP)
===============================================================================

is about:
High-level modules should not depend on low-level modules. Both should depend on abstractions.
Abstractions should not depend on details. Details should depend on abstractions.
-------------------------------------------------
          [ High-Level Module ]                  |
                   │                             |
                   │  depends on                 |
                   ▼                             |
             [ Abstraction / Interface ]         |
                   ▲                             |
                   │  implemented by             |
         ┌─────────┴──────────┐                  |
         │                    │                  |
[ Low-Level Module A ]  [ Low-Level Module B ]   |
-------------------------------------------------

where, 

1. High level module => your code, everything outside the interface
2. Abstraction/Interface => interface
3. Low-Level Module => child classes that inherit from an interface
"""

"""
So basically: 
"everything depends on an interface"
-- Highlander's rule
"""


# let's VIOLATE DIR first
class BadOldPhone: 
    def power_on(self):
        print("Old phone powering on")

    def call(self):
        print("Calling from old phone")

class BadTablet:
    def power_on(self):
        print("Tablet powering on")

    def browse_internet(self):
        print("Browsing on tablet")

class BadDeviceManager:
    def use_old_phone(self):
        phone = BadOldPhone()   # Directly instantiating concrete class inside method, no dependency injection
        phone.power_on()
        phone.call()

    def use_tablet(self):
        tablet = BadTablet() # Directly instantiating concrete class inside method, no dependency injection
        tablet.power_on()
        tablet.browse_internet()

"""
This makes High-level Module depend on Low-level Moule, not interface.
"""


# now let's implement the code properly following DIR

# implementing interfaces first
class Electric(ABC):
    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass


class Callable(ABC):
    @abstractmethod
    def call(self):
        pass


class InternetAccessing(ABC):
    @abstractmethod
    def browse_internet(self):
        pass


# now implement Low-level Module classes
class OldPhone(Electric, Callable):

    def power_on(self):
        print("Welcome to the system")

    def power_off(self):
        print("Buy, bro")

    def call(self):
        print("Calling ...")


class Tablet(Electric, InternetAccessing):

    def power_on(self):
        print("Welcome to the Tablet")

    def power_off(self):
        print("Tablet is swithching off")

    def browse_internet(self):
        print("Enter you search keywords")


# implement High-level Module code with dependency injection (depends on interface, not on Low-level Module)
class DeviceManager:
    # on this line don't get confused. caller = Callable|None is a type annotation.
    # But = None is a default value of caller
    def __init__(self, power: Electric, caller: Callable|None = None, browser: InternetAccessing|None = None):
        self.power = power
        self.caller = caller
        self.browser= browser

    def turn_on(self):
        self.power.power_on()

    def turn_off(self):
        self.power.power_off()

    def call(self):
        if self.caller:
            self.caller.call()

    def browse(self):
        if self.browser:
            self.browser.browse_internet()

# usage
old_phone = OldPhone()
tablet = Tablet()

dm_phone = DeviceManager(power=old_phone, caller=old_phone)

dm_phone.turn_on()
dm_phone.call()
dm_phone.turn_off()

print("----------------------------------")

dm_tablet = DeviceManager(power=tablet, browser=tablet)

dm_tablet.turn_on()
dm_tablet.browse()
dm_tablet.turn_off()
