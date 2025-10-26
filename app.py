from fastapi import FastAPI,Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os 
from src.logger import logging
from fastapi.middleware.cors import CORSMiddleware
from src.pipeline.predict_pipeline import CropPredictionPipeline

app = FastAPI(title="Crop Recommendation API")

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],  # or specify ["http://localhost:3000"] for React app
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

predictor = CropPredictionPipeline()

templates = Jinja2Templates(directory="templates")
logging.info("templates created")
app.mount("/static",StaticFiles(directory="static"),name="static")
logging.info("static files detect")

# Input schema
class CropData(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

@app.get("/",response_class=HTMLResponse)
async def root_read(request:Request):
  return templates.TemplateResponse("index.html",{"request":request})


logging.info("prediction has started ")
@app.post("/predict")
async def predict_ans(data:CropData):
  input_data = data.model_dump()
  prediction = predictor.predict(input_data)

  return {"prediction_crop": prediction}