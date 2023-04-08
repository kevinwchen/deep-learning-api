FROM python:3.9

WORKDIR /app

ENV PORT 8080

ENV HOST 0.0.0.0

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

EXPOSE ${PORT}

CMD exec uvicorn main:app --reload --host ${HOST} --port ${PORT}