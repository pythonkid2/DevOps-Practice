# Dockerize Django App Guide

This guide provides step-by-step instructions for setting up and running a Django project using Docker on an Ubuntu instance.

## Prerequisites

- Ubuntu instance on AWS
- Docker installed on your Ubuntu instance  [click here](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
- Basic knowledge of working with the terminal/command line

## Step 1: Install Django and Create a New Project

### Install Django

Install Django using pip:

```
sudo apt update
sudo apt install python3-pip
pip3 install Django
```

### Create a New Django Project

Create a new Django project:

```
django-admin startproject Dockerize_Django_App
```
```
cd Dockerize_Django_App
```

## Step 2: Create HTML Page

Create an HTML page for your Django project. 

**Create HTML Template**: Create a new directory named `templates` inside the `Dockerize_Django_App` directory. Then create a file named `index.html` and paste your HTML code into it.

```
mkdir templates && cd templates && vi index.html
```

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Welcome to Mathew's Web App!</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f8f9fa; /* Lighter background */
      color: #333;
      margin: 0;
      padding: 0;
    }
    h1 {
      color: #007bff;
      text-align: center;
      margin-top: 50px; /* Added margin */
    }
    .container {
      max-width: 600px;
      margin: auto;
      padding: 20px;
      background-color: #fff; /* White background */
      border-radius: 10px; /* Rounded corners */
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Box shadow */
    }
    p {
      margin-bottom: 20px; /* Increased margin */
      line-height: 1.6; /* Improved readability */
    }
    ul {
      list-style-type: none;
      padding: 0;
    }
    ul li {
      margin-bottom: 10px; /* Adjusted margin */
    }
    a {
      color: #007bff;
      text-decoration: none;
      transition: color 0.3s; /* Smooth color transition */
    }
    a:hover {
      color: #0056b3; /* Darker blue on hover */
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Welcome to Mathew's Web App!</h1>
    <p>Hi there! I'm Mathew, a DevOps Engineer.</p>
    <p>This app is a work in progress. Feel free to explore!</p>
    <ul>
      <li><a href="https://www.linkedin.com/in/mathewjoseph-devops/">LinkedIn</a></li>
      <li><a href="https://github.com/pythonkid2">GitHub</a></li>
    </ul>
    <p>Thanks for visiting!</p>
  </div>
</body>
</html>
```

Save this HTML code in a file named `index.html` in the `Dockerize_Django_App` directory.


## Step 3: Configure Django Settings

Add the HTML page to Django settings by modifying `Dockerize_Django_App/settings.py`. Add `'DIRS': [os.path.join(BASE_DIR, 'templates')],` to the `TEMPLATES` setting.

```
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]
```

you need to import the `os` module at the top of your `settings.py` file. Add the following line at the beginning of `settings.py` file:

```
import os
```

we can allow all IP traffic by setting `ALLOWED_HOSTS` to `['*']`. However, this approach is not recommended for production environments as it can pose security risks by potentially allowing unauthorized access to your Django application.

1. Open your Django project's `settings.py` file.

2. Locate the `ALLOWED_HOSTS` setting.

3. Change it to allow all IP traffic by setting it to `['*']`:

```
ALLOWED_HOSTS = ['*']
```

5. Save the `settings.py` file.

With this configuration, your Django server will accept requests from any host. Remember to revert this setting to a more restrictive configuration (`ALLOWED_HOSTS = ['YOUR_PUBLIC_IP']` or `ALLOWED_HOSTS = ['YOUR_DOMAIN_NAME']`) before deploying your application to a production environment.


Django by default displaying its default page because there are no URLs configured to handle the root URL (`/`) Django project.

To display our HTML page instead, we need to define a URL pattern in your Django project's `urls.py` file to map the root URL to a view that renders HTML template.

1. **Create a View Function**:

Open the `views.py` file in Django app directory. If you don't have create one.
   
Define a view function that renders  HTML template (`index.html`). 
   
```
echo -e "from django.shortcuts import render\n\ndef index(request):\n    return render(request, 'index.html')" > views.py
```

3. **Define URL Mapping**:
   Open the `urls.py` file in Django app directory,
   
Define a URL pattern that maps the root URL (`/`) to the `index` view function you just created. 

```
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Add this line to route the root URL to the index view
    path('admin/', admin.site.urls),  # This line includes the admin URLs
]
```

### Start& Test Django Development Server Locally

Start the Django development server:

```
python3 manage.py runserver 0.0.0.0:8000
```

Access the Django app in your web browser at `http://<your_instance_public_ip>:8000`.

![image](https://github.com/pythonkid2/DevOps-Projects/assets/100591950/dc45aa09-4c25-4315-9f33-9174dac64ad6)

## Step 5: Dockerize Django App

create requirements.txt

```
echo "Django" >> requirements.txt
```
### Create Dockerfile

Create a Dockerfile in the project root directory (`Dockerize-Django-App`) with the following content:

```
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
```

### Build Docker Image

Build the Docker image:

```
docker build -t my_django_app .
```
```
docker login
```
```
docker tag my_django_app mjcmathew/my_django_app:v1.0.0
```
```
docker push mjcmathew/my_django_app:v1.0.0
```
### Run Docker Container

Run a Docker container using the built image:

```
docker run -d -p 8000:8000 my_django_app
```

Access the Dockerized Django app in your web browser at `http://<your_instance_public_ip>:8000`.

## Additional Notes

- Ensure that your AWS security group allows incoming traffic on port 8000 for accessing the Django app.
- Modify the `ALLOWED_HOSTS` setting in `Dockerize-Django-App/settings.py` to include your instance's public IP or domain name.
- Make sure to revert `ALLOWED_HOSTS` to a more restrictive configuration before deploying to production.

## License

This project is licensed under the [MIT License](LICENSE).
```

This README.md file contains all the necessary steps, starting from installing Django to running the project with Docker on an Ubuntu instance, with the project name changed to "Dockerize-Django-App". 
