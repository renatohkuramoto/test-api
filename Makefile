test:
	ENV='test' pytest --cov-config=.coveragerc --cov-report html --cov=. ./

install_requirements:
	pip install -r requirements.txt && pip install -r development/requirements.txt

format:
	cd test-api && autopep8 . ; isort .

check_format:
	pycodestyle ./app; isort --check-only .
