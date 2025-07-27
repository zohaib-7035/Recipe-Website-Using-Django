
---

### ✅ Final Polished `README.md`

```markdown
# 🥗 Vegetable Recipe Web App

A Django web application that allows users to add, view, search, update, and delete vegetable recipes with image support.

---

## 📌 Project Overview

This is a beginner-friendly web app built using the Django framework. Users can:

- 📥 Add new vegetable recipes (with images)
- 🔍 Search recipes by name
- 🧾 View all added recipes
- 🗑️ Delete recipes
- ✏️ Update recipes

This project is ideal for learning CRUD (Create, Read, Update, Delete) operations in Django.

---

## 🛠️ Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS (Bootstrap)
- **Database**: SQLite (default)
- **Language**: Python 3

---

## 📂 Project Structure

```


### ✅ Full Project Tree — `vegetable_recipe`

```
vegetable_recipe/
├── core/
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   │   └── recipe.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── media/                     # User uploaded images (empty until uploaded)
│
├── static/                    # Static files (add CSS/JS here)
│   └── style.css              # Optional custom styling
│
├── vegetable_recipe/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3                 # SQLite database
├── manage.py
├── requirements.txt           # Add with `pip freeze > requirements.txt`
└── README.md                  # You can paste your GitHub readme here
```

---




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

If `requirements.txt` is missing:

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

Then open [http://127.0.0.1:8000/recipe/](http://127.0.0.1:8000/recipe/) in your browser.

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

In `views.py`:

```python
search_query = request.GET.get('search', '')
recipes = Vege.objects.filter(name__icontains=search_query)
```

In `recipe.html`:

```html
<form method="GET" action="{% url 'recipe' %}" class="mb-4">
    <input type="text" name="search" class="form-control" placeholder="Search recipe by name..." value="{{ request.GET.search }}">
    <button type="submit" class="btn btn-primary mt-2">Search</button>
</form>
```

---

## ✅ Features Checklist

* [x] Add recipe with image
* [x] View all recipes
* [x] Search recipe by name
* [x] Delete recipe
* [x] Update recipe
* [ ] User authentication (optional)

---

## 🤝 Contributing

Contributions are welcome! Fork the repo, make your changes, and submit a pull request.

---

## 📄 License

Licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

---

## 🙋‍♂️ Author

**Zohaib Shahid**

---

## 📚 Acknowledgments

* [Django Documentation](https://docs.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Pillow Library](https://python-pillow.org/)

```

---

