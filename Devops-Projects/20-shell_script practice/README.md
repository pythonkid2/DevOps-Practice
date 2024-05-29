
### Task 1: Greeting Script
Create a script that asks for the user's name and then greets them.

#### Hint:
1. Use `read` to get input from the user.
2. Use `echo` to print the greeting.

**Example:**
```bash
#!/bin/bash

echo "Please enter your name:"
read name
echo "Hello, $name! Welcome to the script."
```

### Task 2: Simple Arithmetic
Create a script that takes two numbers as input and performs addition, subtraction, multiplication, and division.

#### Hint:
1. Use `read` to get input from the user.
2. Use arithmetic expansion `$(())` to perform calculations.

**Example:**
```bash
#!/bin/bash

echo "Enter first number:"
read num1
echo "Enter second number:"
read num2

sum=$((num1 + num2))
difference=$((num1 - num2))
product=$((num1 * num2))
if [ $num2 -ne 0 ]; then
    quotient=$((num1 / num2))
else
    quotient="undefined (division by zero)"
fi

echo "Sum: $sum"
echo "Difference: $difference"
echo "Product: $product"
echo "Quotient: $quotient"
```

### Task 3: File Existence Check
Create a script that checks if a file exists and prints a message accordingly.

#### Hint:
1. Use an `if` statement with the `-e` flag to check for file existence.

**Example:**
```bash
#!/bin/bash

echo "Enter the filename to check:"
read filename

if [ -e "$filename" ]; then
    echo "The file '$filename' exists."
else
    echo "The file '$filename' does not exist."
fi
```

### Task 4: Loop Through Numbers
Create a script that prints numbers from 1 to 10.

#### Hint:
1. Use a `for` loop to iterate through a range of numbers.

**Example:**
```bash
#!/bin/bash

for i in {1..10}; do
    echo "Number: $i"
done
```

### Task 5: Backup Script
Create a script that backs up a specified directory to another directory.

#### Hint:
1. Use `cp -r` to copy directories recursively.
2. Use `read` to get the source and destination directories from the user.

**Example:**
```bash
#!/bin/bash

echo "Enter the source directory to backup:"
read source
echo "Enter the destination directory:"
read destination

if [ -d "$source" ]; then
    cp -r "$source" "$destination"
    echo "Backup of '$source' completed in '$destination'."
else
    echo "The source directory '$source' does not exist."
fi
```

### Task 6: Check Disk Usage
Create a script that checks the disk usage of your home directory and prints a warning if it exceeds a certain limit.

#### Hint:
1. Use `du -sh` to get the disk usage.
2. Use an `if` statement to compare the usage with a threshold.

**Example:**
```bash
#!/bin/bash

usage=$(du -sh ~ | cut -f1)
limit="1G"

if [[ "$usage" > "$limit" ]]; then
    echo "Warning: Your home directory is using $usage, which exceeds the limit of $limit."
else
    echo "Your home directory usage is $usage, within the limit of $limit."
fi
```

### Task 7: User Input Validation
Create a script that asks the user for a number between 1 and 10 and keeps asking until a valid number is entered.

#### Hint:
1. Use a `while` loop to repeatedly ask for input.
2. Use `read` to get the user's input.

**Example:**
```bash
#!/bin/bash

while true; do
    echo "Please enter a number between 1 and 10:"
    read number
    if [[ "$number" -ge 1 && "$number" -le 10 ]]; then
        echo "Thank you! You entered a valid number: $number"
        break
    else
        echo "Invalid number. Please try again."
    fi
done
```

### Task 8: Countdown Timer
Create a script that counts down from a given number of seconds.

#### Hint:
1. Use a `for` loop with a decrementing counter.
2. Use `sleep` to wait for one second in each iteration.

**Example:**
```bash
#!/bin/bash

echo "Enter the number of seconds for the countdown:"
read seconds

for (( i=$seconds; i>=0; i-- )); do
    echo "$i"
    sleep 1
done

echo "Time's up!"
```

### Task 9: Rename Files
Create a script that renames all `.txt` files in the current directory to have a `.bak` extension.

#### Hint:
1. Use a `for` loop to iterate through `.txt` files.
2. Use `mv` to rename the files.

**Example:**
```bash
#!/bin/bash

for file in *.txt; do
    mv "$file" "${file%.txt}.bak"
done
```

### Task 10: Display System Information
Create a script that displays basic system information such as the hostname, current user, and current date and time.

#### Hint:
1. Use `hostname` to get the hostname.
2. Use `whoami` to get the current user.
3. Use `date` to get the current date and time.

**Example:**
```bash
#!/bin/bash

echo "Hostname: $(hostname)"
echo "Current user: $(whoami)"
echo "Current date and time: $(date)"
```

