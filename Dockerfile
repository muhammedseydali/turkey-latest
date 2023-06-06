FROM python:3.8-slim

WORKDIR /app

COPY . /app/

RUN pip install -r r.txt

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project.wsgi:application"]
