# Gift Store

An online gift shop built with Django, allowing users to browse, customize, and order personalized gifts.

## Tools & Technologies Used

- **Python 3.x**
- **Django** (web framework)
- **SQLite** (default database)
- **Bootstrap** (frontend styling)
- **HTML/CSS/JavaScript**
- **Git & GitHub** (version control)
- **Pillow** (image handling)
- **VS Code** (recommended IDE)

## Features

- User authentication (signup, login, logout)
- Product listing with images and descriptions
- Customization options for products
- Shopping cart and guest cart support
- Checkout and order placement
- Responsive design

## Project Structure

```
customized_gifts/
    manage.py
    customized_gifts/
        settings.py
        urls.py
        ...
    store/
        models.py
        views.py
        templates/
        ...
    static/
        css/
        ...
    media/
        products/
        ...
db.sqlite3
```

## Setup & Run Commands

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/gift-store.git
   cd gift-store/customized_gifts
   ```

2. **Create and activate a virtual environment**
   ```sh
   python -m venv venv
   venv\Scripts\activate   # On Windows
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations**
   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```sh
   python manage.py runserver
   ```

7. **Access the site**
   Open [http://localhost:8000](http://localhost:8000) in your browser.

## License

MIT

## Credits

Built with Django, Bootstrap, and VS Code.
