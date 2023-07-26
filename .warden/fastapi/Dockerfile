FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY ./pyproject.toml ./
COPY ./poetry.lock* ./

RUN pip install poetry
RUN poetry install

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]