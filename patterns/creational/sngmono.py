"""
The Monostate pattern, also called SNGMONO, is a design approach where multiple instances of
a class can exist, but all instances share the same underlying state. Unlike a classic singleton,
which strictly enforces only one instance of a class, the Monostate pattern allows you to create
as many objects as you like, while ensuring that any changes to the state in one instance are
reflected in all other instances. You might use this pattern instead of a singleton when you want
the flexibility of multiple objects—for example, for cleaner code, easier testing, or better
modularity—while still maintaining a single, shared state. The key difference is that with
a singleton, you are constrained to a single object, whereas with Monostate, the “singleton
behavior” exists in the shared state, not the object itself, so each instance is a normal object
but behaves as if there is only one state. This aligns with the excerpt you mentioned: the objects
appear independent, but their data is synchronized automatically and transparently, without
the user needing to manage how that synchronization happens.
"""

import logging

logger = logging.getLogger(__name__)


class GitFetcher:
    """Fetches the data from Git and ensures consictent version across all instances."""

    _current_tag = None

    def __init__(self, tag):
        self.current_tag = tag

    @property
    def current_tag(self):
        if self._current_tag is None:
            raise AttributeError("tag was never set")
        return self._current_tag

    @current_tag.setter
    def current_tag(self, new_tag):
        self.__class__._current_tag = new_tag

    def pull(self):
        logger.info("pulling from %s", self.current_tag)
        return self.current_tagt.me / DevTwitter
