from .helpers import client, post
import json
from pprint import pprint


async def test_no_content_type(client):
    resp = await client.post('/', headers={}, data='')
    assert resp.status == 406


async def test_wrong_content_type(client):
    resp = await client.post('/', headers={'Content-Type': 'text/plain'}, data='')
    assert resp.status == 406


async def test_malformed_json_data(client):
    resp = await client.post('/', headers={'Content-Type': 'application/json'}, data='sdfdsfsdfsd')
    assert resp.status == 400


async def test_empty_query(client):
    data = {}
    resp = await post(client, '/', data)
    assert resp.status == 422
    assert resp.content_type == 'application/json'
    result = json.loads(await resp.text())
    assert 'name' in result
    assert 'unit' in result


async def test_name_and_unit(client):
    data = {
        "name": "A fancy size chart",
        "unit": "cm"
    }
    resp = await post(client, '/', data)
    assert resp.status == 200
    assert resp.content_type == 'application/json'
    result = json.loads(await resp.text())


async def test_unit_cm(client):
    resp = await post(client, '/', {'unit': 'cm'})
    assert resp.status == 422
    assert resp.content_type == 'application/json'
    result = json.loads(await resp.text())
    assert 'unit' not in result


async def test_unit_in(client):
    resp = await post(client, '/', {'unit': 'in'})
    assert resp.status == 422
    assert resp.content_type == 'application/json'
    result = json.loads(await resp.text())
    assert 'unit' not in result


async def test_unit_not_in_cm(client):
    resp = await post(client, '/', {'unit': 'inch'})
    assert resp.status == 422
    assert resp.content_type == 'application/json'
    result = json.loads(await resp.text())
    assert 'unit' in result


async def test_url_relative_format(client):
    resp = await post(client, '/', {'url': '/something/relative.json'})
    assert resp.status == 422
    assert resp.content_type == 'application/json'
    result = json.loads(await resp.text())
    assert 'url' in result


async def test_url_jibberish(client):
    resp = await post(client, '/', {'url': 'something relative json'})
    assert resp.status == 422
    assert resp.content_type == 'application/json'
    result = json.loads(await resp.text())
    assert 'url' in result


async def test_url_absolute(client):
    resp = await post(client, '/', {'url': 'http://github.com'})
    assert resp.status == 422
    assert resp.content_type == 'application/json'
    result = json.loads(await resp.text())
    assert 'url' not in result



async def test_full_query(client):
    chart = {
        "name": "Women’s sizes",
        "designation": "women",
        "vendor": "",
        "region": "US",
        "unit": "in",
        "url": "https://en.wikipedia.org/wiki/US_standard_clothing_size",
        "elements": [
            {
                "code": "34",
                "body_parts": [
                    {
                        "name": "bust",
                        "size": 38
                    },
                    {
                        "name": "waist",
                        "size": 30
                    },
                    {
                        "name": "hip",
                        "size": 39
                    },
                    {
                        "name": "back_waist_length",
                        "size": 17.25
                    }
                ]
            },
            {
                "code": "36",
                "body_parts": [
                    {
                        "name": "bust",
                        "size": 40
                    },
                    {
                        "name": "waist",
                        "size": 32
                    },
                    {
                        "name": "hip",
                        "size": 41
                    },
                    {
                        "name": "back_waist_length",
                        "size": 17.375
                    }
                ]
            }
        ]
    }

    resp = await post(client, '/', chart)

    # print(await resp.text())
    assert resp.status == 200
    assert resp.content_type == 'application/json'

