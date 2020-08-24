python -m venv venv

source venv/Scripts/activate (가상환경 생성)

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver