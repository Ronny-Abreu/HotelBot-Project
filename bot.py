# Lógica central del HotelBot
import uuid
import aiohttp
from typing import List
from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount
from openai import AzureOpenAI
from config import DefaultConfig
import prompts

CONFIG = DefaultConfig()


class HotelBot(ActivityHandler):

    def __init__(self):
        self.llm_client = AzureOpenAI(
            azure_endpoint=CONFIG.AZURE_OPENAI_ENDPOINT,
            api_key=CONFIG.AZURE_OPENAI_KEY,
            api_version=CONFIG.AZURE_OPENAI_API_VERSION,
        )

    # ── 1. Bienvenida cuando el huésped abre el chat ──
    async def on_members_added_activity(
        self, members_added: List[ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(prompts.WELCOME_MESSAGES["es"])

    # ── 2. Cuando el huésped escribe un mensaje ──
    async def on_message_activity(self, turn_context: TurnContext):
        texto_usuario = turn_context.activity.text

        # A) Detección de idioma y traducción
        idioma_detectado, texto_traducido = await self._traducir(texto_usuario)

        # B) Escalamiento — se evalúa sobre el texto ya traducido al español
        if any(
            keyword in texto_traducido.lower() for keyword in prompts.ESCALATION_KEYWORDS
        ):
            idioma_clave = (
                idioma_detectado
                if idioma_detectado in prompts.ESCALATION_MESSAGE
                else "es"
            )
            await turn_context.send_activity(prompts.ESCALATION_MESSAGE[idioma_clave])
            return

        # C) Llamada al cerebro (Azure OpenAI)
        respuesta_final = await self._consultar_openai(
            texto_traducido, idioma_detectado
        )

        # D) Enviar respuesta al huésped
        await turn_context.send_activity(respuesta_final)

    # ── Traducción ──
    async def _traducir(self, texto: str):
        idioma_detectado = "es"
        texto_traducido = texto

        url = f"{CONFIG.TRANSLATOR_ENDPOINT}/translate"
        params = {"api-version": "3.0", "to": "es"}
        headers = {
            "Ocp-Apim-Subscription-Key": CONFIG.TRANSLATOR_KEY,
            "Ocp-Apim-Subscription-Region": CONFIG.TRANSLATOR_REGION,
            "Content-type": "application/json",
            "X-ClientTraceId": str(uuid.uuid4()),
        }
        body = [{"text": texto}]

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    url, params=params, headers=headers, json=body
                ) as resp:
                    resultado = await resp.json()
                    idioma_detectado = resultado[0]["detectedLanguage"]["language"]
                    texto_traducido = resultado[0]["translations"][0]["text"]
        except Exception as e:
            print(f"[Translator Error] {e}")

        return idioma_detectado, texto_traducido

    async def _consultar_openai(self, texto_traducido: str, idioma: str) -> str:
        try:
            respuesta = self.llm_client.chat.completions.create(
                model=CONFIG.AZURE_OPENAI_DEPLOYMENT,
                messages=[
                    {"role": "system", "content": prompts.SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": (
                            f"El huésped dice (traducido al español): {texto_traducido}. "
                            f"Responde SIEMPRE en este idioma: '{idioma}'."
                        ),
                    },
                ],
                temperature=0.7,
                max_tokens=300,
            )
            return respuesta.choices[0].message.content

        except Exception as e:
            print(f"[OpenAI Error] {e}")
            return (
                "Lo siento, tengo problemas de conexión. "
                "Por favor llame a recepción: Ext. 0."
            )
