"""
"""
from nanigans.config import AUTH

class Credentials(object):

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
        self._credentials = AUTH if all(AUTH.values()) else None

    @property
    def credentials(self):
        return self._credentials
    
    def __repr__(self):
        return "<[Credentials Object]>"
