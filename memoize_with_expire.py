"""
Contains memoize class for caching function results with an expiration time.
"""
from time import time


class MemoizeWithExpiry(object):
    """
    Wrap a function so that results for any argument tuple are stored in the attribute cache. Note that
    the args to the function must be usable as a dictionary keys. Only cache results younger than expiry_time
    (seconds) will be returned.

    NOTE: Calling wrapped functions with keyword arguments current results in errors.

    Args:
        cache (dict or dict-like object): Houses the stored data.
        expiry_time (int): Time in seconds until the cache expires, meaning the time until the cache will no longer
            be used and the function result will be recalculated.
        num_args (int): Default None, which means all arguments are important. Number of important args to verify
            when looking up in the cache for a stored result.

    Attributes:
        Same as Args.
    """
    def __init__(self, cache, expiry_time=0, num_args=None):
        self.cache = cache
        self.expiry_time = expiry_time
        self.num_args = num_args

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            """
            Higher order function that checks if the function result for the given *args have been calculated
            within the past expiry_time seconds. If the cached result exists, that is returned, else the function
            is run normally, the result is cached and the result is returned.

            Args:
                *args: List will act as the cache key (at least the first part of it)

            Returns:
                Normal function result
            """
            # TODO get working with kwargs
            if kwargs:
                raise NotImplementedError("Use only positional arguments.")

            mem_args = args[:self.num_args]
            # Check the cache
            if mem_args in self.cache:
                result, timestamp = self.cache[mem_args]
                # Check the age
                age = time() - timestamp
                if not self.expiry_time or age < self.expiry_time:
                    return result
            # Get a new result
            result = func(*args)
            # Cache it
            self.cache[mem_args] = (result, time())
            # Return it
            return result
        return wrapped
