init:
	pip install -r requirements.txt --use-mirrors

test:
	nosetests -v tests

test:
	nosetests tests

configure:
	python configure.py
