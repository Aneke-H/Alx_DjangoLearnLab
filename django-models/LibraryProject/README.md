# 📚 LibraryProject – Introduction to Django Development Environment Setup

## 🎯 Objective

This project demonstrates how to set up a basic Django development environment.  
It was created as part of the `Introduction_to_Django` module from the `Alx_DjangoLearnLab` repository.

---

## 🛠️ Steps Followed

### 🥇 Step 1: Install Django

Ensure the Python installed on your system is python version 3.10 or greater.
`Use Python --version` to confirm.

Create a virtual env for the project using
```bash
python -m venv lms_venv
```
The above is so that all dependencies are packaged in a virtual env.


Django was installed using pip:

```bash
pip install django
```

🥈 Step 2: Create the Django Project

A new Django project named LibraryProject was created using:

```
django-admin startproject LibraryProject
```

🥉 Step 3: Navigate to the Project Directory

Changed into the project folder: and explore the project structure

```
cd LibraryProject

Introduction_to_Django/
└── LibraryProject/
    ├── LibraryProject/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    ├── manage.py
    └── README.md   ← this file

```

🏃 Step 4: Start the Development Server

The development server was started with:
```
python manage.py runserver
```

This launched the server at:

http://127.0.0.1:8000/ or *localhost:8000*


**Opening that URL in a browser showed the default Django welcome page, confirming that the setup was successful.**

**lastly** use `pip freeze > requirement.txt` to save the list of your dependencies used.