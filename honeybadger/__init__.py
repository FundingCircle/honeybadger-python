"""
Use cases:

>>> from honeybadger import honeybadger
>>> honeybadger.notify()
>>> honeybadger.configure(**kwargs)
>>> honeybadger.context(**kwargs)
"""

from .version import __version__

__all__ = ['honeybadger', '__version__']
