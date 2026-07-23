from pathlib import Path


class PromptManager:

    def __init__(self):

        self.base_path = (
            Path(__file__)
            .resolve()
            .parent
            .parent
            / "prompts"
        )

    def get_system_prompt(self) -> str:

        archivo = self.base_path / "system_prompt.txt"

        return archivo.read_text(
            encoding="utf-8"
        )

    def get_user_prompt(self) -> str:

        archivo = self.base_path / "user_prompt.txt"

        return archivo.read_text(
            encoding="utf-8"
        )