import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

async def run_api():
    process = await asyncio.create_subprocess_exec(
        'uvicorn', 'api.main:app', '--host', '0.0.0.0', '--port', '8000'
    )
    await process.wait()