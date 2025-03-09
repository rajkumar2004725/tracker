Sustainability Tracker API

Overview

The Sustainability Tracker API allows users to track their sustainability actions, assign points to each action, and manage them through a RESTful API. This API provides endpoints for creating, retrieving, updating, and deleting sustainability actions.

Getting Started
  To start using the Sustainability Tracker API, follow these steps:

Prerequisites
Ensure you have the following installed:
  Python 3.x
  Django 4.x
  Django REST Framework
  SQLite (or configure your preferred database)

Backend structure

    sustainability-tracker/  # Root folder
    │── backend/             # Django backend
    │   ├── actions/         # Django app for sustainability actions
    │   │   ├── migrations/
    │   │   ├── __init__.py
    │   │   ├── models.py
    │   │   ├── serializers.py
    │   │   ├── views.py
    │   │   ├── urls.py
    │   │   ├── tests.py
    │   ├── backend/         # Django project settings
    │   │   ├── __init__.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   ├── wsgi.py
    │   │   ├── asgi.py
    │   ├── manage.py        # Django management script
    │   ├── db.sqlite3       # Database (if using SQLite)

Installation

1.Clone the repository:
    git clone https://github.com/your-repo/sustainability-tracker-api.git
    cd sustainability-tracker-api

2.Create and activate a virtual environment:
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate

3.Run database migrations:
  python manage.py migrate

4.Start the development server:
  python manage.py runserver

API Endpoints
Sustainability Actions

List All Actions
Endpoint: GET /api/actions/
    Response:
    
    [
      {
        "id": 1,
        "action": "Planted a tree",
        "date": "2025-01-07",
        "points": 30
      }
    ]

Create a New Action
Endpoint: POST /api/actions/

    Request Body:
    
    {
      "action": "Used public transport",
      "date": "2025-03-08",
      "points": 20
    }
    
    Response:
    
    {
      "id": 2,
      "action": "Used public transport",
      "date": "2025-03-08",
      "points": 20
    }

Retrieve a Specific Action
Endpoint: GET /api/actions/{id}/

Update an Action
Endpoint: PUT /api/actions/{id}/

    Request Body:
    
    {
      "action": "Recycled plastic",
      "date": "2025-03-09",
      "points": 15
    }

Delete an Action
Endpoint: DELETE /api/actions/{id}/


Error Handling
HTTP Status Code   ||    Meaning

400                  Bad request (e.g., missing fields)

403                  Forbidden (no permission)

404                  Not found (invalid endpoint)

429                  Too many requests (rate limit exceeded)

500                  Internal server error










Sustainability Tracker Frontend 🌱


This is the frontend for the Sustainability Tracker project, built using React.js. The application allows users to track sustainability actions, assign points, and manage actions using a clean and user-friendly interface.

🚀 Features

✅ Fetch and display sustainability actions from the backend API.
✅ Add new sustainability actions via a form.
✅ Edit and update existing actions.
✅ Delete sustainability actions.
✅ Styled interface with CSS and Toast notifications for feedback.

🛠️ Tech Stack

React.js (Frontend framework)
Axios (For API requests)
React Toastify (For notifications)
CSS (For styling)


📦 Installation & Setup


1️⃣ Clone the Repository
    git clone https://github.com/rajkumar2004725/Sustainability-Tracker.git
cd Sustainability-Tracker/frontend
2️⃣ Install Dependencies
    npm install
3️⃣ Start the React App
    npm start
This will start the development server at http://localhost:3000/.

⚡ API Configuration
This frontend communicates with the Django backend. Ensure your backend is running before testing the frontend.

Backend API URL:
Modify the API_URL in src/services/api.js if needed:

javascript
    const API_URL = "http://127.0.0.1:8000/api/actions/";

📌 Project Structure

    sustainability-tracker/ 
    │── frontend/   
    │── src/
    │   ├── components/      # React components
    │   │   ├── ActionList.js
    │   │   ├── ActionForm.js
    │   ├── services/        # API service (Axios requests)
    │   │   ├── api.js
    │   ├── App.js           # Main app component
    │   ├── index.js         # Entry point
    │── public/              # Static files
    │── package.json         # Dependencies
    │── README.md            # Project documentation


🎯 Usage

    Add a sustainability action → Fill in the form and click "Add Action".
    Edit an action → Click "Edit", modify details, and save changes.
    Delete an action → Click "Delete" to remove an action.

🎨 Styling & UI

    Uses CSS for styling (App.css).
    Responsive design for better user experience.
    Toast notifications to provide user feedback.


🐞 Troubleshooting


🔴 If API requests fail (CORS issue)
Ensure CORS is enabled in backend/settings.py:

        INSTALLED_APPS = [
            'corsheaders',
            'rest_framework',
            'actions',
        ]
        MIDDLEWARE = [
            'corsheaders.middleware.CorsMiddleware',
        ]
        CORS_ALLOW_ALL_ORIGINS = True  # Allow frontend requests

🔴 If dependencies are missing
Run:
    npm install

🔴 If frontend does not start
Try:
    rm -rf node_modules package-lock.json
    npm install
    npm start
