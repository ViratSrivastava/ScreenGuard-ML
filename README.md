# ScreenGuard-ML

Welcome to the ScreenGuard Kids ML Backend repository! This project aims to reduce screen usage among children by leveraging machine learning models to monitor and manage screen time effectively.

*****Note: Before Initial release Version, readme will be updated to add relevent information over the period of time***

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
- **Machine Learning:** TensorFlow, PyTorch
- **APIs:** RESTful APIs

### Steps for running

1. **Clone the repository:**

   ```powershell
   git clone https://github.com/AntiProton-Labs/ScreenGuard-ML.git
   cd ScreenGuard-ML
   ```

2. **Create a virtual environment:**

   ```powershell
   python -m venv app-backend-venv
   app-backend-venv\Scripts\Activate
   ```

3. **Install the dependencies:**

   ```powershell
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   Update the `DATABASE_URL` in the `.env` file with your database credentials.

   ```powershell
   python manage.py migrate  # For Django
   # or
   flask db upgrade  # For Flask
   ```

5. **Run the application:**

   ```powershell
   python manage.py runserver  # For Django
   # or
   flask run  # For Flask
   ```

## Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) to get started.
