FROM python:3.12-slim

RUN apt-get update && \
apt-get install -y gettext && \
rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


RUN python manage.py compilemessages

RUN mkdir -p /vol/web/static
RUN python manage.py collectstatic --noinput

EXPOSE 3000
CMD ["gunicorn", "--bind", "0.0.0.0:3000", "config.wsgi:application"]
