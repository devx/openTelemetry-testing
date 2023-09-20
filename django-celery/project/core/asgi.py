"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import sys
from pathlib import Path


from django.core.asgi import get_asgi_application
from opentelemetry.instrumentation.asgi import OpenTelemetryMiddleware

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(ROOT_DIR / "emr_api"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

django_application = get_asgi_application()
django_application = OpenTelemetryMiddleware(django_application)

from config.websocket import websocket_application  # noqa isort:skip

async def application(scope, receive, send):
    if scope["type"] == "http":
        await django_application(scope, receive, send)
    elif scope["type"] == "websocket":
        await websocket_application(scope, receive, send)
    else:
        raise NotImplementedError(f"Unknown scope type {scope['type']}")
