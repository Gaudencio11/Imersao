passos para rodar servidor local
python3 -m venv venv
pip install -r "requirements.txt"

py manage.py runserver
(control + c para parar servidor)

py manage.py makemigrations
py manage.py migrate

py manage.py runserver
(manda bala)
