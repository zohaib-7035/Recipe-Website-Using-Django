
```markdown
## 🥗 Vegetable Recipe Web App

A Django web application that allows users to add, view, search, and delete vegetable recipes with image support.

---

## 📌 Project Overview

This is a beginner-friendly web app built using the Django framework. Users can:

- 📥 Add new vegetable recipes (with images)
- 🔍 Search recipes by name
- 🧾 View all added recipes
- 🗑️ Delete recipes

This project is ideal for learning CRUD (Create, Read, Update, Delete) operations in Django.

---

## 🖥️ Demo

> 🚧 Add screenshots or a live demo link if hosted.

---

## 🛠️ Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS (Bootstrap for styling)
- **Database**: SQLite (default with Django)
- **Language**: Python 3

---

## 📂 Project Structure

```

vegetable\_recipe/
├── core/                  # Main Django app
│   ├── migrations/
│   ├── templates/
│   │   └── recipe.html    # Main HTML template
│   ├── **init**.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py          # Vege model defined here
│   ├── tests.py
│   ├── urls.py            # App-level routing
│   └── views.py           # Business logic
├── media/                 # Uploaded recipe images
├── static/                # Static files (CSS, JS, Images)
├── vegetable\_recipe/      # Project-level settings
│   ├── **init**.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py            # Project-level URL configuration
│   └── wsgi.py
├── db.sqlite3             # SQLite database
├── manage.py
├── requirements.txt       # Project dependencies
└── README.md              # This file

````

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/vegetable-recipe-app.git
cd vegetable-recipe-app
````

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # On Windows
source venv/bin/activate     # On macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install django pillow
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/recipe/](http://127.0.0.1:8000/recipe/)

---

## 🧾 Example Model: `Vege`

```python
class Vege(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
```

---

## 🔍 Search Feature

* In the frontend (`recipe.html`), there's a search form.
* On the backend, the view filters recipes using `icontains`:

```python
search_query = request.GET.get('search', '')
recipes = Vege.objects.filter(name__icontains=search_query)
```

---

## ✅ Features To-Do

* [x] Add recipe with image
* [x] View all recipes
* [x] Search recipe by name
* [x] Delete recipe
* [ ] Edit recipe (optional)
* [ ] User login & authentication (optional)

---


## 🤝 Contributing

Contributions are welcome! Please fork the repo and submit a pull request.

---

## 📄 License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

---

## 🙋‍♂️ Author

**Zohaib Shahid**

---

## 📚 Acknowledgments

* [Django Documentation](https://docs.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Pillow](https://python-pillow.org/)

```

---


