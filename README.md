# HotelBotAzure
Detalles:
1. Azure Translator detecta el idioma
Es como un traductor automático de Google pero de Microsoft. En cuanto el huésped escribe, el sistema detecta si está en francés, japonés, árabe, etc. y traduce el mensaje al español o inglés para que el bot lo entienda.
2. Azure OpenAI procesa la pregunta
Es el "cerebro" del bot. Recibe el mensaje ya traducido, entiende qué quiere el huésped (pedir desayuno, hacer check-out, pedir transporte, etc.) y formula una respuesta inteligente.
3. Azure Bot Service devuelve la respuesta
Es el "mensajero". Toma la respuesta del cerebro, la traduce de vuelta al idioma original del huésped, y la muestra en la pantalla. El huésped nunca se da cuenta de todo lo que pasó por detrás.
