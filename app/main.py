from fastapi import FastAPI
import asyncio


app = FastAPI()

async def main():
    await asyncio.sleep(0)
    
    
if __name__ == '__main__':
    asyncio.run(main())