from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .database import add_survey
from .schemas import SurveyResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/survey", response_class=HTMLResponse)
def get_survey(request: Request):
    return templates.TemplateResponse("survey.html", {"request": request})

@app.post("/survey", response_class=HTMLResponse)
async def post_survey(
    age_range: str = Form(...),
    profession: str = Form(...),
    current_work: str = Form(None),
    work_type: str = Form(...),
    motivations: str = Form(...),
    challenges: str = Form(...),
    flexibility: int = Form(...),
    work_preference: str = Form(...),
    desired_features: str = Form(...),
    training_interest: int = Form(...),
    specific_work: str = Form(None),
    additional_features: str = Form(None),
):
    survey_data = {
        "age_range": age_range,
        "profession": profession,
        "current_work": current_work,
        "work_type": work_type,
        "motivations": motivations,
        "challenges": challenges,
        "flexibility": flexibility,
        "work_preference": work_preference,
        "desired_features": desired_features,
        "training_interest": training_interest,
        "specific_work": specific_work,
        "additional_features": additional_features,
    }
    new_survey = await add_survey(survey_data)
    return templates.TemplateResponse("thank_you.html", {"request": Request})

@app.get("/thank_you", response_class=HTMLResponse)
def thank_you(request: Request):
    return templates.TemplateResponse("thank_you.html", {"request": request})
