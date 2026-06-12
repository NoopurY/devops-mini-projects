# 🚀 Docker Compose Fullstack App

A complete fullstack application using Docker Compose with a frontend, backend, and database.

## 📋 Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     Docker Network                      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐      ┌──────────────┐                │
│  │              │      │              │                │
│  │  Frontend    │      │  Backend     │                │
│  │  (Nginx)     │──────│  (Flask)     │                │
│  │  Port 80     │      │  Port 5000   │                │
│  │              │      │              │                │
│  └──────────────┘      └──────────────┘                │
│        ↓                       ↓                        │
│   Port 8081              ┌──────────────┐              │
│   (exposed)              │              │              │
│                          │  Database    │              │
│                          │  (PostgreSQL)│              │
│                          │  Port 5432   │              │
│                          │              │              │
│                          └──────────────┘              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## 🗂️ Project Structure

```
mini-project-05-docker-compose-fullstack-app/
├── docker-compose.yml       # Orchestrates all services
├── README.md                # This file
├── backend/
│   ├── Dockerfile           # Python 3.9 image for Flask
│   ├── app.py               # Flask API with /api endpoint
│   └── requirements.txt      # Python dependencies (flask, psycopg2)
├── frontend/
│   ├── index.html           # HTML UI with "Call Backend" button
│   └── nginx.conf           # Nginx configuration for routing
```

## 🛠️ Services

### Frontend (Nginx)
- **Port**: 8081 (externally exposed)
- **Internal Port**: 80
- **Files**: `frontend/index.html`, `frontend/nginx.conf`
- **Routes**:
  - `/` → Serves `index.html`
  - `/api` → Proxies to backend at `http://backend:5000/api`

### Backend (Flask)
- **Port**: 4000 (externally exposed → 5000 internal)
- **Internal Port**: 5000
- **Files**: `backend/app.py`, `backend/requirements.txt`, `backend/Dockerfile`
- **Endpoints**:
  - `GET /api` → Returns JSON with database info, message, and timestamp
  - `GET /` → Returns 404 (not defined)

### Database (PostgreSQL)
- **Port**: 5432 (internal only, not exposed)
- **Credentials**:
  - User: `postgres`
  - Password: `postgres`
  - Database: `testdb`
- **Data Persistence**: Volume `pgdata` persists data across container restarts

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose installed
- Port 8081 available on your machine

### Run the Application

```bash
docker-compose up --build
```

This will:
1. Build the backend image
2. Start all three services (frontend, backend, database)
3. Connect services through Docker network

### Access the Application

**Frontend UI:**
```
http://localhost:8081
```
- Click "Call Backend" button to test the connection
- Response shows database version, message, and timestamp

**Backend API (Direct):**
```
http://localhost:4000/api
```
- Returns JSON response directly from Flask

## 📝 API Response Example

```json
{
  "database": "PostgreSQL 13.23 (Debian 13.23-1.pgdg13+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit",
  "message": "Hello from Flask Backend 🚀",
  "time": "2026-06-12T17:39:03.863824"
}
```

## 🛑 Stop the Application

```bash
docker-compose down
```

This stops and removes all containers. Database volume `pgdata` is preserved.

## 🗑️ Clean Up (Remove Everything)

```bash
docker-compose down -v
```

This removes containers AND volumes (database data will be lost).

## 📊 View Logs

View all services:
```bash
docker-compose logs -f
```

View specific service:
```bash
docker-compose logs backend
```

## 🔧 How It Works

1. **User visits** `http://localhost:8081` → Nginx serves `index.html`
2. **User clicks button** → JavaScript calls `fetch('/api')`
3. **Nginx proxy** routes `/api` → `http://backend:5000/api`
4. **Flask backend** receives request, queries PostgreSQL database
5. **Response** returns database version + message + timestamp
6. **Frontend** displays JSON response in the browser

## 📦 Files Explained

| File | Purpose |
|------|---------|
| `docker-compose.yml` | Defines all services and their configuration |
| `backend/Dockerfile` | Creates Python image with Flask dependencies |
| `backend/app.py` | Flask API with database connection |
| `backend/requirements.txt` | Python packages: Flask, psycopg2 |
| `frontend/index.html` | HTML page with button and JavaScript fetch |
| `frontend/nginx.conf` | Nginx server config with API proxy |

## ✅ What's Working

- ✅ Frontend UI loads at port 8081
- ✅ Backend Flask API responds on port 5000
- ✅ PostgreSQL database stores and serves data
- ✅ Nginx proxies requests from frontend to backend
- ✅ Docker network connects all services
- ✅ Database persistence with volumes

## 🐛 Troubleshooting

**Port already in use?**
```bash
docker-compose down  # Free up ports
```

**Can't connect to backend?**
```bash
docker-compose logs backend  # Check backend logs
```

**Database not initialized?**
```bash
docker-compose down -v  # Remove volume and restart
docker-compose up --build
```

---

**Project**: DevOps Mini Project #5 - Docker Compose Fullstack Application
