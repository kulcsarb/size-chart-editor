from aiohttp import web
from webargs.aiohttpparser import parser
from .schema import SizeChart
from pprint import pprint


async def get_index(request):
    return web.json_response({})


async def post_index(request):
    if request.headers['Content-Type'] != 'application/json':
        raise web.HTTPNotAcceptable()

    data = await parser.parse(SizeChart, request)

    return web.json_response({})


async def get_chart(request):
    chart_id = request.match_info['id']

    return web.json_response({})


async def put_chart(request):
    if request.headers['Content-Type'] != 'application/json':
        raise web.HTTPNotAcceptable()
    chart_id = request.match_info['id']
    data = await parser.parse(SizeChart, request)

    return web.json_response({})


async def delete_chart(request):
    chart_id = request.match_info['id']

    return web.json_response({})


# class SizeChartController(web.View):
#
#     async def post(self):
#         if self.request.headers['Content-Type'] != 'application/json':
#             raise web.HTTPNotAcceptable()
#
#         args = await parser.parse(SizeChart, self.request)
#
#         return web.json_response({})
#
#     async def get(self):
#         return web.json_response({})
#


def setup_routes(api):
    """Make routes addable to any given application instance

    """
    # api.router.add_route('*', '/', SizeChartController)

    api.router.add_get('/', get_index)
    api.router.add_post('/', post_index)
    api.router.add_get(r'/{id:\d+}', get_chart)
    api.router.add_put(r'/{id:\d+}', put_chart)
    api.router.add_delete(r'/{id:\d+}', delete_chart)


api = web.Application()
setup_routes(api)
