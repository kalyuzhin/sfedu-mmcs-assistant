from app.services.speech.speech_synthesizer import SpeechSynthesizer
from app.services.speech.speech_recognizer import SpeechRecognizer
from app.services.api.response_service import ResponseService
from app.services.api.intent_service import IntentService
from app.db.milvus import Milvus
from app.services.api import client, settings


class App:
    def __init__(self):
        self.recognizer = SpeechRecognizer()
        self.synthesizer = SpeechSynthesizer()
        self.response_service = ResponseService(client)
        self.intent_service = IntentService(client)
        self.db = Milvus(settings.MILVUS_NAME)
