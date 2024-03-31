# Task 2

### Step 1: Write Python Unit Test

1. Write a Python unit test script that connects to the atg.world website and checks if it loads properly. Include log or print statements for tracking.
```
import requests

def test_website_load():
    url = "https://atg.world"
    response = requests.get(url)
    assert response.status_code == 200, "Website did not load properly"
    print("Website loaded successfully")

if __name__ == "__main__":
    test_website_load()
```

2. Push the Python unit test script to a GitHub repository.

### Step 2: Host Jenkins on a Free Server

1. Set up a free server (e.g., AWS EC2, Google Cloud, or any other hosting service).

   Install **Java**
   
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/4d146df2-cae1-4eed-ae41-715077259fcf)

   
3. Install Jenkins on the server. You can follow the official Jenkins installation [guide](https://www.jenkins.io/doc/book/installing/linux/#debianubuntu)
   
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/f3fea253-e0a4-42f7-814f-556d61f21382)

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/39b735aa-4b71-461b-aa78-916f9aaba603)

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/877f7654-b951-410b-b36d-f83a1d88ab06)

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/e01ecd6f-fd0d-4dcf-9e02-aea09502ee38)


### Step 3: Configure Jenkins Job
1. Create a new Jenkins job:
   - Go to Jenkins dashboard.
   - Click on "New Item" to create a new job.
   - Configure the job to run the Python unit test script.
   - Add necessary build steps to execute the test.

### Step 4: Run and Verify Unit Test in Jenkins
1. Trigger the Jenkins job manually to run the Python unit test.
2. Check the console output of the Jenkins job to see if the test passed or failed based on the website loading.

### Step 5: Submission
1. Share the link to your Jenkins instance hosted at `jenkins.domainname.com`.
2. Provide steps to run the unit test in Jenkins.
3. Record a screen capture showing the Jenkins job configuration, Jenkinsfile, and build job console output.
4. Share the video link and GitHub link to the Python unit test program as part of your submission.

### Additional Notes:
- Make sure to properly document all steps and configurations for easy understanding.
- Test the entire setup before submission to ensure everything works as expected.

If you have any questions or need further clarification on any step, feel free to ask. Good luck with your task submission!
