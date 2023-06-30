# Flask and React Tutorial

This project provides a step-by-step tutorial on connecting Flask (a Python web framework) with React (a JavaScript library for building user interfaces). The tutorial aims to help you understand the basics of integrating a Flask backend with a React frontend.

## Prerequisites

Before starting with this tutorial, ensure that you have the following installed:

- Python (version 3.6 or higher)
- Node.js and npm (Node Package Manager)

## Getting Started

1. Clone the Repository

git clone https://github.com/vinicius-mattoso/REACT-FLASK_LEARNING.git
cd REACT-FLASK_LEARNING

2. Backend Setup (Flask)

- Create and activate a virtual environment (recommended):

  ```
  python3 -m venv env
  source env/bin/activate  # For Unix/Linux
  .\env\Scripts\activate  # For Windows
  ```

- Install the required Python dependencies:

  ```
  pip install -r requirements.txt
  ```

- Start the Flask server:

  ```
  flask run
  ```

3. Frontend Setup (React)

cd ../frontend


- Install the required Node.js dependencies:

  ```
  npm install
  ```

- Start the React development server:

  ```
  npm start
  ```

4. Open the App

Open your web browser and visit `http://localhost:3000` to see the Flask-React app in action.

## Tutorial Sections

1. Section 1: Setting up Flask Backend
- Description: Setting up a basic Flask backend server to serve API endpoints.
- Code Changes: Backend code files (e.g., `app.py`, `requirements.txt`).

2. Section 2: Creating React Frontend
- Description: Creating a React frontend with basic components and UI elements.
- Code Changes: Frontend code files (e.g., `App.js`, `index.js`).

3. Section 3: Fetching Data from Flask API
- Description: Making API requests from React frontend to the Flask backend and displaying the data.
- Code Changes: Frontend code files (e.g., `App.js`).

4. Section 4: Sending Data to Flask API
- Description: Implementing form submission in React and sending data to the Flask backend.
- Code Changes: Frontend code files (e.g., `App.js`), backend code files (e.g., `app.py`).

5. Section 5: Advanced Topics (optional)
- Description: Exploring more advanced topics like authentication, database integration, etc.
- Code Changes: Varies based on the topics covered.

## Contributions

Contributions to improve this tutorial are welcome! If you find any issues or have suggestions, feel free to submit a pull request or create an issue.


