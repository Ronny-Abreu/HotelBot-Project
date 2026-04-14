# 🏨 Hotel Paradise International — AI Concierge

[![Azure](https://img.shields.io/badge/Azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white)](https://azure.microsoft.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

**Hotel Paradise International** es una landing page de alta gama diseñada para presentar un asistente de conserjería virtual inteligente. Utilizando la potencia de la inteligencia artificial generativa, el sistema permite a los hoteles ofrecer una atención al huésped multilingüe, automatizada y de lujo las 24 horas del día.

---

## ✨ Características Principales

- **🌎 Multilingüe Nativo**: Soporte para más de 60 idiomas con detección automática.
- **🧠 IA Generativa (GPT-4o)**: Conversaciones fluidas y naturales basadas en el knowledge base del hotel.
- **⚡ Respuesta en Tiempo Real**: Procesamiento y entrega de mensajes en menos de 2 segundos.
- **🎨 Interfaz Premium**: Diseño moderno con animaciones GSAP, ScrollTrigger y modo oscuro nativo.
- **📱 Experiencia Mobile First**: Totalmente optimizado para dispositivos móviles con navegación fluida.
- **🤖 Roadmap de Arquitectura**: Visualización clara del flujo de procesamiento de datos.

---

## 🛠️ Stack Tecnológico

### Backend & AI
- **Python 3.10+**: Lenguaje principal del servidor y lógica del bot.
- **Azure Bot Service**: Orquestador de la mensajería y conexión con canales.
- **Azure OpenAI (GPT-4o)**: El "cerebro" detrás de la comprensión del lenguaje natural.
- **Azure Translator**: Motor de detección y traducción instantánea de idiomas.
- **Aiohttp**: Servidor asíncrono para manejar la landing y el bot.

### Frontend
- **HTML5 & Vanilla CSS**: Estructura y estilos personalizados (High-level design).
- **JavaScript (ES6+)**: Lógica de interacción y cambio de temas.
- **GSAP & ScrollTrigger**: Animaciones de scroll cinematográficas y micro-interacciones.

---

## 🏗️ Cómo funciona la magia

El proceso se divide en tres capas fundamentales para garantizar una experiencia sin fricciones para el huésped:

1. **Detección Automática (Azure Translator)**: 
   Funciona como un traductor inteligente que detecta instantáneamente el idioma del huésped (francés, japonés, árabe, etc.) y normaliza el mensaje para su procesamiento interno.
   
2. **Procesamiento Inteligente (Azure OpenAI)**:
   Es el **cerebro** del bot. Recibe el contexto, entiende la intención del huésped (pedir desayuno, preguntar por el check-out o solicitar transporte) y genera una respuesta coherente y hospitalaria.

3. **Entrega de Respuesta (Azure Bot Service)**:
   Actúa como el **mensajero**. Toma la respuesta del cerebro, la traduce de vuelta al idioma original del huésped y la proyecta en la interfaz en milisegundos.

---

## 🚀 Instalación y Despliegue Local

### Requisitos Previos
- Python 3.10 o superior.
- Una cuenta de Azure con recursos de Bot Service, OpenAI y Translator configurados.

### Pasos
1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Ronny-Abreu/HotelBot-Project.git
   cd HotelBot-Project
   ```

2. **Configurar el entorno:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Variables de Entorno:**
   Crea un archivo `.env` basado en `.env.example` y completa tus credenciales de Azure.

4. **Ejecutar el servidor:**
   ```bash
   python app.py
   ```
   Abre [http://localhost:8000](http://localhost:8000) en tu navegador.

---

## 🌐 Despliegue en Producción

El proyecto incluye flujos de trabajo de **GitHub Actions** configurados en `.github/workflows/main_hotelbot-itla.yml` para el despliegue automático en **Azure App Service**.

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo para más detalles.

---
*Desarrollado para Hotel Paradise International — Elevando la hospitalidad con Inteligencia Artificial.*
