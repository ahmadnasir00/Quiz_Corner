# Flask Quiz App

A simple quiz application built with Flask, SQLAlchemy, and Flask-Login.

## Features

- User registration and login
- Create and take multiple-choice quizzes
- Leaderboard to display top quiz takers
- Scoring system: Users get a point for the first time they get 50% or more correct on a quiz

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/ahmadnasir00/Quiz_Corner.git
   cd Quiz_Corner
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
4. Run the app:
    ```sh
    python setup_admin.py && python create_quiz_db.py
    python run.py
