
# Lifestyle Survey App

A full-stack web application created for the Tshimologong Software Development Internship practical test. It collects lifestyle survey data from users and presents summarized results. The application is built using HTML, CSS, JavaScript, Python (Flask), and SQLite.

## 🛠️ Technologies Used

- HTML & CSS for layout and styling
- JavaScript for form logic and validation
- Python Flask for backend API
- SQLite for data storage

## 🎯 Features

### Screen 1: Fill Out Survey
- Collects:
  - Full Name
  - Email
  - Contact
  - Date of Birth (used to calculate age)
- Select multiple favourite foods (checkboxes)
- Rate lifestyle questions (radio buttons from 1 to 5)
- Validation:
  - All fields must be filled
  - At least one food must be selected
  - All rating questions must be answered
  - Age must be between 5 and 120 (calculated from Date of Birth)

### Screen 2: View Survey Results
- Displays:
  - Total number of surveys
  - Average age
  - Oldest participant
  - Youngest participant
  - Percentage of people who like Pizza
  - Average rating for “Eat out”
- Shows "No Surveys Available" if no data is in the database

## 📂 Project Structure

```
index.html         # User interface
style.css          # Styles (Zaziza Tech branding)
script.js          # Form validation and backend communication
server.py          # Flask API and SQLite logic
survey.db          # SQLite database (auto-generated)
```

## 🚀 Running the App Locally

### Prerequisites
- Python 3.x installed
- Flask + Flask-CORS

Install dependencies:

```bash
pip install flask flask-cors
```

Run the server:

```bash
python server.py
```

Then open `index.html` in your browser.

## 🎥 Demo

👉 [link here]

## 👤 Author

**Snethemba Promise Ngcobo**  
📧 s.p.ngcobo@outlook.com  
🔗 [LinkedIn](https://za.linkedin.com/in/spngcobo)

---

## 📄 License

This project is provided for educational purposes and evaluation for the internship program.
