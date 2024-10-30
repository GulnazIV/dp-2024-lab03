FROM python:3.10-slim

WORKDIR /app

COPY . .

CMD ["bash", "-c", "python -m unittest tests/tests.py && python main.py"]