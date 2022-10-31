![](https://raw.githubusercontent.com/Gaudencio11/imersao/main/static/images/LOGO-ROXA-LETREIRO-HORIZONTAL.png)

**Web page da imersão da Fábrica de Software 2021.1**

![](https://img.shields.io/badge/Django-3-blue) ![](https://img.shields.io/badge/Python-3-blue) ![](https://img.shields.io/badge/Pillow-8.2.0-green) ![](https://img.shields.io/badge/psycopg2-newest_version-green)

### Features

- A Platform for events where you can put information and put links in card format
- You can add the information through the admin page, code editing no needed 


### Instalation

Initiate venv at the project diretory:

	py venv -m venv
	cd venv/Scripts
	activate
	cd ../..

Install requirements.txt:

	py manage.py -r requirements.txt

Run comands bellow (repeat process may be required) to migrate:

	py manage.py makemigrations
	py manage.py migrate
	py manage.py runserver

#### Usefull documentation:
[Django Docs](https://docs.djangoproject.com/en/4.1/) 

[Heroku Docs](https://devcenter.heroku.com/categories/reference)

Use this code as you want, we hope it can help you :call_me_hand: 
