# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.11

WORKDIR /code

ENV PYTHONUNBUFFERED=1

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
COPY . /code
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
EXPOSE 8888

# runs the production server
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8888"]