from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import Response
from shared.backend.app.models import QueryRequest
from shared.app import App

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


@router.post("/synthesize")
async def synthesize(request: QueryRequest):
    try:
        _bytes = app.synthesizer.synthesize_speech_gtts(request.text)

        return Response(content=_bytes, media_type="audio/mpeg")
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))


@router.post("/process")
async def process(audio: UploadFile = File(...)):
    try:
        content = await audio.read()
        text = app.recognizer.recognize_speech_bytes(content)
        intent = app.intent_service.get_intent(text)
        context = app.db.search_vectors(intent, "mmcs_data")
        response_text = app.response_service.make_response(context, text)
        _bytes = app.synthesizer.synthesize_speech_gtts(response_text)

        return Response(content=_bytes, media_type="audio/mpeg")
    except Exception as ex:
        print(str(ex))
        raise HTTPException(status_code=500, detail=str(ex))
