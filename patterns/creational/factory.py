from abc import ABC, abstractmethod

"""
This code includes factory pattern because it controls the creation of object
based on conditional input.

Purpose of a Factory:
Decide which concrete class to instantiate based on some input or condition.
Factory return instance like return LogoutEvent() if particular conditions are met.

Factory pattern consists of:
=> FACTORY PRODUCT INTERFACE (interface)
=> FACTORY CONCRETE PRODUCT (concrete implementation of interface)
=> FACTORY or also called FACTORY METHOD
(orchestrator that instatniates needed class if meets condition)
=> CLIENT (caller == calls factory)

"""


# factory product interface
class Event(ABC):
    """Interface for Login, Logout and Unknown events"""

    @staticmethod
    @abstractmethod
    def meets_condition(event_data: dict) -> bool: ...

    # this is a conditional for creating and object that is common in factory pattern


# factory concrete product
class LoginEvent(Event):
    """Event for login"""

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return event_data["before"]["session"] == 0 and event_data["after"]["session"] == 1


# factory concrete product
class LogoutEvent(Event):
    """Event for logout"""

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return event_data["before"]["session"] == 1 and event_data["after"]["session"] == 0


# factory concrete product
class UnknownEvent(Event):
    """Fallback"""

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        """This is a Null Object pattern. It ignores event_data on purpose."""
        return False


# factory (factory method)
class SystemMonitor:
    """
    Factory identifies Event type and instantiates even subclass based on conditional input
    """

    def identify_event(self, event_data):

        for cls in Event.__subclasses__():
            if cls.meets_condition(event_data):
                return cls()

        return UnknownEvent()


# client
monitor = SystemMonitor()
EventType = monitor.identify_event({"before": {"session": 1}, "after": {"session": 0}})
print(EventType.__class__.__name__)
