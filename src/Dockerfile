FROM python:3.12-slim
WORKDIR /src
COPY requirements.txt /src/
# Install Git
RUN apt-get update && apt-get install -y git
# Configure Git for Git Python
ENV GIT_PYTHON_REFRESH=quiet

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code
COPY . /src/

CMD ["sh", "-c", "python src/manage.py migrate && python src/manage.py runserver 0.0.0.0:8000"]
