"""
Módulo de Inteligencia Artificial.

Este paquete contiene las implementaciones de los distintos proveedores
de IA, la gestión de prompts y las clases comunes utilizadas durante
el proceso de extracción.
"""

from .base_client import BaseAIClient
from .gemini_client import GeminiClient
from .prompt_manager import PromptManager
from .extraction_result import ExtractionResult

__all__ = [
    "BaseAIClient",
    "GeminiClient",
    "PromptManager",
    "ExtractionResult",
]