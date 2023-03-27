from aiohttp import web
from asyncio import sleep, ensure_future
    
async def stream_url(request):
    print(request)
    response = web.StreamResponse()
    response.content_type = "text/plain"
    await response.prepare(request)
    for i in range(10):
        b = bytearray(f"{i}\r\n", 'utf-8')
        await response.write(b)
        await sleep(2)
    print("Done")
    return response

async def foo(request):
    return web.json_response('hello')

app = web.Application()
#app.router.add_get('/stream', stream_url)
#app.router.add_get('/foo', foo)
web.run_app(app, host='127.0.0.1', port=8080)