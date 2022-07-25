import asyncio
from asyncio import ensure_future, Task, sleep

async def do_something_asynchronously(t):
    await sleep(t)
    return t

def print_result(the_task):
    print(the_task.result())

def do_something():
    future_result = ensure_future(do_something_asynchronously(3))
    future_result.add_done_callback(print_result)

async def run():
    do_something()
    await sleep(10)
    print("Done")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())