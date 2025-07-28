#!/usr/bin/env python3
"""Module with async coroutine that waits for a random delay."""

import asyncio
import random
from typing import Optional


async def wait_random(max_delay: Optional[int] = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay (inclusive).

    Args:
        max_delay (int, optional): Maximum delay in seconds. Defaults to 10.

    Returns:
        float: The delay time waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
