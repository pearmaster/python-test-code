
import asyncio
import itertools
from aiostream import stream

async def number_generator(name, sleepytime):
    numbers_returned = 0
    while numbers_returned < 10:
        numbers_returned += 1
        await asyncio.sleep(sleepytime)
        yield (name, numbers_returned)

async def main():
    generator1 = number_generator("foo", 1)
    generator2 = number_generator("bar", 2)
    async for data in stream.merge(generator1, generator2):
        name, num = data
        print(f"{name} number {num}")

if __name__ == '__main__':
    asyncio.run(main())