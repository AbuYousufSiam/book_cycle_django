FROM python:3.12-slim
WORKDIR /app


# Install Git
RUN apt-get update && apt-get install -y git
# Configure Git for Git Python
ENV GIT_PYTHON_REFRESH=quiet

COPY . /app

RUN pip install -r src/requirements.txt

CMD ["sh", "-c", "python src/manage.py migrate && python src/manage.py runserver 0.0.0.0:8000"]
