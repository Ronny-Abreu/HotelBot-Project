# app.py — Servidor principal del HotelBot
import sys
import traceback
from datetime import datetime
from http import HTTPStatus

from aiohttp import web
from aiohttp.web import Request, Response, json_response
from botbuilder.core import (
    BotFrameworkAdapterSettings,
    TurnContext,
    BotFrameworkAdapter,
)
from botbuilder.schema import Activity, ActivityTypes

from bot import HotelBot
from config import DefaultConfig

CONFIG = DefaultConfig()

SETTINGS = BotFrameworkAdapterSettings(
    app_id=CONFIG.APP_ID,
    app_password=CONFIG.APP_PASSWORD,
    channel_auth_tenant=CONFIG.APP_TENANT_ID,
)

ADAPTER = BotFrameworkAdapter(SETTINGS)
BOT = HotelBot()


# ── Manejo de errores globales ──
async def on_error(context: TurnContext, error: Exception):
    print(f"\n[on_turn_error] Error: {error}", file=sys.stderr)
    traceback.print_exc()
    await context.send_activity(
        "❌ El bot encontró un error. Por favor intenta de nuevo."
    )
    if context.activity.channel_id == "emulator":
        trace_activity = Activity(
            label="TurnError",
            name="on_turn_error",
            timestamp=datetime.utcnow(),
            type=ActivityTypes.trace,
            value=f"{error}",
            value_type="https://www.botframework.com/schemas/error",
        )
        await context.send_activity(trace_activity)


ADAPTER.on_turn_error = on_error


# ── Endpoint principal ──
async def messages(req: Request) -> Response:
    if req.content_type != "application/json":
        return Response(status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE)

    body = await req.json()
    activity = Activity().deserialize(body)
    auth_header = req.headers.get("Authorization", "")

    response = await ADAPTER.process_activity(activity, auth_header, BOT.on_turn)
    if response:
        return json_response(data=response.body, status=response.status)
    return Response(status=HTTPStatus.OK)


import aiohttp

# ── Landing Page ──
async def index(req: Request) -> Response:
    try:
        with open("web/index.html", "r", encoding="utf-8") as f:
            content = f.read()

        token = "ERROR_GENERANDO_TOKEN"
        if CONFIG.WEB_CHAT_SECRET:
            try:
                # Generamos un token temporal para no exponer el Secret Key en la web (Mejor Práctica)
                async with aiohttp.ClientSession() as session:
                    headers = {"Authorization": f"Bearer {CONFIG.WEB_CHAT_SECRET}"}
                    async with session.get("https://webchat.botframework.com/api/tokens", headers=headers) as resp:
                        if resp.status == 200:
                            token = (await resp.text()).strip('"')
            except Exception as e:
                print(f"Error fetcheando token web chat: {e}")
                
        # Inyectamos el token en lugar de la Secret Key
        content = content.replace("{{WEB_CHAT_TOKEN}}", token)
        return Response(text=content, content_type="text/html")
    except Exception as e:
        return Response(text=f"Error cargando landing: {str(e)}", status=500)


APP = web.Application()
APP.router.add_post("/api/messages", messages)

import os as _os
if _os.path.isdir("web"):
    APP.router.add_get("/", index)
    APP.router.add_get("/index.html", index)
    APP.router.add_static("/", "web")

if __name__ == "__main__":
    try:
        port = int(CONFIG.PORT)
        web.run_app(APP, host="0.0.0.0", port=port)
    except Exception as error:
        raise error
