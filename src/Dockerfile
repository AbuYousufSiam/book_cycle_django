FROM python:3.12-slim
WORKDIR /app
RUN apt update

COPY src/requirements.txt /app/

RUN apt-get install -y git
# Configure Git for Git Python
ENV GIT_PYTHON_REFRESH=quiet
COPY . /app/

RUN pip install -r requirements.txt
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
