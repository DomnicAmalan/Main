FROM python:3.8.2

COPY pyproject.toml /

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

RUN pip3 install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]




