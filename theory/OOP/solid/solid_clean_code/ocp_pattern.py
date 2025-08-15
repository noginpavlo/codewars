from abc import ABC, abstractmethod
from collections.abc import Mapping

"""
This is an OCP SOLID pattern that I found in 'Clean Code in Python'.
The pattern helps to avoid creating a lot of if/elif statements by creating classes.
"""

"""
=> In this example we need to identify the event type that happened in some system.
=> The system sends formatted data (preformated in a particular way).
=> We need to read the data and determine the event type based on it.

The schema of the code:

                    +----------------------+
                    |  High-Level Module   |
                    |  (SystemMonitor)     |
                    +----------------------+
                            |
                            | calls identify_event()
                            v
                    +----------------------+
                    |      Interface       |
                    |       (Event)        |
                    | => Stores raw_data   |
                    | => Declares shared   |
                    |   structure & method |
                    |   (meets_condition)  |
                    +----------------------+
                            |
                            | uses __subclasses__()
                            v
                    +--------------------------------------------+
                    |         Low-Level Modules (Event Types)    |
                    |                                            |
                    | +------------------+   +-----------------+ |
                    | |   LoginEvent     |   |  LogoutEvent    | |
                    | |------------------|   |-----------------| |
                    | | @staticmethod    |   | @staticmethod   | |
                    | | meets_condition  |   | meets_condition | |
                    | | Check: session   |   | Check: session  | |
                    | | 0 → 1 (login)    |   | 1 → 0 (logout)  | |
                    | +------------------+   +-----------------+ |
                    |                                            |
                    | +------------------+                       |
                    | |  UnknownEvent     | ← fallback           |
                    | +------------------+                       |
                    | | always returns    |                      |
                    | | False             |                      |
                    | +------------------+                       |
                    +--------------------------------------------+
                            |
                            | Based on matches
                            v
                    +--------------------------+
                    |   Returns correct Event  |
                    |   instance (LoginEvent,  |
                    |   LogoutEvent, etc.)     |
                    +--------------------------+
"""


class Event(ABC):
    """
    This is an abstract base class that validates preconditions
    and provides interface for subtypes of it.
    """

    @staticmethod
    def validate_preconditions(event_data: dict) -> None:
        """
        Validates data structure of event_data defining precondition to meet.
        """

        if not isinstance(event_data, Mapping):
            raise ValueError(f"{event_data!r} not in a dict")
        for moment in ("before", "after"):
            if moment not in event_data:
                raise ValueError(f"{moment} not in {event_data!r}")

    @staticmethod  # @staticmethod does not take self parameter btw.
    @abstractmethod
    def meets_condition(event_data: dict) -> bool: ...


class LoginEvent(Event):
    """Low-level Module: LoginEvent, LogoutEvent, UnknownEvent"""

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return event_data["before"]["session"] == 0 and event_data["after"]["session"] == 1


class LogoutEvent(Event):

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return event_data["before"]["session"] == 1 and event_data["after"]["session"] == 0


class UnknownEvent(Event):
    """
    This is a Null Object Pattern. It ignores event_data on purpose. Still has it thought
    because required by LSP and the logic of identify_event().
    """

    @staticmethod
    def meets_condition(event_data: dict) -> bool:  # event_data is not used on purpose
        return False


class SystemMonitor:
    """
    This class identifies events that occur in the system.
        => It is a High-level Module by the way.
    """

    def __init__(self, event_data: dict[str, str]):
        self.event_data = event_data

    def identify_event(self):
        """Identifies event if preconditionas are met."""

        Event.validate_preconditions(self.event_data)
        for event_cls in Event.__subclasses__():
            if event_cls.meets_condition(self.event_data):
                return event_cls(self.event_data)

        return UnknownEvent(self.event_data)
