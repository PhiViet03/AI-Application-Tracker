# AI Job Application Tracker

A REST API to track and analyze job applications — built with FastAPI, SQLAlchemy, and Google Gemini AI.

🚀 **Live API:** https://ai-application-tracker-w93i.onrender.com

---

## What it does

Log every job you apply to, track where each application stands, and get AI-powered analysis of your job search patterns — all through a clean REST API.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/application` | Add a new job application |
| GET | `/applications` | Get all applications |
| PUT | `/update_status/{id}` | Update application status |
| DELETE | `/delete_application/{id}` | Delete an application |
| POST | `/applications/analyze` | Get AI analysis of your job search |

### Example request — add an application
```json
POST /application
{
  "Company": "Google",
  "Role": "Backend Engineer",
  "Date_Applied": "2024-04-13",
  "Status": "applied"
}
```

### Example response — AI analysis
```json
POST /applications/analyze
{
  "analysis": "You're applying to senior roles as a fresher.
  Adjust your targeting toward junior and intern positions..."
}
```

### Status options
`applied` → `interview` → `rejected` / `offer`

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | FastAPI, Python |
| Database | SQLite, SQLAlchemy |
| AI | Google Gemini API |
| Container | Docker |
| Deployment | Render |

---

## Run locally

**1. Clone the repo**
```bash
git clone https://github.com/PhiViet03/ai-application-tracker.git
cd ai-application-tracker
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your API key**
```bash
# create a .env file
GEMINI_API_KEY=your_key_here
```

**4. Run**
```bash
python FastAPI.py
```

API is live at `http://localhost:8000`
Interactive docs at `http://localhost:8000/docs`

---

## Run with Docker

```bash
docker build -t job-tracker .
docker run -p 8000:8000 --env-file .env job-tracker
```

---

## Why I built this

I built this project to learn backend development hands-on — covering REST API design, database modeling, Docker containerization, cloud deployment, and AI API integration. It solves a real problem I have as a fresh grad actively job hunting in Vietnam.