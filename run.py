import asyncio
from aiohttp import web
from routes import setup_routes
from tasks import queue


async def listen_to_queue(app):
    try:
        while True:
            await asyncio.sleep(3.0)
            task = await queue.get()
            print("Task: ", task)
    except asyncio.CancelledError:
        pass


async def start_background_tasks(app):
    app['queue_listener'] = asyncio.create_task(listen_to_queue(app))


async def cleanup_background_tasks(app):
    app['queue_listener'].cancel()
    await app['queue_listener']


async def main():
    app = web.Application()
    setup_routes(app)
    app.on_startup.append(start_background_tasks)
    app.on_cleanup.append(cleanup_background_tasks)
    return app


if __name__ == '__main__':
    web.run_app(main())
