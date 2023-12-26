FROM python:3.12-slim
WORKDIR /app
RUN apt update
RUN apt install -y default-libmysqld-dev
# Copy the requirements.txt file into the container at /app/
RUN apt install -y pkg-config libhdf5-dev gcc
RUN pip install --upgrade pip setuptools wheel
COPY ./requirements.txt /app/

# Configure Git for Git Python
ENV GIT_PYTHON_REFRESH=quiet

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . /app/


CMD ["sh", "-c", "python src/manage.py makemigrations && python src/manage.py migrate && python src/manage.py runserver 0.0.0.0:8080"]