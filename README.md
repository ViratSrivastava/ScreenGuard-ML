# ScreenGuard-ML
Welcome to the ScreenGuard Kids ML Backend repository! This project aims to reduce screen usage among children by leveraging machine learning models to monitor and manage screen time effectively.

*****Note: Before Initial release Verions reasme woll be updated to add relevent information obver the period of time***
## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Introduction

ScreenGuard Kids is an application designed to help parents manage their children's screen time. This repository hosts the backend services, including machine learning models that monitor screen usage and provide recommendations to reduce screen time.

## Features

- Monitor screen usage in real-time.
- Predictive models to anticipate excessive screen time.
- API endpoints for integrating with front-end applications.
- Parental controls to set screen time limits.
- Notifications and alerts for excessive usage.

## Technologies

- **Programming Language:** Python
- **Framework:** Flask/Django (choose one based on your implementation)
- **Machine Learning:** TensorFlow, PyTorch
- **Database:** PostgreSQL, SQLite
- **APIs:** RESTful APIs
- **Others:** Docker, Kubernetes for containerization and orchestration

## Installation

### Prerequisites

- Python 3.8+
- pip (Python package installer)
- Docker (optional, for containerization)
- PostgreSQL (or your choice of database)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AntiProton-Labs/ScreenGuard-ML.git
   cd ScreenGuard-ML
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv app-backend-venv
   .\app-backend-venv\Scripts\Activate.ps1
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   Update the `DATABASE_URL` in the `.env` file with your database credentials.

   ```bash
   python manage.py migrate  # For Django
   # or
   flask db upgrade  # For Flask
   ```

5. **Run the application:**

   ```bash
   python manage.py runserver  # For Django
   # or
   flask run  # For Flask
   ```

## Usage

1. **Start the server:**

   ```bash
   python manage.py runserver  # For Django
   # or
   flask run  # For Flask
   ```

2. **Access the API documentation:**

   Navigate to `http://localhost:8000/api/docs` (Django) or `http://localhost:5000/api/docs` (Flask) for API documentation.

## API Endpoints

### Authentication

- **POST /api/auth/login:** User login
- **POST /api/auth/register:** User registration

### Screen Time Monitoring

- **GET /api/screen-time:** Get screen time data
- **POST /api/screen-time:** Log screen time data

### Parental Controls

- **POST /api/parental-controls/limit:** Set screen time limit
- **GET /api/parental-controls/limit:** Get current screen time limit

### Notifications

- **GET /api/notifications:** Get notifications
- **POST /api/notifications:** Send notification

## Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) to get started.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to open issues or submit pull requests to help improve the project.

---
