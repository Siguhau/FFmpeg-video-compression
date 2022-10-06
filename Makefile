fixme:
	docker run --rm -v "${PWD}:/code" -it python:3.10 "bash" "-c" "cd /code && pip install -r requirements/black.txt -r requirements/isort.txt -r requirements/flake8.txt && isort src && black src && flake8 src"
