from fastapi import FastAPI
import asyncio

from routers.router import ROUTER as router 

app = FastAPI()

app.include_router(router)
#app.include_router()

async def main():
    await asyncio.sleep(0)
    
    
if __name__ == '__main__':
    asyncio.run(main())