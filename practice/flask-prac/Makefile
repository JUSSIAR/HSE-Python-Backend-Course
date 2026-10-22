PIP := venv/bin/pip
PYTHON3 := venv/bin/python3

clear:
	rm -rf venv

venv:
	python3 -m venv venv

install_requirements:
	${PIP} install -r requirements.txt

freeze:
	${PIP} freeze > requirements.txt

run:
	${PYTHON3} main.py

up_service:
	make clear
	make venv
	make install_requirements
	make run
