# 🛡️ Adaptive LLM Safety Evaluation Platform

A production-ready AI security platform that evaluates Large Language Models (LLMs) against prompt injection and adversarial attacks. The platform automatically generates attack variants, evaluates model responses, assigns risk scores, stores experiment history, and provides a real-time analytics dashboard.

---

## ✨ Features

- 🔥 Prompt Injection Testing
- 🛡️ LLM Safety Evaluation
- 🤖 Ollama + Qwen2.5 Integration
- 📊 Risk Scoring Engine
- 📜 Experiment History
- 🔍 Search & Filtering
- 📈 Interactive Analytics Dashboard
- 📥 CSV Export
- 📥 JSON Export
- 🐳 Docker Support
- ⚡ FastAPI REST APIs
- 💾 SQLite Database

---

## 🏗️ System Architecture

> Architecture diagram will be added soon.

```text
                User
                  │
                  ▼
         Streamlit Dashboard
                  │
                  ▼
             FastAPI Backend
                  │
      ┌───────────┼────────────┐
      ▼           ▼            ▼
 SQLite DB    Ollama API   Safety Engine
                  │
                  ▼
             Qwen2.5 Model
```

---

## 📂 Project Structure

```text
adaptive-llm-safety-platform/

├── app/
│   ├── agents/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── evaluator/
│   ├── services/
│   └── main.py
│
├── dashboard/
│   └── app.py
│
├── datasets/
│
├── docs/
│
├── screenshots/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 🚀 Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## AI

- Ollama
- Qwen2.5:7B

## Dashboard

- Streamlit
- Plotly

## DevOps

- Docker
- Docker Compose

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/AryanThakur30/adaptive-llm-safety-platform.git

cd adaptive-llm-safety-platform
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run FastAPI

```bash
uvicorn app.main:app --reload
```

API Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Docker

### Build

```bash
docker compose build
```

### Run

```bash
docker compose up
```

---

# 📡 REST API

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/generate` | Run safety evaluation |
| GET | `/history` | List experiments |
| GET | `/history/{id}` | Get experiment |
| DELETE | `/history/{id}` | Delete experiment |
| GET | `/stats` | Dashboard statistics |
| GET | `/history/export/csv` | Export CSV |
| GET | `/history/export/json` | Export JSON |

---

# 📊 Dashboard

The Streamlit dashboard provides:

- Live Statistics
- Experiment History
- Search
- Safety Distribution
- Strategy Distribution
- Risk Score Trend
- Auto Refresh
- CSV Export
- JSON Export

---

# 📸 Screenshots

Coming Soon

- Dashboard
- Charts
- Swagger UI
- Docker
- Architecture Diagram

---

# 📈 Future Improvements

- JWT Authentication
- PostgreSQL Support
- Redis Cache
- Kubernetes Deployment
- CI/CD Pipeline
- Prometheus Integration
- Grafana Monitoring
- Multi-Model Evaluation
- User Management
- Role-Based Access Control

---

# 👨‍💻 Author

**Aryan Thakur**

Computer Science Student  
Delhi University

GitHub

https://github.com/AryanThakur30

---

# 📄 License

This project is licensed under the MIT License.

---

## ⭐ If you found this project useful, consider giving it a star!
