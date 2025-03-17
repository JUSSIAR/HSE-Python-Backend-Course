PIP := .venv/bin/pip
PYTHON3 := .venv/bin/python3

clear:
	rm -rf .venv

venv:
	python3 -m venv .venv

install_requirements:
	${PIP} install -r requirements.txt

freeze:
	${PIP} freeze > requirements.txt

run:
	${PYTHON3} manage.py runserver

create_migrations:
	${PYTHON3} manage.py makemigrations

migrations:
	${PYTHON3} manage.py migrate

up_service:
	make clear
	make venv
	make install_requirements
	make create_migrations
	make migrations
	make run

superuser:
	${PYTHON3} content/manage.py createsuperuser

start_static_server:
	npx http-server -p 3000 ./frontend/scripts
