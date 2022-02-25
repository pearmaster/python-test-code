
import asyncio

class A:

    def __init__(self):
        self._lock = asyncio.Lock()

    async def do_something_long(self, i):
        print("Begin Wait {}".format(i))
        await asyncio.sleep(2)
        print("End Wait {}".format(i))

    async def call_me(self, i):
        async with self._lock:
            await self.do_something_long(i)

async def do_a_few_things(count):
    a = A()
    tasks = []
    for i in range(0, count):
        tasks.append(a.call_me(i))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(do_a_few_things(5))

    