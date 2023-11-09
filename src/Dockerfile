FROM python:3.12-slim
WORKDIR /app
RUN apt update
# RUN apt install -y default-libmysqld-dev
COPY . /app/
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]