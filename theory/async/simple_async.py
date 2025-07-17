import asyncio
import datetime
import random

"""
Fust the structure of the async coroutine
"""


async def hello():
    print("Example1: hello!")


async def main1():
    await hello()
    print("Example1: finished")


asyncio.run(main1())


"""
Now an example with time delay.
Function say_hello and say_goodbye start in the same time, then they wait
(like sumulating I/O).
The sooner the function completed, the sooner it prints End.
So they are executed sumultaniously, and curated in the way that who ends
first gets the chance to print End.
"""


async def say_hello():
    print("Start hello!")
    await asyncio.sleep(2)
    print("End hello!")


async def say_goodbye():
    print("Start goodbye!")
    await asyncio.sleep(1)
    print("End goodbye!")


async def main2():
    task1 = asyncio.create_task(say_hello())
    task2 = asyncio.create_task(say_goodbye())

    await task1
    await task2


asyncio.run(main2())


"""
Now the hardest example in this file.
These coroutines run loops with random delay, this shows that they are
not executed in particular order, they are executed as soon as delay ends.
The random order of executing those loops exemplifies async execution.
As soon as one task ends other starts.

>>> Loop1 takes 3 seconds to recharge
>>> Loop2 is running and sets 5 second recharge
>>> Loop3 is ready to execute wearas Loops 1 and 2 sleep for 3 and 5 seconds.
>>> Loop3 executes and sets up recharge delay to 5 sec.
>>> All 3 loops are on cooldown. The program just waits.
>>> Loop1 is recharged after 3 seconds. Executes.
"""


async def delay():
    await asyncio.sleep(random.randint(0, 5))


async def display_date(num: int):
    start_time = asyncio.get_event_loop().time()
    end_time = start_time + 10

    while True:
        print(f"Loop: {num}, Time: {datetime.datetime.now()}")
        if asyncio.get_event_loop().time() >= end_time:
            break
        await delay()


async def main3():
    task1 = asyncio.create_task(display_date(1))
    task2 = asyncio.create_task(display_date(2))
    task3 = asyncio.create_task(display_date(3))

    await task1
    await task2
    await task3


asyncio.run(main3())
