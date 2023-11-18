# Use a specific version of Python image
FROM python:3.12-slim

# Set the working directory to /app
WORKDIR /app

# Update the package index
RUN apt-get update

# Copy the requirements.txt file into the container at /app/
COPY src/requirements.txt /app/

# Copy the entire project into the container at /app/
COPY . /app/

# Install Git
RUN apt-get install -y git

# Configure Git for Git Python
ENV GIT_PYTHON_REFRESH=quiet

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Command to run on container start
CMD ["bash", "-c", "python src/manage.py migrate && python src/manage.py runserver 0.0.0.0:8000"]
