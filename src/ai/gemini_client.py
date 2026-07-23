import json
import os
from pathlib import Path
from typing import Dict, Any

from dotenv import load_dotenv
from google import genai

from ai.base_client import BaseAIClient
from google.genai import types

load_dotenv()


class GeminiClient(BaseAIClient):

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise Exception(
                "No existe GEMINI_API_KEY en el .env"
            )

        self.client = genai.Client(
            api_key=api_key
        )

        self.model = os.getenv(
            "MODEL",
            "gemini-2.5-pro"
        )

    def extract_json(
        self,
        pdf_path: Path,
        system_prompt: str,
        user_prompt: str
    ) -> Dict[str, Any]:

        print(f"Subiendo {pdf_path.name}...")

        archivo = self.client.files.upload(
            file=pdf_path
        )

        print("Generando respuesta...")

        response = self.client.models.generate_content(

            model=self.model,

            contents=[
                archivo,
                system_prompt,
                user_prompt
            ]
        )

        texto = response.text.strip()

        # Eliminar markdown si Gemini lo devuelve
        if texto.startswith("```"):

            texto = (
                texto
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

        try:

            return json.loads(texto)

        except json.JSONDecodeError as e:

            raise Exception(
                f"""
Gemini devolvió un JSON inválido.

Error:

{e}

Respuesta:

{texto}
"""
            )