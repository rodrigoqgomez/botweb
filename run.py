import asyncio
from app import app as flask_app

async def run_flask():
    from hypercorn.asyncio import serve
    from hypercorn.config import Config

    config = Config()
    config.bind = ["0.0.0.0:5000"]
    await serve(flask_app, config)

if __name__ == "__main__":
    asyncio.run(run_flask())
