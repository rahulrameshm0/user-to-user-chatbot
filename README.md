# 🗨️ User-to-User Chatbot

A Django-based real-time messaging web application that allows registered users to communicate privately with each other — similar to a simple version of WhatsApp or Messenger. This project demonstrates how to implement user authentication, messaging, and dynamic UI updates in Django.

---

## 🚀 Features

- 🔐 User registration, login, and logout system
- 🧑‍🤝‍🧑 Chat with any registered user (user-to-user)
- 📩 Real-time message updates (using Django ORM and AJAX)
- 🔔 Unread message indicator
- 🖼️ Clean and responsive UI

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (can be upgraded to PostgreSQL)
- **Version Control:** Git + GitHub

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/rahulrameshm0/user-to-user-chatbot.git
cd user-to-user-chatbot

cd django-chat-app
```
-
## 🤝 Contributions
- Feel free to fork this project and contribute to make it better.

## 2. Create and Activate Virtual Environment

```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```
## 2. Create and Activate Virtual Environment

```bash
pip install -r requirements.txt
```
## 3. Install Dependencies
```bash
pip install -r requirements.txt
```
## 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
## 5. Start the Development Server
```bash
python manage.py runserver
Visit http://127.0.0.1:8000 in your browser.
```


## 📁 Folder Structure
```bash
user-to-user-chatbot/
│
├── chatapp/               # Django app for chat logic
│   ├── models.py          # Message model
│   ├── views.py           # Handles chat view logic
│   └── templates/
│       └── chatapp/       # HTML templates
│
├── static/                # Static files (CSS, JS)
├── media/                 # Uploaded media files
├── screenshots/           # App screenshots for README
├── db.sqlite3             # SQLite database
├── manage.py
└── requirements.txt
👨‍💻 Author
Rahul Ramesh
🔗 

```


## 🌐 Deployment (Optional)

Heroku (if PostgreSQL support is added)

## 📌 Future Improvements
✅ WebSocket support for real-time messaging

✅ Profile picture support

✅ Group chat

✅ Better mobile responsiveness

---
