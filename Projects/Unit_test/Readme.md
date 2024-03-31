# Task 2

### Step 1: Write Python Unit Test

1. Write a Python unit test script that connects to the atg.world website and checks if it loads properly. Include log or print statements for tracking.

```
import unittest
import requests

class TestWebsiteConnection(unittest.TestCase):

    def test_website_load(self):
        response = requests.get("https://atg.world")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

```

2. Push the Python unit test script to a GitHub repository.

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/fdbfd371-154f-4180-bf81-5e1a7605af0c)


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
   - Click on "New Item" to create a new pipeline job.
     ![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/1d6fddd3-7f88-4a07-b346-61467ccc1a1a)

   - Configure the job to run the Python unit test script.
   ![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/72873b40-fa99-4705-8ce6-7815596e6235)

   - Add necessary build steps to execute the test.


### Step 4: Run and Verify Unit Test in Jenkins

1. Trigger the Jenkins job manually to run the Python unit test.
Check the console output of the Jenkins job to see if the test passed or failed based on the website loading.
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/89ccb462-94c1-41fc-b916-38a70c208093)


![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/0199442d-4c21-4f51-bb2d-6c6251ab689c)


# Thank you! - Mathew Joseph 
