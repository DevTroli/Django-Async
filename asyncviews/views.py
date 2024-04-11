import asyncio
import httpx
from django.http import HttpResponse

async def http_call_async():
    for num in range(1,11):
        await asyncio.sleep(2)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Using asynchronism in the Django framework")


