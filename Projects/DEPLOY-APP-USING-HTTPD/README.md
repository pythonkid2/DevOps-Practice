To deploy the app using Apache HTTP Server (`httpd`), follow these steps:

1. Update the system and install necessary packages:
    ```
    sudo yum update -y
    sudo yum install httpd git -y
    ```

2. Clone the repository and navigate to the project directory:
    ```
    git clone https://github.com/pythonkid2/DevOps-Practice
    cd DevOps-Practice/Projects/DEPLOY-APP-USING-HTTPD
    ```

3. Move the contents of the project directory to `/var/www/html/`, which is the default directory where Apache (`httpd`) serves files:
    ```
    sudo cp -r * /var/www/html/
    ```

4.Start HTTPD

```
sudo systemctl start httpd
sudo systemctl enable httpd
```

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/fb956e72-7072-4c97-9281-6b993a53a4dc)

  Optionally, if you need to clone a specific branch:
    ```
    git clone -b branch_name https://github.com/pythonkid2/DevOps-Practice
    ```

This series of commands will update the system, install `httpd` and `git`, clone the repository, and deploy the app by copying its contents to the Apache document root directory (`/var/www/html/`). If you need to clone a specific branch, you can use the provided command.

