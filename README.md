# AI Job Application Tracker

A REST API to track and analyze job applications using FastAPI and AI-powered insights.

## Features
- Log job applications (company, role, date, status)
- View all applications
- Update application status (applied → interview → rejected → offer)
- Delete applications
- AI-powered analysis of your job search patterns and habits

## Stack
- **Backend:** FastAPI, Python
- **Database:** SQLite, SQLAlchemy
- **AI:** Google Gemini API

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/application` | Add a new application |
| GET | `/applications` | Get all applications |
| PUT | `/update_status/{id}` | Update application status |
| DELETE | `/delete_application/{id}` | Delete an application |
| POST | `/applications/analyze` | Get AI analysis of your job search |

## Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add a `.env` file with your `GEMINI_API_KEY`
4. Run: `python Main.py`
