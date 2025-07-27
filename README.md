

````markdown
# 🥕 Vegetable Recipe Web App (Django)

A simple Django-based web application to **add**, **view**, **search**, and **delete** vegetable recipes with image support.

---

## 🚀 Features

- Add new vegetable recipes (name, description, image)
- View all stored recipes
- Search recipes by name
- Delete recipes (with confirmation)
- Responsive and user-friendly interface (HTML/CSS)
- Uses Django’s built-in ORM and admin panel

---

## 🛠 Tech Stack

- **Backend:** Django
- **Frontend:** HTML, CSS (Bootstrap or plain)
- **Database:** SQLite (default in Django)
- **Language:** Python

---

## 📸 Screenshots

> _Add screenshots of your homepage, recipe list, and add form here._

---

## 🔧 Installation

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/vegetable-recipe-app.git
cd vegetable-recipe-app
````

2. **Create and Activate Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Linux/macOS
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Start the Server**

```bash
python manage.py runserver
```

6. **Visit the App**

Open your browser and go to:
`http://127.0.0.1:8000/recipe/`

---

## 📝 Folder Structure

```
vegetable-recipe/
├── core/                 # Main Django app
│   ├── models.py         # Vege model
│   ├── views.py          # View logic
│   ├── urls.py           # URL routing
│   └── templates/
│       └── recipe.html   # Main template
├── static/               # Static files (CSS, images)
├── media/                # Uploaded images
├── db.sqlite3            # SQLite database
├── manage.py
└── README.md
```

---

## ✍️ Model Info

**Vege model (core/models.py):**

```python
class Vege(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
```

---

## 📬 Contact

If you have any questions or suggestions, feel free to open an issue or reach out:

* GitHub: [yourusername](https://github.com/yourusername)
* Email: [your.email@example.com](mailto:your.email@example.com)

---

## 📄 License

This project is licensed under the MIT License.

```

---

### ✅ Optional Additions:

- You can add a `requirements.txt` file with:
```

Django>=3.2
Pillow

```


