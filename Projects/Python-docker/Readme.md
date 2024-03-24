
# Python web server displaying "hello world" containerized with Docker and hosted on an EC2 instance

To accomplish the task of creating a basic Python web server that displays "hello world", containerizing it with Docker, and hosting it on an EC2 instance, you can follow the steps below:

### Steps:

1. **Create a Python Web Server:**
   
   Create a Python file named `app.py` with the following code:
   ```
   from http.server import BaseHTTPRequestHandler, HTTPServer

   class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
       def do_GET(self):
           self.send_response(200)
           self.end_headers()
           self.wfile.write(b'Hello, World!')

   server_address = ('', 8000)
   httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
   httpd.serve_forever()
   ```

2. **Create a Docker Container:**
   
   Create a `Dockerfile` with the following content:
   ```
   FROM python:3.9
   COPY app.py /app.py
   CMD ["python", "/app.py"]
   ```

3. **Build and Run the Docker Container:**
   
   Build the Docker image:
   ```
   docker build -t hello-world-server .
   ```
   
   Run the Docker container:
   ```
   docker run -d -p 8000:8000 hello-world-server
   ```

4. **Host it on EC2:**
   
   - Launch an EC2 instance.
   - Install Docker on the EC2 instance.
   - Copy the Docker image to the EC2 instance.
   - Run the Docker container on the EC2 instance.

5. **Provide Details:**
   
   - IP Address/Hostname of the server: [Your EC2 Public IP/Hostname]
   - Docker Repository: [Provide the repository link if you pushed the image to Docker Hub]
   - Docker Code Details: [Provide the Dockerfile content]

### Note:
- Ensure that port 8000 is open in the security group of your EC2 instance.
- Modify the security settings and configurations as needed based on your requirements.

By following these steps, you will have a basic Python web server displaying "hello world" containerized with Docker and hosted on an EC2 instance.
