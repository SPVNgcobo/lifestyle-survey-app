# Lifestyle Survey App

This is a full-stack web application that allows users to complete a lifestyle survey and view aggregated results. The project was developed as part of the **Tshimologong Software Development Internship** practical assignment.

## 🛠️ Built With

- HTML5 + CSS3
- JavaScript (Frontend logic)
- Python Flask (Backend API)
- SQLite (Database)

## 🧩 Features

### Screen 1: Fill Out Survey
- Collects Full Name, Email, Contact, and Date
- Allows users to select their favourite food (checkboxes)
- Users rate lifestyle questions (radio buttons: 1–5)
- Validates all inputs before submission
- Saves responses to SQLite database via Flask API

### Screen 2: View Survey Results
- Displays:
  - Total number of surveys
  - Average age (contact value)
  - Oldest and youngest participant
  - Percentage of users who like Pizza
  - Average “Eat Out” rating
- If no data is found, displays “No Surveys Available”
