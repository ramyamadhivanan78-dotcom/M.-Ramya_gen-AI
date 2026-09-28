from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations
from models import TextRequest

app = FastAPI(
    title="EduGenie",
    description="Google Gemini powered learning assistant",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/health")
async def health():
    return {"status": "ok", "service": "EduGenie"}


@app.post("/qa")
async def qa(request: TextRequest):
    try:
        return {"result": answer_question(request.text)}
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc))


@app.post("/explain")
async def explain(request: TextRequest):
    try:
        return {"result": explain_topic(request.text)}
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc))


@app.post("/quiz")
async def quiz(request: TextRequest):
    try:
        return generate_quiz(request.text).model_dump()
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc))


@app.post("/summarize")
async def summarize(request: TextRequest):
    try:
        return {"result": summarize_text(request.text)}
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc))


@app.post("/learn/recommendations")
async def recommendations(request: TextRequest):
    try:
        return {"result": get_learning_recommendations(request.text)}
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc))
