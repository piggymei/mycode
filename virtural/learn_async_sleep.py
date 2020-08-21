#!/usr/bin/env python3

import asyncio
from datetime import datetime as dt
import time

async def rolex():
    await asyncio.sleep(1)
    print(f"Rolex: {dt.now()}")

async def main():
    # Fancy looking, but still slow
    print("Job 1:")
    await rolex()
    print("Job 2:")
    await rolex()
    
if __name__ == "__main__":
    asyncio.run(main())
