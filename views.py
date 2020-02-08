from aiohttp import web
from datetime import datetime
import json
from tasks import queue

QUEUED = "queued"
RUNNING = "running"


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
        data = {'queue_num': queue.qsize(),
                'n': request.query['n'],
                'd': request.query['d'],
                'n1': request.query['n1'],
                'interval': request.query['interval'],
                'status': QUEUED,
                'cur_val': request.query['n1'],
                'start_date': datetime.now().strftime('%Y-%m-%d %H:%M')
                }
        await queue.put(data)
        print("creating new object with ", data)
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        response_obj = {'status': 'failed', 'reason': str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)


async def get_status(request):
    try:

        response_obj = {'status': 'success', 'queue_list': str(queue.qsize())}

        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        response_obj = {'status': 'failed', 'reason': str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)
