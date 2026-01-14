# Dynamic Portfolio Website (Django)

## Requirements (from the provided PDF)
- Portfolio sections: Bio, Education, Skills, Experience, Projects
- **Separate Django app for each section**
- Data must come from **database** (no hardcoded HTML data)

## Folder Structure (important)
- `bio/`, `education/`, `skills/`, `experience/`, `projects/`  → each section is its own Django app with its own model.
- `main/` → home page view that reads all apps' models and renders `templates/home.html`.

## Run Locally
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:
- Home: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Add Data (Admin Panel)
1. Create **one** record in **Bio**
2. Add multiple records in Education, Skill, Experience, Project

> If Bio is empty, the site will show placeholder text.
