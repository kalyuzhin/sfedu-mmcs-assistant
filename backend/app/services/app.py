from backend.app.services.speech.speech_synthesizer import SpeechSynthesizer
from backend.app.services.speech.speech_recognizer import SpeechRecognizer
from backend.app.services.api.response_service import ResponseService
from backend.app.services.api.intent_service import IntentService
from backend.app.db.milvus import Milvus
from backend.app.services.api import client, settings


class App:
    def __init__(self):
        self.recognizer = SpeechRecognizer()
        self.synthesizer = SpeechSynthesizer()
        self.response_service = ResponseService(client)
        self.intent_service = IntentService(client)
        self.db = Milvus(settings.MILVUS_NAME)
