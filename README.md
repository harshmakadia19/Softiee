# Softiee OROS — Online Restaurant Ordering System

Softiee OROS is a robust, modular API built to bridge the gap between customer convenience and restaurant operational efficiency. Developed with a **"Guest-First"** philosophy, the system allows users to browse menus and place orders without account registration, while providing staff with advanced analytics for inventory management and revenue tracking.

---

## 🎥 Final Presentation & Demo

The final presentation includes a brief introduction, a technical deep-dive, and a live demonstration of the system's core features.

- **Video Folder:** The raw video file can also be found in the `/presentation` directory of this repository.
- **User Manual:** A complete guide for end-users on how to navigate and use the system can be found in the `/presentation` directory.
- **Technical Document:** The full technical specification and system design documentation can also be found in the `/presentation` directory.

---

## 🚀 Key Features

### For Customers
- **No-Account Ordering:** Seamlessly place orders as a guest.
- **Fuzzy Search:** Filter menu items by category (e.g., "Vegetarian," "Spicy") using partial string matching.
- **Real-Time Tracking:** Every order generates a unique 12-character tracking number for status lookups.
- **Review System:** Rate and review specific dishes to share experiences with other diners.

### For Restaurant Staff
- **Low-Stock Alerts:** Automated monitoring of ingredients with proactive alerts for items falling below 10 units.
- **Revenue Analytics:** Calculate daily revenue totals based on completed transactions.
- **Popularity Tracking:** Identify "Unpopular Dishes" using SQL joins and average rating thresholds (< 3.0 stars).
- **Full CRUD:** Complete Create, Read, Update, and Delete functionality across all 11 database tables.

---

## 🛠️ Technical Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Language | Python 3.11+ |
| Database | MySQL |
| ORM | SQLAlchemy |
| Validation | Pydantic |
| Testing | Pytest |

---

## ⚙️ Installation & Setup

### 1. Initialize Virtual Environment

It is recommended to use a virtual environment to isolate dependencies.

```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
```

### 2. Install Dependencies

```bash
pip install fastapi
pip install "uvicorn[standard]" 
pip install sqlalchemy 
pip install pymysql 
pip install pytest 
pip install pytest-mock 
pip install httpx 
pip install cryptography
```

### 3. Database Configuration

Update the database connection in `api/dependencies/config.py` with your local MySQL credentials:

```python
class conf:
    db_host = "localhost"
    db_name = "sandwich_maker_api"
    db_port = 3306
    db_user = "root"
    db_password = "rootroot"
    app_host = "localhost"
    app_port = 8000
```

### 4. Running the Application

```bash
uvicorn api.main:app --reload
```

Once the server is running, access the interactive API documentation at:
**http://127.0.0.1:8000/docs**

---

## 🧪 Automated Testing

The project includes a comprehensive suite of unit and integration tests covering tracking logic, revenue calculation, and CRUD operations.

To run the tests, execute the following command from the root directory:

```bash
pytest
```

---

## 📂 Architecture Overview

The project follows a **Modular Layered Architecture**:

```
api/
├── models/        # SQL table definitions and relationships
├── routers/       # API route definitions and request handling
├── controllers/   # Core business logic and database queries
├── schemas/       # Pydantic models for data validation
└── dependencies/  # Database session management and global configurations
```

---

## 👥 Team Members — Team Softiee

| Name | Role |
|---|---|
| Harsh Patel | Product Manager |
| Shreem Patel | Scrum Master |
| Tanishka Patel | Lead Developer |

**Course:** ITSC-3155 Software Engineering

**Date:** May 2026