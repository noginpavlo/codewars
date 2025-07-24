"""
This is an OCP SOLID pattern that I found in 'Clean Code in Python'.
The pattern helps to avoid creating a lot of if/elif statements by createing classes.
"""

"""
What this code does is:
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
                    |         Low-Level Modules (Event Types)     |
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


