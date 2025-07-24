"""
This is an OCP SOLID pattern that I found in 'Clean Code in Python'.
The pattern helps to avoid creating a lot of if/elif statements by createing classes.
"""

"""
=> Basically we need to identify the event type that happened in some system.
=> The system sends formated in a particular way data. We need to read the data and determine
the event type. 

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


"""Interface: Event"""
class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meets_condition(event_data: dict) -> bool: #  @staticmethod does not take self parameter btw.
        return False


"""Low-level Module: LoginEvent, LogoutEvent, UnknownEvent"""
class LoginEvent(Event):

    @staticmethod
    def meets_condition(event_data: dict):
        return (
            event_data["before"]["session"] == 0
            and event_data["after"]["session"] == 1
        )


class LogoutEvent(Event):

    @staticmethod
    def meets_condition(event_data: dict):
        return (
            event_data["before"]["session"] == 1
            and event_data["after"]["session"] == 0
        )


class UnknownEvent(Event):
    """This is a Null Object Pattern. It returns itself(UnknownEven object) and does nothing when event in unknown"""


class SystemMonitor:
    """This class identifies events that occur in the system. It is a High-level Module"""

    def __init__(self, event_data: dict):
        self.event_data = event_data

    def identify_event(self):
        for event_cls in Event.__subclasses__():
            try:
                if event_cls.meets_condition(self.event_data):
                    return event_cls(self.event_data)
            except KeyError:
                continue
        return UnknownEvent(self.event_data)
