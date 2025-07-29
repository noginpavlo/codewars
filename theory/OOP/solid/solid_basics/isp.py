from abc import ABC, abstractmethod
"""
I — Interface Segregation Principle (ISP)
===================================================================

is about:
Clients should not be forced to depend on interfaces they do not use.

In other words:

Prefer many small, specific interfaces over one large, general-purpose one.
"""

"""
Context:

Device	Can Call |	Can Access Internet	Can | Turn On/Off
OldPhone	✅	 |           ❌             |  	✅
NewPhone	✅   |           ✅             |  	✅
Tablet  	❌   |         	 ✅             | 	✅
"""


# let's VIOLATE the ISP
class SmartDevice(ABC):  # this interface is too conplex
    @abstractmethod
    def call(self): pass  # tablet will not be able to
    @abstractmethod
    def browse_internet(self): pass  # old phone will not be able to
    @abstractmethod
    def power_on(self): pass
    @abstractmethod
    def power_off(self): pass


class BadOldPhone(SmartDevice):
    def call(self): print("Calling...")

    def browse_internet(self):  # cannot borowse internet
        raise NotImplementedError("No internet access")

    def power_on(self): print("Powering on")
    def power_off(self): print("Shutting down")


class BadTablet(SmartDevice):
    def call(self):  # cannot call
        raise NotImplementedError("Tablets can't call")

    def browse_internet(self): print("Browsing internet")
    def power_on(self): print("Powering on")
    def power_off(self): print("Shutting down")


class BadNewPhone(SmartDevice):
    def call(self): print("Calling...")
    def browse_internet(self): print("Browsing internet")
    def power_on(self): print("Powering on")
    def power_off(self): print("Shutting down")


"""
So in the above example only NewPhone is using the complex interface fully.
Other devices are kinda implementation workarounds to bypass the interface frame
(interface says that the device must have all methods.
You cannot call? Must explicitly state that.
It can't call anywhay, why bother explicitly defining it?)
"""


# now let's separate dubious interface and create multiple small ones following ISP
class Hardware(ABC):
    @abstractmethod
    def power_on(self): pass
    @abstractmethod
    def power_off(self): pass


class Callable(ABC):
    @abstractmethod
    def call(self): pass


class InternetAccessing(ABC):
    @abstractmethod
    def access_internet(self): pass


"""
These interfaces can be used depending on the device capabilities
and type by utilizing class inheritance.
"""


class OldPhone(Hardware, Callable):
    def power_on(self):
        print("Old phone powering on")

    def power_off(self):
        print("Old phone shutting down")

    def call(self):
        print("Calling from old phone")


class Tablet(Hardware, InternetAccessing):
    def power_on(self):
        print("Tablet powering on")

    def power_off(self):
        print("Tablet shutting down")

    def browse_internet(self):
        print("Browsing internet on tablet")


class NewPhone(Hardware, InternetAccessing, Callable):
    def power_on(self):
        print("New phone powering on")

    def power_off(self):
        print("New phone shutting down")

    def call(self):
        print("Calling from new phone")

    def browse_internet(self):
        print("Browsing internet on new phone")


"""
So basically this way we separate dubious and overly complex interface chunks
so that clients =>
=> (code that uses functionality that is defined and implmeted somewhere else)
don't have to depend on interfaces that they do not use.
"""
