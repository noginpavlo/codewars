from abc import ABC, abstractmethod

"""
Implement not a great system
"""


# interface
class Event(ABC):
    """Interface for Login, Logout and Unknown events"""

    @staticmethod
    @abstractmethod
    def meets_contidion(event_data: dict) -> bool: ...


# low-level module
class LoginEvent(Event):
    """Event for login"""

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return event_data["before"]["session"] == 0 and event_data["after"]["session"] == 1


class LogoutEvent(Event):
    """Event for logout"""

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return event_data["before"]["session"] == 1 and event_data["after"]["session"] == 0


class UnknownEvent(Event):
    """Fallback"""

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        """This is a Null Object pattern. It ignores event_data on purpose."""
        return False


# high-level module
class SystemMonitor:
    """
    Client that identifies Event type and return Event
    """

    def identify_event(self, event_data):

        for cls in Event.__subclasses__():
            if cls.meets_condition(event_data):
                return cls

        return UnknownEvent


monitor = SystemMonitor()
EventType = monitor.identify_event({"before": {"session": 1}, "after": {"session": 0}})
print(EventType.__name__)
