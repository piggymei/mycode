#!/usr/bin/env python3

"""
This program exemplifies how to:

- Connect to the event loop
- Schedule a function to run in the event loop
- Run the event loop
"""

import asyncio
from datetime import datetime as dt
import time

def sundial():
    """
    This function sleeps for 1 second,
    then prints out the current time.
    
    Notice that this is a task that "blocks" 
    execution of other code
    """
    
    time.sleep(1)
    print(f"Sundial: {dt.now()}")

loop = asyncio.get_event_loop() # Connect to the event loop
loop.call_soon(sundial) # Schedule a function to run in the event loop
loop.call_soon(sundial) # Schedule another function to run in the event loop
loop.run_until_complete(asyncio.sleep(1)) # Run the event loop and sleep for 1 second

