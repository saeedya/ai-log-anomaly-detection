install:
	pip install -r requirements-dev.txt

run:
	uvicorn app.main:app --reload

train:
	python ml/train.py

test:
	pytest

lint:
	ruff check .

security:
	bandit -r app ml
	pip-audit -r requirements.txt
	pip-audit -r requirements-dev.txt

docker-build:
	docker build -t ai-log-anomaly-detection:latest .

docker-run:
	docker run --rm -p 8000:8000 ai-log-anomaly-detection:latest