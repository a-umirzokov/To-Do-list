1. Create a virtual environment in a `venv/` folder by typing `python -m venv venv` in your console.
2. Activate the venv using `source venv/bin/activate` (Linux, MacOS) or `venv\Scripts\activate.bat` (Windows).
3. Install the dependencies with `python -m pip install -r requirements.txt`
4. Generate the empty SQLite database and tables using `python manage.py migrate`
5. Run the app with `python manage.py runserver`