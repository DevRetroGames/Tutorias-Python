from pathlib import Path
import yaml

# Folder where the language files (YAML) are stored
LANG_FOLDER = "i18n"

class MessageLoader:
    """
    Loads localized messages from a YAML file based on the given language code.
    """

    def __init__(self, lang_code="en"):
        # Set the language code (default is English)
        self.lang_code = lang_code
        # Load messages during initialization
        self.messages = self._load_messages()

    def _load_messages(self) -> dict:
        """
        Load the messages.yml file for the specified language.
        """
        # Build the path to the messages.yml file
        path = Path(__file__).parent / LANG_FOLDER / self.lang_code / "messages.yml"
        
        # Open the YAML file and load its content into a dictionary
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def get_messages(self) -> dict:
        """
        Return the loaded messages dictionary.
        """
        return self.messages