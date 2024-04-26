#!/usr/bin/env python3
"""
Asynchronous coroutine takes an integer argument(max_delay)
then waits for a random delay between 0 and max_delay
seconds and eventually returns it as a float
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns a random number between 0 and max_delay"""
    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number
