import asyncio
from app import app as flask_app
import bot

async def run_flask():
    from hypercorn.asyncio import serve
    from hypercorn.config import Config

    config = Config()
    config.bind = ["0.0.0.0:5000"]
    await serve(flask_app, config)

async def main():
    bot_task = asyncio.create_task(bot.start_bot())
    flask_task = asyncio.create_task(run_flask())
    await asyncio.gather(bot_task, flask_task)

if __name__ == "__main__":
    asyncio.run(main())
