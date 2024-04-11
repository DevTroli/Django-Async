import asyncio
import httpx
from django.http import HttpResponse

async def http_call_async():
    for num in range(1, 11):
        await asyncio.sleep(2)
        print(num)
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://httpbin.org")
            print(response)
    except httpx.HTTPStatusError as errorHTTP:
        print(f"Error making HTTP request: {errorHTTP}")
    except Exception as ex:  # Pega a exceção do código 
        print(f"Unexpected error: {ex}")

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())

    return HttpResponse("Using asynchronism in the Django framework")


