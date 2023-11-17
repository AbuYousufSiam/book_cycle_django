FROM python:3.12-slim
WORKDIR /app
RUN apt update
# RUN apt install -y default-libmysqld-dev
# Copy the requirements.txt file into the container at /app/
COPY src/requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . /app/


CMD ["sh", "-c", "python src/manage.py migrate && python src/manage.py runserver 0.0.0.0:8080"]