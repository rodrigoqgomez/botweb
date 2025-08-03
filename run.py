import os
import asyncio
from app import app as flask_app
from hypercorn.asyncio import serve
from hypercorn.config import Config

async def run_flask():
    config = Config()
    port = int(os.environ.get("PORT", 5000))
    config.bind = [f"0.0.0.0:{port}"]
    await serve(flask_app, config)

if __name__ == "__main__":
    asyncio.run(run_flask())
