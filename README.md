# Healthcare Backend – Django Assignment

## 📌 Project Overview

This project is a **Healthcare Backend System** built with **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**.
It allows users to register, log in, and manage **patients, doctors, and their mappings** securely using **JWT authentication**.

---

## 🚀 Features

* **User Authentication**

  * Register new users
  * Login with JWT authentication (using `djangorestframework-simplejwt`)

* **Patient Management APIs**

  * Create, view, update, and delete patients
  * Authenticated users can only manage their own patients

* **Doctor Management APIs**

  * Create, view, update, and delete doctor records

* **Patient–Doctor Mapping APIs**

  * Assign doctors to patients
  * Retrieve mappings of patients and doctors
  * Remove mappings

* **Security**

  * JWT-based authentication
  * Validation and error handling
  * Sensitive data managed using environment variables

---

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** PostgreSQL
* **Authentication:** JWT (`djangorestframework-simplejwt`)
* **Tools:** Postman (for API testing), Python `venv` or `pipenv`

---

## 📂 Project Structure

```
healthcare-backend-django-/
│── config/              # Django project settings
│── api/                 # Main app with models, serializers, views, urls
│── manage.py            # Django management script
│── requirements.txt     # Dependencies
│── .env.example         # Example environment variables
│── README.md            # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/sri18-cmd/healthcare-backend-django-.git
cd healthcare-backend-django-
```

### 2️⃣ Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file in the root directory with the following:

```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_NAME=healthcare_db
DATABASE_USER=postgres
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### 5️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Start the server

```bash
python manage.py runserver
```

---

## 📡 API Endpoints

### Authentication

* `POST /api/auth/register/` – Register new user
* `POST /api/auth/login/` – Login and get JWT token

### Patients

* `POST /api/patients/` – Add patient
* `GET /api/patients/` – List all patients
* `GET /api/patients/<id>/` – Get patient details
* `PUT /api/patients/<id>/` – Update patient
* `DELETE /api/patients/<id>/` – Delete patient

### Doctors

* `POST /api/doctors/` – Add doctor
* `GET /api/doctors/` – List all doctors
* `GET /api/doctors/<id>/` – Get doctor details
* `PUT /api/doctors/<id>/` – Update doctor
* `DELETE /api/doctors/<id>/` – Delete doctor

### Patient–Doctor Mapping

* `POST /api/mappings/` – Assign doctor to patient
* `GET /api/mappings/` – List all mappings
* `GET /api/mappings/<patient_id>/` – Get doctors of a patient
* `DELETE /api/mappings/<id>/` – Remove mapping

---

## 🧪 Testing

* Use **Postman** or any API client to test endpoints
* Ensure JWT token is included in `Authorization: Bearer <token>` header for protected APIs

---
