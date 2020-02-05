from aiohttp import web
import json
import asyncio

queue = asyncio.Queue()


async def index(request):
    try:
        response_obj = {'status': 'success'}
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        response_obj = {'status': 'failed', 'reason': str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)


async def add_task(request):
    try:
        response_obj = {'status': 'success'}
        data = {'n': request.query['n'], 'd': request.query['d'], 'n1': request.query['n1'],
                'interval': request.query['interval']}
        queue.put_nowait(data)
        print("creating new object with {}", data)
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        response_obj = {'status': 'failed', 'reason': str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)


async def get_status(request):
    try:

        response_obj = {'status': 'success', 'queue_list': str(queue)}
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        response_obj = {'status': 'failed', 'reason': str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)
