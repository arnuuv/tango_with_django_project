# **Rango - A Django Project**

This is a university project following the first 10 chapters of the Tango with Django book. The project is built using Django and covers fundamental concepts such as models, views, templates, forms, authentication, and session handling.

# **Installation and Setup**

1. Clone the Repository
   ~git clone <your-repository-url>
   ~cd rango

2. Create and Activate a Virtual Environment
   a) On Windows (cmd/powershell):
   ~python -m venv venv
   ~venv\Scripts\activate

   b) On macOS/Linux:
   ~python3 -m venv venv
   ~source venv/bin/activate

3. Install Dependencies
   ~pip install -r requirements.txt

4. Apply Migrations
   ~python manage.py migrate

5. Create a Superuser (Optional, for admin access)
   ~python manage.py createsuperuser

Follow the prompts to set up a username, email, and password.

6. Run the Development Server
   ~python manage.py runserver

Access the project at: http://127.0.0.1:8000/

# **Additional Commands**

1. Running the Django Shell
   ~python manage.py shell

2. Running Tests
   ~python manage.py test

3. Collecting Static Files
   ~python manage.py collectstatic

4. Deactivating Virtual Environment
   ~deactivate

# **Contributing**

~Feel free to fork this repository and submit pull requests.

# **License**

~This project is for educational purposes and follows the structure of Tango with Django.
