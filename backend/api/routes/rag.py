from backend.models import QueryRequest
from shared.app import App
from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter(prefix="/rag", tags=["rag"])
app = App()


@router.post("/transcribe")
async def transcribe(audio: UploadFile = File(...)):
    try:
        content = await audio.read()
        text = app.recognizer.recognize_speech_bytes(content)
        return {"text": text}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))


@router.post("/query")
async def query_assistant(request: QueryRequest):
    try:
        intent = app.intent_service.get_intent(request.text)
        context = app.db.search_vectors(intent, "mmcs_data")
        response = app.response_service.make_response(context, request.text)
        return {"response": response}
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))
