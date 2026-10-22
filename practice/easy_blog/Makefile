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
	${PYTHON3} fullstack_example/manage.py runserver

create_migrations:
	${PYTHON3} fullstack_example/manage.py makemigrations

migrations:
	${PYTHON3} fullstack_example/manage.py migrate

up_service:
	make clear
	make venv
	make install_requirements
	make create_migrations
	make migrations
	make run

superuser:
	${PYTHON3} fullstack_example/manage.py createsuperuser

start_static_server:
	npx http-server -p 3333 ./static
