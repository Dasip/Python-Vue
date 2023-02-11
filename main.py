"""
Входная точка для ручного запуска
"""

from aiohttp import web
import app

web.run_app(app.get_app())
