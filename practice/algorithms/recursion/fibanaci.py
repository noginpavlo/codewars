"""
Basic solution of fibanaci problem.
"""

from functools import lru_cache


@lru_cache  # caches already computed values (LRU: least recently used)
def fibanaci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibanaci(n - 1) + fibanaci(n - 2)


print(fibanaci(100))
