import aiohttp
import asyncio

async def run():
    try:
        print("Creating session")
        async with aiohttp.ClientSession() as session:
            print("Making request")
            async with session.get("http://localhost:8080/stream") as resp:
                async for line in resp.content:
                    print(f"Line '{line}'")
                print("Done iterating over response content")
            print("Done with response")
        print("done with session")
    except Exception as e:
        print(f"Caught exception: {e}")

if __name__ == '__main__':
    asyncio.run(run())