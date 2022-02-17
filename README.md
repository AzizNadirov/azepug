# AzePUG
### My portfolio platform for Azerbaijanian Python Users Group

Ideally, this will have abilities: blog, events, vacancies. And commenting all of them for logged in users.
## How to install:
1) Install python packages: 
    pip install -r requirements.txt
2) Make migrations and apply them:
    python manage.py makemigrations
    python manage.py migrate
3) Run dewelopment server:
    python manage.py runserver
4) Open up localhost in your browser
    http://127.0.0.1:8000/