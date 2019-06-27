FROM python:3.7.3-stretch

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY Pipfile Pipfile.lock ./
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --dev --system

COPY docker/django/uwsgi.ini ./uwsgi.ini
RUN mkdir -p /var/log/backend/uwsgi && chown -R root:root /var/log/backend/uwsgi

COPY docker/django/start.sh ./start.sh
RUN chmod +x start.sh

COPY . .

EXPOSE 8000
