from aiohttp import web


async def get_index(request):
    return web.json_response({})


async def post_index(request):
    return web.json_response({})


async def get_chart(request):
    return web.json_response({})


async def put_chart(request):
    return web.json_response({})


async def delete_chart(request):
    return web.json_response({})




api = web.Application()
api.router.add_get('/', get_index)
api.router.add_post('/', post_index)
api.router.add_get(r'/{id:\d+}', get_chart)
api.router.add_put(r'/{id:\d+}', put_chart)
api.router.add_delete(r'/{id:\d+}', delete_chart)
