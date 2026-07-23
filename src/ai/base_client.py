from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Any


class BaseAIClient(ABC):
    """
    Contrato base para cualquier proveedor de IA.
    """

    @abstractmethod
    def extract_json(
        self,
        pdf_path: Path,
        system_prompt: str,
        user_prompt: str
    ) -> Dict[str, Any]:
        """
        Recibe un PDF y devuelve un JSON válido.

        Raises:
            Exception si la extracción falla.
        """
        pass