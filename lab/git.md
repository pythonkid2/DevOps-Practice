
### Step 1: Configure Git
First, configure your Git with your GitHub account details.

```
git config --global user.name "pythonkid2"
git config --global user.email "mjcmathew@gmail.com"
```

### Step 2: Generate SSH Key
1. Generate a new SSH key:

   ```
   ssh-keygen -t ed25519 -C "mjcmathew@gmail.com"
   ```

   If you are using a legacy system that doesn't support the Ed25519 algorithm, use:

   ```
   ssh-keygen -t rsa -b 4096 -C "mjcmathew@gmail.com"
   ```

2. When prompted to "Enter a file in which to save the key," press Enter to accept the default file location.

3. At the prompt, type a secure passphrase (optional but recommended).

### Step 3: Add SSH Key to the SSH-Agent

1. Start the SSH agent:

   ```
   eval "$(ssh-agent -s)"
   ```

2. Add your SSH private key to the SSH agent:

   ```
   ssh-add ~/.ssh/id_ed25519
   ```

   If you used a different name for your key, replace `id_ed25519` with your key's name.

### Step 4: Add SSH Key to Your GitHub Account

1. Copy the SSH key to your clipboard:

   ```
   cat ~/.ssh/id_ed25519.pub
   ```

   If you used a different name for your key, replace `id_ed25519.pub` with your key's name.

2. Log in to your GitHub account.
3. In the upper-right corner, click your profile photo, then click **Settings**.
4. In the user settings sidebar, click **SSH and GPG keys**.
5. Click **New SSH key**.
6. In the "Title" field, add a descriptive label for the new key (e.g., "Personal Laptop").
7. Paste your key into the "Key" field.
8. Click **Add SSH key**.
9. If prompted, confirm your GitHub password.

### Step 5: Initialize a Git Repository
Navigate to your project directory and initialize a Git repository.

```
cd /new
git init
```

### Step 6: Add Files to the Repository
Add the files you created to the Git repository.

```
git add .
```

### Step 7: Commit the Files
Commit the files with a message.

```
git commit -m "Initial commit with 1 to 7.txt files"
```

### Step 8: Create a New Repository on GitHub
1. Go to GitHub and log in to your account.
2. Click on the "New" button to create a new repository.
3. Name your repository (e.g., "new-repo").
4. Add a description if you like.
5. Choose the visibility (public or private).
6. Do not initialize the repository with a README, .gitignore, or license.
7. Click "Create repository."

### Step 9: Add GitHub Repository as Remote
Copy the SSH URL of your new repository from GitHub and add it as a remote in your local Git repository.

```
git remote add origin git@github.com:pythonkid2/new-repo.git
```

### Step 10: Push to GitHub
Push your local repository to GitHub.

```
git push -u origin master
```

Following these steps will set you up with SSH and allow you to push your files to GitHub securely.
