from aiohttp import web
from aiohttp_swagger import *
import os.path
from . import ROOT_PATH
from .api import api


async def index(request):
    return web.HTTPFound('/api/doc')


app = web.Application()
app.router.add_get('/', index)
app.add_subapp(prefix='/charts', subapp=api)

setup_swagger(app, swagger_from_file=os.path.join(ROOT_PATH, 'swagger.yaml'))

if __name__ == '__main__':
    web.run_app(app, port=8000)

