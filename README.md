# 📌 Sticky Notes (Django)

Bootcamp project — a colourful sticky-notes board with full **CRUD**
(Create, Read, Update, Delete).

## Features
- Board view of all notes (`/`)
- Note detail (`/note/<pk>/`)
- Create (`/note/new/`), Edit (`/note/<pk>/edit/`), Delete confirmation (`/note/<pk>/delete/`)
- Colour-coded notes (yellow / pink / green / blue / purple)
- Bootstrap 5 + custom CSS (`static/notes/css/style.css`)
- Admin interface enabled (`/admin/`)

## Design diagrams
See [`diagrams/`](diagrams/) — required submission artefacts:
- `use_case_diagram.png` — actor + 5 CRUD use cases
- `sequence_diagram.png` — Create-Note flow (Browser → View → Form → Model → DB)
- `class_diagram.png` — `Note`, `NoteForm`, CBV views
- `diagrams/README.md` — PlantUML sources + design notes

## Setup (venv excluded from submission — mentor regenerates it)
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Open http://127.0.0.1:8000/

## Static files
```bash
python manage.py collectstatic
```
collects CSS into `staticfiles/` (`STATIC_ROOT`), per Step 12.

## Project layout
```
sticky_notes/        # project config (settings.py, urls.py)
notes/               # app: models.py, forms.py, views.py, urls.py, admin.py
notes/templates/notes/  base.html, note_list.html, note_detail.html,
                        note_form.html, note_confirm_delete.html
static/notes/css/style.css
diagrams/            # use-case, sequence, class diagrams + README
```
