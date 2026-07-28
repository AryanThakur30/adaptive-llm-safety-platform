<div align="center">

# 🛡️ Adaptive LLM Safety Evaluation Platform

### Production-Ready Platform for Automated LLM Safety Evaluation

<p align="center">

<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white"/>
<img src="https://img.shields.io/badge/Ollama-Qwen2.5-black?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>

</p>

<p align="center">

<img src="https://img.shields.io/github/stars/AryanThakur30/adaptive-llm-safety-platform?style=flat-square"/>
<img src="https://img.shields.io/github/forks/AryanThakur30/adaptive-llm-safety-platform?style=flat-square"/>
<img src="https://img.shields.io/github/last-commit/AryanThakur30/adaptive-llm-safety-platform?style=flat-square"/>

</p>

</div>

---

# 📖 Overview

Adaptive LLM Safety Evaluation Platform is a production-ready application that automatically evaluates prompts against multiple adversarial attack strategies. It generates risk scores, stores experiment history in PostgreSQL, and provides analytics for analyzing Large Language Model safety.

---

# ✨ Features

- 🚀 Automated Prompt Evaluation
- 🎯 Multiple Prompt Attack Strategies
- 📊 Dynamic Risk Scoring
- 🗄️ PostgreSQL-backed Experiment Storage
- 📜 Searchable Experiment History
- 📂 CSV & JSON Export
- ⚡ FastAPI REST APIs
- 🐳 Dockerized Deployment
- 🧩 Modular Architecture

---

# 🏗️ System Architecture

```text
                        ┌──────────────────────────────┐
                        │        User / Client         │
                        └──────────────┬───────────────┘
                                       │
                                 HTTP Request
                                       │
                                       ▼
                     ┌─────────────────────────────────┐
                     │         FastAPI Backend         │
                     └──────────────┬──────────────────┘
                                    │
         ┌──────────────────────────┼─────────────────────────┐
         ▼                          ▼                         ▼
 ┌────────────────┐        ┌────────────────┐       ┌────────────────┐
 │ Prompt Engine  │        │ Attack Engine  │       │ Risk Scoring   │
 └────────────────┘        └────────────────┘       └────────────────┘
                                    │
                                    ▼
                        ┌────────────────────────┐
                        │   Ollama (Qwen2.5)     │
                        └────────────┬───────────┘
                                     │
                                     ▼
                        ┌────────────────────────┐
                        │     SQLAlchemy ORM     │
                        └────────────┬───────────┘
                                     │
                                     ▼
                        ┌────────────────────────┐
                        │      PostgreSQL        │
                        └────────────────────────┘
```

---

# 📂 Project Structure

```text
Adaptive-LLM-Safety-Platform
│
├── app
│   ├── api
│   ├── core
│   ├── database
│   │   ├── database.py
│   │   ├── crud.py
│   │   └── models.py
│   ├── evaluator
│   ├── services
│   ├── templates
│   ├── static
│   └── main.py
│
├── exports
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# ⚙️ Tech Stack

| Category | Technology |
|----------|------------|
| Backend | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| LLM | Ollama (Qwen2.5) |
| Containerization | Docker |
| Language | Python |

---

# 📊 Project Metrics

| Metric | Value |
|---------|-------|
| REST APIs | 10+ |
| Core Modules | 6+ |
| Database | PostgreSQL |
| Attack Strategies | Multiple |
| ORM | SQLAlchemy |
| Deployment | Docker |

---

# 🚀 Getting Started

```bash
git clone https://github.com/AryanThakur30/adaptive-llm-safety-platform.git

cd adaptive-llm-safety-platform

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

# 🔗 Project Links

### GitHub Repository

**https://github.com/AryanThakur30/adaptive-llm-safety-platform**

### LinkedIn

**https://www.linkedin.com/in/aryan-thakur-78530b250/**

---

# 👨‍💻 Author

**Aryan Thakur**

Computer Science Graduate | AI & Backend Engineering Enthusiast

⭐ If you found this project useful, consider giving it a star.
