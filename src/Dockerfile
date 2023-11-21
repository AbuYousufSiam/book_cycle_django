FROM python:3.12-slim
WORKDIR /app

# Install Git
RUN apt-get update && apt-get install -y git

# Configure Git for Git Python
ENV GIT_PYTHON_REFRESH=quiet

# Copy the requirements.txt file into the container at /app/
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app/

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]