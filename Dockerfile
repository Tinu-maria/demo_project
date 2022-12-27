FROM python:3.8-slim-buster

# ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
 
COPY . .

CMD ["python3","manage.py","runserver", "0.0.0.0:8000"]

# EXPOSE 8000

# CMD python3 manage.py runserver