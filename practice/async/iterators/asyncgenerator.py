"""
Basic example of async generator with asyncio.
"""

import asyncio
from typing import AsyncGenerator


async def gen(number: int) -> AsyncGenerator:

    for n in range(0, number):
        await asyncio.sleep(1)
        yield n


async def main():
    async for number in gen(5):
        print(number)


asyncio.run(main())
