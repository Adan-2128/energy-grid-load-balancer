<p align="center">
  <a align="center" href="#"> <i>Energy Grid Load Balancer</i></a>
  <br><br>
  <h1>⚡ EcoGrid AI</h1>
  <h3>Smart Energy Grid Load Balancer & Predictive Optimizer • Developed with IBM Watson AI</h3>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI"/>
  <img src="https://img.shields.io/badge/Powered%20by-IBM%20Watson-052FAD?style=for-the-badge&logo=ibm&logoColor=white" alt="IBM Watson"/>
  <img src="https://img.shields.io/badge/VectorDB-ChromaDB-000000?style=for-the-badge&logo=databricks&logoColor=white" alt="ChromaDB"/>
</p>

<br>

<p align="center">
  <strong>Say goodbye to unpredictable power surges and unexplained energy spikes forever!</strong><br>
  <em>"Will the power grid overload in the next two hours?" → automated forecasting has your back.</em>
</p>

<br>

## 🌟 What EcoGrid AI Actually Does

| Feature | Description | Why you'll love it |
|:---|:---|:---|
| 📊 **Historical Benchmark** | Visualizes previous energy usage metrics to identify trends and abnormal spikes | Comprehensive grid health at a single glance |
| 🔮 **2-Hour Predictive Engine** | Uses machine learning to forecast multi-variable consumption trends 2 hours ahead | Catch grid overloads before they actually happen |
| 📉 **Load Balancing Graph** | Generates real-time demand vs. capacity graphs for intelligent power distribution | Prevents blackouts and optimizes resource allocation |
| 💬 **GridExpert Chatbot** | Ask energy optimization questions — answers driven by an isolated RAG pipeline | Instant explanations explaining *why* energy is spiked |
| 💡 **Actionable Insights** | Generates clear, AI-driven mitigation steps on *how* to prevent unnecessary energy waste | Directly aligns with SDG 7 (Affordable & Clean Energy) |
| 💾 **Ephemeral Session Logs** | Temporarily caches active readings dynamically for trend analysis without creepy history tracking | Secure, reliable, and privacy-focused |

<br>

## 🚀 Quick Start (Local Development)

```bash
# 1. Clone the repository
git clone [https://github.com/your-username/ecogrid-ai.git](https://github.com/your-username/ecogrid-ai.git)
cd ecogrid-ai

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate          # ← Windows users: venv\Scripts\activate

# 3. Install core dependencies
pip install -r requirements.txt

# 4. Set up your environment variables
cp .env.example .env

# 5. Edit your .env file and add your official credentials:
# WATSONX_URL=[https://us-south.ml.cloud.ibm.com](https://us-south.ml.cloud.ibm.com)
# WATSONX_APIKEY=your-ibm-watsonx-api-key
# WATSONX_PROJECT_ID=your-ibm-cloud-project-id

# 6. Ensure your static asset folders exist
mkdir -p static templates

# 7. Boot up the local ASGI server 🎉
python app.py
