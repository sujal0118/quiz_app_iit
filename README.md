#Console-Based Quiz App

Welcome to Console-Based Quiz App,a feature-rich ,consloe-based quiz app written in Python.This Project Simulates a real quiz experience through terminal,offering user authentication,dynamic question selection ,timed quizzes and leaderboard

> Built with simplicity ,spped and learning in mind

## Preview


## Features

✅ **User Registration & Login**  
✅ **Dynamic Subject & Difficulty Selection**  
✅ **Randomized Questions with Timer Support**  
✅ **Score Saving with Metadata (time, subject, level)**  
✅ **Top 5 Leaderboard (sorted by score & time)**  
✅ **File-Based Modular Architecture**  
✅ **Extensible Design for New Subjects/Difficulties**

---

## 🗂 Project Structure

```
quizmaster/
├── main.py                     # Entry point for the application
├── data/
│   ├── questions.txt           # Bank of all questions
│   ├── users.txt               # Registered user data
│   ├── score.txt               # All quiz attempts
│   └── leaderboard.txt         # Top 5 leaderboard data
├── utils/
│   ├── file_oprations.py       # File I/O functions
│   └── timer.py                # Countdown timer logic
└── README.md

```
## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/quizmaster.git
cd quizmaster
```

### 2. Ensure Python 3.x is Installed

You can verify by running:
```bash
python --version
```

### 3. Run the App

```bash
python main.py
```

---
##Question File Format

Ensure your `questions.txt` follows this CSV-like format:

```
Question,OptionA,OptionB,OptionC,OptionD,CorrectOption(A/B/C/D),Difficulty(easy/medium/hard)
```

**Example:**
```
What is the capital of India?,Delhi,Mumbai,Chennai,Kolkata,A,easy
```

---

---
## How It Works

1. Users **register/login** securely.
2. Choose a **subject** and **difficulty**.
3. Quiz questions are **randomized** and presented one-by-one.
4. A **timer** runs in the background based on difficulty level.
5. On completion, scores are saved and shown with time taken.
6. The **leaderboard** updates dynamically with top performers.

##Leaderboard Logic

The leaderboard displays the **Top 5 performers** based on:
- 🎯 **Highest Score**
- ⏱️ **Fastest Completion Time (if scores tie)**

Stored in `leaderboard.txt` for easy export and audit.


##Challenges Faced

- Implementing a **non-blocking timer** for each quiz level.
- Designing a **file-driven system** without databases.
- Sorting leaderboard by multiple criteria (**score + time**).
- Building a **clean console interface** with only native Python.

---

##  Future Enhancements

- Admin panel for adding/editing questions
- Web-based version using Flask/Django
- Detailed quiz analytics for users
- Profile system with historical data
- Email notifications for quiz results

---
##Demo Video

 **[Click here to watch the project demo](https://youtu.be/your-video-link)**  
📽️ Includes:
- Full feature walkthrough
- Code structure explanation
- Design decisions & challenges
---
## 👨‍💻 Author

**Sujal Jawalkar**
