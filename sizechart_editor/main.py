from aiohttp import web
from aiohttp_swagger import *
import os.path
from . import ROOT_PATH
from .api import api
from json.decoder import JSONDecodeError


async def index(request):
    """Temporary function to redirect the user to the online API documentation"""
    return web.HTTPFound('/api/doc')


async def json_error_handler_middleware(app, handler):
    """Fancy JSON error handler factory"""
    async def json_error_handler(request):
        """Fancy error handler to present all internal errors as JSON objects to the client"""
        try:
            return await handler(request)
        except JSONDecodeError:
            return web.json_response({"error": "Unable to parse json input"}, status=400)
        except web.HTTPException:
            raise
        except:
            return web.json_response({"error": "Internal server error"}, status=500)
    return json_error_handler


app = web.Application(middlewares=[json_error_handler_middleware])

app.router.add_get('/', index)
app.add_subapp(prefix='/charts', subapp=api)

setup_swagger(app, swagger_from_file=os.path.join(ROOT_PATH, 'swagger.yaml'))

if __name__ == '__main__':
    web.run_app(app, port=8000)

