
# AI Safety Incident Log API

This project implements a simple RESTful API backend to **log and manage AI safety incidents** using **Flask (Python)** and **MySQL**.  
It is developed as part of a backend intern take-home assignment for an AI safety startup.

---

## 🛠️ Technology Stack

| Layer | Technology |
|:-----|:------------|
| Language | Python 3.10+ |
| Framework | Flask |
| Database | MySQL 8.0 |
| ORM | SQLAlchemy |
| Others | python-dotenv (for environment variables), PyMySQL (DB connector) |

---

# 📥 Installation and Local Setup

Follow these steps carefully to set up and run the project locally:

## 1. Install Python

Make sure you have Python 3.10+ installed.  
Check version:

```bash
python --version
```

If not installed, download from [Python official website](https://www.python.org/downloads/).

---

## 2. Install MySQL

Ensure MySQL Server is installed on your machine.  
If not installed, download from [MySQL Downloads](https://dev.mysql.com/downloads/installer/).

After installation, **create a new database**:

```bash
mysql -u root -p
```
Enter your MySQL password, then:

```sql
CREATE DATABASE incident_log_db;
EXIT;
```

---

## 3. Clone the Project

```bash
git clone https://github.com/rouymen/AI-Safety-Incident-Log-API.git
cd AI-Safety-Incident-Log-API
```

---

## 4. Set Up Virtual Environment

(Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)
```

---

## 5. Install Python Dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt` includes:
- Flask
- Flask-SQLAlchemy
- PyMySQL
- python-dotenv

---

## 6. Configure Environment Variables

Create a `.env` file in the project root with the following content:

```env
DATABASE_URL=mysql+pymysql://<username>:<password>@localhost:3306/incident_log_db
```

Example:

```env
DATABASE_URL=mysql+pymysql://root:password123@localhost:3306/incident_log_db
```

---

## 7. Run the Flask Application

```bash
python app.py
```

- The app will start on `http://127.0.0.1:5000/`
- Tables will be created automatically at the first request.

---

# 🧱 Database Schema (MySQL)

Table: `incidents`

| Column        | Type         | Details                       |
|:--------------|:-------------|:-------------------------------|
| id            | INT          | Auto Increment, Primary Key    |
| title         | VARCHAR(255) | Short summary of incident      |
| description   | TEXT         | Detailed description           |
| severity      | VARCHAR(20)  | "Low", "Medium", or "High"      |
| reported_at   | TIMESTAMP    | Default to CURRENT_TIMESTAMP   |


---

# 📬 API Endpoints

All endpoints accept and return `application/json` format.

---

## 1. GET `/incidents`

Retrieve all incidents.

```bash
curl http://127.0.0.1:5000/incidents
```

---

## 2. POST `/incidents`

Create a new incident.

```bash
curl -X POST http://127.0.0.1:5000/incidents \
-H "Content-Type: application/json" \
-d '{"title":"AI Hallucination","description":"Model gave wrong facts.","severity":"Medium"}'
```

---

## 3. GET `/incidents/<id>`

Retrieve a specific incident by ID.

Example:
```bash
curl http://127.0.0.1:5000/incidents/1
```

---

## 4. DELETE `/incidents/<id>`

Delete an incident by ID.

Example:
```bash
curl -X DELETE http://127.0.0.1:5000/incidents/1
```

---

