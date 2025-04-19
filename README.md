# Generative Voice Assistant

A voice‑enabled assistant for the SFEDU MMCS department, combining speech recognition, retrieval‑augmented generation (
RAG) over department data, and speech synthesis. It exposes a FastAPI backend to handle transcription, query processing,
and audio response.

## Aim of this Work

The SFEDU MMCS Assistant project aims to provide an interactive, voice‑driven interface to departmental information (
courses, achievements, departments, etc.) by:

- **Ingesting** markdown‑based MMCS data into a vector store
- **Recognizing** user queries via speech
- **Retrieving** relevant context using RAG
- **Generating** and synthesizing spoken responses in real time

## Usage

### Prerequisites

- **Python 3.12**
- **PortAudio** (for audio I/O)
- **Git**
- **Docker & Docker Compose** (optional)

### Local Setup

1. **Clone** the repository
   ```bash
   git clone https://github.com/kalyuzhin/sfedu-mmcs-assistant.git
   cd sfedu-mmcs-assistant
   ```
2. **Environment**
   ```bash
   cp .env-example .env
   # Edit `.env` with your API tokens, endpoints, and other settings
   ```
3. **Dependencies**
   ```bash
   pip3.12 install -r requirements.txt
   ```
4. **Run** the server
   ```bash
   python main.py
   ```
   The API will be available at `http://<HOST>:<PORT>/api/v1`

### Docker Setup

Alternatively, build and run using Docker Compose:

```bash
docker-compose up --build
```

- Service name: `voice-assistant-mmcs-api`
- Exposes `${PORT:-8080}`

## Project Structure

```
sfedu-mmcs-assistant/
├── data/                           # Department data (markdown and raw text)
│   ├── adm_achievements.md         # Administrative achievements
│   ├── adm_department.md           # Administrative department info
│   ├── all_data.txt                # Consolidated raw data
│   ├── departments.md              # Departments overview
│   └── mmcs.md                     # MMCS‑specific data
├── shared/                         # Core libraries & modules
│   ├── api/                        # API clients & services
│   │   ├── client.py               # HTTP client setup
│   │   ├── intent_service.py       # Intent classification
│   │   └── response_service.py     # RAG response assembly
│   ├── app.py                      # Application factory (Speech + Services)
│   ├── backend/                    # FastAPI backend
│   │   └── app/
│   │       ├── main.py             # FastAPI instantiation
│   │       └── api/
│   │           ├── main.py         # API router setup
│   │           └── routes/rag.py   # `/rag` endpoints (transcribe, query, synthesize)
│   ├── core/
│   │   └── config.py               # Pydantic settings loader
│   ├── db/
│   │   └── milvus.py               # Vector store interface for Milvus
│   ├── parsers/                    # Data parsers (if any)
│   └── speech/                     # Speech I/O modules
│       ├── speech_recognizer.py    # Speech‑to‑text
│       └── speech_synthesizer.py   # Text‑to‑speech
├── .dockerignore                   # Docker ignore rules
├── .env-example                    # Example environment variables
├── .gitignore                      # Git ignore rules
├── Dockerfile                      # Docker image instructions
├── docker-compose.yml              # Multi‑container orchestration
├── main.py                         # Entry point (runs uvicorn)
├── requirements.txt                # Python dependencies
└── README.md                       
```