### Task 11: Find and Replace Text in Files
Create a script that replaces a specified string with another string in all `.txt` files in the current directory.

#### Hint:
1. Use `sed` for find and replace.
2. Use a `for` loop to iterate through `.txt` files.

**Example:**
```bash
#!/bin/bash

echo "Enter the string to replace:"
read search
echo "Enter the replacement string:"
read replace

for file in *.txt; do
    sed -i "s/$search/$replace/g" "$file"
done
```

### Task 12: Generate a Random Password
Create a script that generates a random password of a specified length.

#### Hint:
1. Use `tr` to create random characters.
2. Use `/dev/urandom` as a source of randomness.

**Example:**
```bash
#!/bin/bash

echo "Enter the desired password length:"
read length

password=$(tr -dc 'A-Za-z0-9' < /dev/urandom | head -c "$length")
echo "Generated password: $password"
```

### Task 13: Monitor Log File
Create a script that monitors a log file and prints new entries as they are added.

#### Hint:
1. Use `tail -f` to follow the log file.

**Example:**
```bash
#!/bin/bash

echo "Enter the log file to monitor:"
read logfile

if [ -e "$logfile" ]; then
    tail -f "$logfile"
else
    echo "The file '$logfile' does not exist."
fi
```

### Task 14: Directory Size Alert
Create a script that checks the size of a specified directory and sends an alert if it exceeds a certain size.

#### Hint:
1. Use `du -sh` to get the directory size.
2. Use an `if` statement to compare the size with a threshold.

**Example:**
```bash
#!/bin/bash

echo "Enter the directory to check:"
read directory
echo "Enter the size limit (e.g., 100M):"
read limit

size=$(du -sh "$directory" | cut -f1)

if [[ "$size" > "$limit" ]]; then
    echo "Alert: The size of '$directory' is $size, which exceeds the limit of $limit."
else
    echo "The size of '$directory' is $size, within the limit of $limit."
fi
```

### Task 15: System Uptime
Create a script that prints the system uptime.

#### Hint:
1. Use the `uptime` command to get the system uptime.

**Example:**
```bash
#!/bin/bash

echo "System uptime: $(uptime -p)"
```

### Task 16: Check Internet Connection
Create a script that checks if the internet connection is active by pinging a well-known server.

#### Hint:
1. Use `ping` to check connectivity.
2. Use an `if` statement to check the ping result.

**Example:**
```bash
#!/bin/bash

ping -c 1 google.com &> /dev/null

if [ $? -eq 0 ]; then
    echo "Internet connection is active."
else
    echo "No internet connection."
fi
```

### Task 17: Create a Directory Structure
Create a script that creates a directory structure for a project.

#### Hint:
1. Use `mkdir -p` to create directories recursively.

**Example:**
```bash
#!/bin/bash

echo "Enter the project name:"
read project

mkdir -p "$project"/{src,bin,docs}

echo "Directory structure for '$project' created."
```

### Task 18: CPU Usage Alert
Create a script that checks the CPU usage and prints a warning if it exceeds a certain threshold.

#### Hint:
1. Use `mpstat` or

 `top` to get CPU usage.
2. Use an `if` statement to compare the usage with a threshold.

**Example:**
```bash
#!/bin/bash

threshold=80

cpu_usage=$(mpstat 1 1 | awk '/Average/ {print 100 - $12}')

if (( ${cpu_usage%.*} > threshold )); then
    echo "Warning: CPU usage is at $cpu_usage%, which exceeds the threshold of $threshold%."
else
    echo "CPU usage is at $cpu_usage%, within the threshold of $threshold%."
fi
```

### Task 19: List Installed Packages
Create a script that lists all installed packages on your system.

#### Hint:
1. Use `dpkg -l` on Debian-based systems or `rpm -qa` on Red Hat-based systems.

**Example for Debian-based systems:**
```bash
#!/bin/bash

dpkg -l
```

### Task 20: Send an Email Alert
Create a script that sends an email alert if a specified directory exceeds a certain size.

#### Hint:
1. Use `mail` or `sendmail` to send emails.
2. Use `du -sh` to get the directory size.

**Example:**
```bash
#!/bin/bash

echo "Enter the directory to check:"
read directory
echo "Enter the size limit (e.g., 100M):"
read limit
echo "Enter the email address to send the alert to:"
read email

size=$(du -sh "$directory" | cut -f1)

if [[ "$size" > "$limit" ]]; then
    echo "Alert: The size of '$directory' is $size, which exceeds the limit of $limit." | mail -s "Directory Size Alert" "$email"
else
    echo "The size of '$directory' is $size, within the limit of $limit."
fi
```

Feel free to try these tasks and ask if you need further assistance or more advanced tasks!
