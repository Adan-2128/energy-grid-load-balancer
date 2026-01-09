import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["energy_db"]

# Clear old data (optional)
db.energy_guidelines.drop()

# Insert plain text guidelines (no embeddings needed)
guidelines = [
    "High temperatures above 25°C increase HVAC energy usage by up to 10% per degree. Recommend reducing HVAC setpoint during peak hours.",
    "Energy consumption spikes between 12-18 due to higher occupancy and lighting. Suggest dimming lights or shifting non-essential loads.",
    "Humidity over 60% can make HVAC work harder for cooling. Turn on dehumidifier mode if available.",
    "Off-peak hours (after 20:00) have lower electricity rates. Shift energy-intensive tasks like laundry or charging to save costs.",
    "Daylight hours can reduce lighting needs by 30%. Use natural light and turn off unnecessary lights.",
    "Historical data shows average building usage is 10-15 kWh baseline + temperature-driven increases.",
    "For temperatures below 20°C, reduce heating gradually to maintain comfort while saving energy."
]

db.energy_guidelines.insert_many([{"text": text} for text in guidelines])

print("Guidelines inserted successfully! (No embeddings – simple RAG)")