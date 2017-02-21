import pytest
from aiohttp import web
from sizechart_editor.api import setup_routes
from sizechart_editor.main import json_error_handler_middleware
import json


@pytest.fixture
def client(loop, test_client):
    app = web.Application(loop=loop, middlewares=[json_error_handler_middleware])
    setup_routes(app)
    return loop.run_until_complete(test_client(app))


def post(client, route, data):
    return client.post(route,
                       headers={'Content-Type': 'application/json',
                                'Accept': 'application/json'},
                       data=json.dumps(data)
                       )
