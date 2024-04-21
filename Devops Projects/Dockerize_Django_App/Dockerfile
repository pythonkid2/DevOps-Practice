# Use the official Python image as a parent image
FROM python:3.10

# Set environment variables to prevent Python from writing pyc files and buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install dependencies
RUN pip install -r requirements.txt

# Run the Django development server on port 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
