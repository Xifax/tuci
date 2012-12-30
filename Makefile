init:
	pip install -r requirements.txt --use-mirrors

test:
	lettuce tests

run:
	python t.pyw

env:
	virtualenv venv
