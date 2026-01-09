from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from prediction import predict_energy_usage
from rag import get_rag_explanation
from pymongo import MongoClient

load_dotenv()

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    hour: int
    day_of_week: int
    temperature: float
    humidity: float

@app.post("/api/get_insights")
async def get_insights(data: InputData):
    # Predict energy usage
    features = [data.hour, data.day_of_week, data.temperature, data.humidity]
    predicted_usage = predict_energy_usage(features)

    # <-- CORRECTION 1: Use AI (Granite) for precise, personalized recommendation + explanation
    # Build a detailed prompt so Granite generates both smart recommendation and explanation
    query = f"""Building energy prediction: {predicted_usage:.2f} kWh at hour {data.hour}:00 (day {data.day_of_week}).
Current conditions: Temperature {data.temperature}°C, Humidity {data.humidity}%.
Peak hours are typically 12-18.

Provide:
1. A concise, actionable smart recommendation (specific HVAC adjustment, lights, load shifting, estimated savings).
2. Brief explanation grounded in energy efficiency guidelines.

Be precise, balance comfort and savings, and suggest quantified actions."""

    # Granite generates the full response (recommendation + explanation)
    ai_response = get_rag_explanation(query)

    # Split for display: first part as recommendation, full as explanation
    lines = ai_response.strip().split('\n', 1)
    recommendation = lines[0].strip() if lines else ai_response.strip()
    explanation = ai_response.strip()

    # <-- CORRECTION 2: Removed old simple rule-based recommendation
    # (No more "Reduce HVAC by 20% during peak hours." — now fully AI-driven)

    return {
        "predicted_usage": predicted_usage,
        "recommendation": recommendation,  # Now AI-generated, much more precise
        "explanation": explanation  # Full AI explanation with RAG context
    }
client = MongoClient(os.getenv("MONGO_URI"))
db = client["energy_db"]