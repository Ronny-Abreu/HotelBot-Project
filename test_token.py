import asyncio
import aiohttp
from config import DefaultConfig

async def test_token():
    config = DefaultConfig()
    secret = config.WEB_CHAT_SECRET
    print(f"Secret: {secret}")
    
    async with aiohttp.ClientSession() as session:
        headers = {"Authorization": f"Bearer {secret}"}
        async with session.get("https://webchat.botframework.com/api/tokens", headers=headers) as resp:
            print(f"Status: {resp.status}")
            text = await resp.text()
            print(f"Token: {text}")

if __name__ == "__main__":
    asyncio.run(test_token())
