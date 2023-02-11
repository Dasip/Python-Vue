"""
Входная точка для ручного запуска
"""
import asyncio

from aiohttp import web
import app

# async def hello(request):
#     return web.Response(text="HELLO")
#
#
# app = web.Application()
# app.add_routes([web.get('/', hello)])

web.run_app(app.get_app())


