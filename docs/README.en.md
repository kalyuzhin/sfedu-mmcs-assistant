# Generative Voice Assistant

This project is a course assignment for developing a voice assistant for the MMCS Department at SFEDU. The system
integrates speech recognition, Retrieval‑Augmented Generation (RAG) using departmental data, and speech
synthesis. The backend is built on FastAPI, handling audio requests, generating appropriate responses, and streaming
audio in real time.

## Aim of the Project

The goal of this course assignment is to develop a prototype voice assistant that will:

- **Automate** access to structured information for the MMCS Department at SFEDU through semantic search over uploaded
  documentation (Markdown, txt) stored in a vector database.
- **Implement** a speech‑to‑text module to convert spoken user queries into text.
- **Integrate** Retrieval‑Augmented Generation (RAG) to retrieve and assemble relevant context from academic materials.
- **Provide** speech synthesis for responses, enabling a convenient hands‑free interface to interact with department
  resources.

## Usage

### Requirements

- **Python 3.12**
- **PortAudio** (for audio input/output)
- **Git**
- **Docker & Docker Compose** (optional, for containerized deployment)

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kalyuzhin/sfedu-mmcs-assistant.git
   cd sfedu-mmcs-assistant
   ```
2. **Configure the environment**
   ```bash
   cp backend/.env-example backend/.env
   # Edit backend/.env to add your API keys and other settings.
   ```
3. **Install dependencies**
   ```bash
   pip3.12 install -r backend/requirements.txt
   ```
4. **Start the server**
   ```bash
   cd backend
   python main.py
   ```
   The API will be available at `http://localhost:8080`.

### Running with Docker

Build and launch the service using Docker Compose:

```bash
docker-compose up --build
```

By default, the `voice-assistant-mmcs-api` service will run on port `8080`.

## Project Structure

```
sfedu-mmcs-assistant/
├── backend/                   # Backend
│   ├── app/                   # FastAPI application
│   │   ├── api/               # HTTP routes
│   │   ├── core/              # Configuration
│   │   ├── db/                # Vector database
│   │   ├── services/          # Business logic and integrations
│   │   │   ├── api/           # RAG and intent service clients
│   │   │   └── speech/        # STT/TTS modules
│   │   └── main.py            # Application entry point
│   ├── data/                  # Departmental Markdown and text data
│   ├── .dockerignore          
│   ├── .env-example           
│   ├── Dockerfile             
│   ├── main.py                # Uvicorn launcher
│   └── requirements.txt       # Python dependencies
│
├── shared/                    # Shared utilities and parsers
│   ├── parsers/               # Data parsing utilities
│   ├── scripts.py             # Helper scripts
│   └── requirements.txt       # Shared dependencies
│
├── docs/                      # Documentation
│   ├── README.en.md           # English guide
│   └── README.ru.md           # Russian guide
│
├── .gitignore                 
├── docker-compose.yml         
└── README.md                  
```
