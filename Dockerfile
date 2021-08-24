# Pull base image
FROM python:3.7-slim

# Install psql so that "python manage.py dbshell" works
RUN apt-get update -qq && apt-get install -y postgresql-client

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /django

# Install dependencies
COPY requirements.txt /django/requirements.txt
RUN pip install -r /django/requirements.txt

# Copy project
COPY . /django/


