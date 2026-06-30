# 🔐 Secure Authentication System

A secure authentication system built with **Flask**, **PostgreSQL**, **JWT**, and **bcrypt**. The project provides user registration, login, JWT-based API authentication, and a browser-based interface for authentication and user management.

---

## 📌 Features

- User Registration
- User Login
- Password Hashing using bcrypt
- JWT Token Generation
- Protected API Endpoints
- User Profile
- Session-based Web Login
- Logout
- Email Validation
- Strong Password Validation
- Duplicate Username Check
- Duplicate Email Check
- PostgreSQL Database
- Database Migrations using Flask-Migrate
- Responsive Bootstrap UI

---

## 🛠 Technologies Used

- Python 3.11
- Flask
- PostgreSQL
- SQLAlchemy
- Flask-Migrate
- Flask-Bcrypt
- PyJWT
- Bootstrap 5
- HTML5
- CSS3

---

## 📁 Project Structure

```
secure_auth/
│
├── app/
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── profile.html
│   │
│   ├── __init__.py
│   ├── auth.py
│   ├── config.py
│   ├── decorators.py
│   ├── models.py
│   ├── routes.py
│   └── validators.py
│
├── migrations/
├── venv/
├── .env
├── manage.py
├── run.py
├── requirements.txt
└── README.md
```

---

## ⚙ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/secure-authentication-system.git
```

---

### 2. Navigate to the project

```bash
cd secure-authentication-system
```

---

### 3. Create a virtual environment

```bash
python -m venv venv
```

---

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 6. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://postgres:password@localhost:5432/secure_auth
JWT_EXPIRATION=30
```

---

### 7. Run Database Migrations

```bash
flask --app manage db upgrade
```

---

### 8. Run the application

```bash
python run.py
```

---

## 🌐 Web Pages

| Page | URL |
|------|------|
| Home | `/` |
| Register | `/register-page` |
| Login | `/login-page` |
| Dashboard | `/dashboard` |

---

## 🔌 API Endpoints

### Register User

**POST**

```
/register
```

Request

```json
{
    "username":"john",
    "email":"john@example.com",
    "password":"Password@123"
}
```

---

### Login

**POST**

```
/login
```

Request

```json
{
    "email":"john@example.com",
    "password":"Password@123"
}
```

Response

```json
{
    "message":"Login successful",
    "token":"JWT_TOKEN"
}
```

---

### Protected Profile

**GET**

```
/profile
```

Header

```
Authorization: Bearer JWT_TOKEN
```

---

## 🔒 Security Features

- bcrypt Password Hashing
- JWT Authentication
- Protected API Routes
- Strong Password Validation
- Email Validation
- Duplicate User Detection
- Session Management

---

## 📷 Screenshots

Add screenshots here after completing the project.

Example:

```
screenshots/
│
├── home.png
├── register.png
├── login.png
├── dashboard.png
└── api-testing.png
```

---

## 🚀 Future Improvements

- Password Reset
- Email Verification
- Refresh Tokens
- User Roles (Admin/User)
- Docker Support
- Unit Testing
- Account Lockout
- Login History

---

## 📄 License

This project is created for educational purposes.