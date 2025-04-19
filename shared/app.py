from shared.speech.speech_synthesizer import SpeechSynthesizer
from shared.speech.speech_recognizer import SpeechRecognizer
from shared.api.response_service import ResponseService
from shared.api.intent_service import IntentService
from shared.db.milvus import Milvus
from shared.api import client, settings


class App:
    def __init__(self):
        self.recognizer = SpeechRecognizer()
        self.synthesizer = SpeechSynthesizer()
        self.response_service = ResponseService(client)
        self.intent_service = IntentService(client)
        self.db = Milvus(settings.MILVUS_NAME)

    def startup(self):
        pass


