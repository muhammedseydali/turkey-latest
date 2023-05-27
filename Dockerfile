FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install -r r.txt

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
