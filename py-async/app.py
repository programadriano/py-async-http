import aiohttp
import asyncio
import json

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response_json = await response.text()
            data = json.loads(response_json)  
            if data:  
                print("Primeiro item do array:", data[0])
            else:
                print("Array está vazio")

loop = asyncio.get_event_loop()
loop.run_until_complete(fetch('https://financialmodelingprep.com/api/v3/search?query=AA&apikey=D8dRfKqo22VYZJNjL0RtQJ0fxQ1VS4en'))
