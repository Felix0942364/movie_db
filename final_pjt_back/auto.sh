rm -rf articles/migrations
rm -rf articles/__pycache__
rm -rf accounts/migrations
rm -rf accounts/__pycache__
rm -rf movies/migrations
rm -rf movies/__pycache__
rm -rf final_pjt_back/__pycache__
rm db.sqlite3

mkdir accounts/migrations
mkdir articles/migrations
mkdir movies/migrations

touch accounts/migrations/__init__.py
touch articles/migrations/__init__.py
touch movies/migrations/__init__.py



# python manage.py makemigrations 
# python manage.py migrate
# python manage.py runserver

