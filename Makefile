init:
	pip install -r requirements.txt --use-mirrors

test:
	lettuce tests
