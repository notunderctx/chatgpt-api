from __future__ import annotations
from turbo import Turbo
import asyncio
import pretty_errors
import tracemalloc
tracemalloc.start()
async def main():
    turbo = Turbo()
    await turbo.tubo()

if __name__ == "__main__":
    asyncio.run(main())
