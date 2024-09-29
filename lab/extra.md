tagging

![image](https://github.com/user-attachments/assets/512add6f-7f29-48f4-a41f-0ed2ccf3bc37)

### user data test 

#!/bin/bash

# Update the system
sudo apt update -y

# Install Apache2
sudo apt install apache2 -y

# Create a custom index.html with server details
echo "<h1>Server Details</h1>
<p><strong>Hostname:</strong> $(hostname)</p>
<p><strong>IP Address:</strong> $(hostname -I | cut -d' ' -f1)</p>" | sudo tee /var/www/html/index.html

# Restart the Apache2 service
sudo systemctl restart apache2
