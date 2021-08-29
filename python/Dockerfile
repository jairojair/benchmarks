FROM python:3.9-alpine AS base

RUN apk add --update  \
	postgresql-dev \
	gcc \
	musl-dev \
	make

RUN pip install --upgrade pip

COPY requirements.txt /
RUN pip install -r requirements.txt

FROM base AS fastapi

EXPOSE 8000
COPY ./fastapi/main.py /main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


FROM base AS flask

EXPOSE 5000
COPY ./flask/main.py /main.py
CMD ["gunicorn", "main:app", "-b", "0.0.0.0:5000"]