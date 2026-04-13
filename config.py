import os
from dotenv import load_dotenv

load_dotenv()


class DefaultConfig:
    """Configuración para el bot"""

    PORT = int(os.environ.get("PORT", 8000))
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    APP_TYPE = os.environ.get("MicrosoftAppType", "SingleTenant")
    APP_TENANT_ID = os.environ.get("MicrosoftAppTenantId", "")

    # Azure Translator
    TRANSLATOR_KEY = os.environ.get("TRANSLATOR_KEY", "")
    TRANSLATOR_ENDPOINT = os.environ.get("TRANSLATOR_ENDPOINT", "")
    TRANSLATOR_REGION = os.environ.get("TRANSLATOR_REGION", "")

    # Azure OpenAI
    AZURE_OPENAI_KEY = os.environ.get("AZURE_OPENAI_KEY", "")
    AZURE_OPENAI_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT", "")
    AZURE_OPENAI_DEPLOYMENT = os.environ.get("AZURE_OPENAI_DEPLOYMENT", "")
    AZURE_OPENAI_API_VERSION = os.environ.get(
        "AZURE_OPENAI_API_VERSION", "2024-12-01-preview"
    )
