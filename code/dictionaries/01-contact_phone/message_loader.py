from pathlib import Path
import yaml

class MessageLoader:
    def __init__(self, lang_code="en"):
        self.lang_code = lang_code
        self.messages = self._load_messages()

    def _load_messages(self) -> dict:
        path = Path(__file__).parent / "lang" / self.lang_code / "messages.yml"
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def get_messages(self) -> dict:
        return self.messages