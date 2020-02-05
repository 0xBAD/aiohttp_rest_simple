from views import index, add_task, get_status


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/new_task', add_task)
    app.router.add_get('/get_status', get_status)
