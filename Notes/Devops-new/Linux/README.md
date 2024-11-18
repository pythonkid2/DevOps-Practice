
### Linux Filesystem Hierarchy

![Linux Architecture](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/b7ff75dc-b6dd-40e9-b8ad-a8091d6d2aaf)

1. **/bin** - Contains essential binary executables for the system. These are the basic command-line utilities required for the system to boot and operate in single-user mode. Examples include `ls`, `cp`, and `mv`.

2. **/boot** - Contains the boot loader files, including the kernel and other files needed to boot the Linux operating system. This directory is critical for system startup.

3. **/dev** - Contains device files. These are special files that represent hardware devices and peripherals such as hard drives, terminals, and USB devices. For example, `/dev/sda` represents a hard disk.

4. **/etc** - Contains all the system-wide configuration files and shell scripts that are used to boot and initialize system settings. This includes configuration files for different services and applications.

5. **/home** - Contains the home directories for all the system's users. Each user has a directory under `/home`, where they can store personal files and directories. For example, `/home/username`.

6. **/lib** - Contains essential shared libraries needed to boot the system and run the commands in `/bin` and `/sbin`. This directory also includes kernel modules.

7. **/mnt** - A mount point for temporarily mounting filesystems. This directory is commonly used by system administrators to mount storage devices or other file systems.

8. **/opt** - Used for the installation of add-on application software packages. Applications that are not included in the default Linux distribution can be installed here.

9. **/proc** - A virtual filesystem that provides information about running processes and the kernel. This directory contains files that are representations of system and process information.

10. **/root** - The home directory of the root user (superuser). This is not the root (/) directory, but the root user's personal directory.

11. **/sbin** - Contains essential system binaries that are generally used by the system administrator. These commands are crucial for system maintenance and repair. Examples include `fsck`, `reboot`, and `shutdown`.

12. **/srv** - Contains data for services provided by the system. For example, web server data might be stored in `/srv/www`.

13. **/tmp** - Contains temporary files that are created by system processes and applications. Files in this directory may be deleted upon system reboot.

14. **/usr** - Contains user utilities and applications. This directory has several subdirectories, such as `/usr/bin` for user binaries, `/usr/lib` for libraries, and `/usr/share` for shared data.

15. **/var** - Contains variable data files. This includes log files, mail and printer spool files, and files that are frequently modified. For example, log files are stored in `/var/log`.

---

### Example Command

To view the system's user account information, you can use the following command:
```sh
cd /etc && cat passwd
```
This will display the contents of the `/etc/passwd` file, which contains user account information. Note that while this file can be viewed by all users, sensitive information such as passwords is stored in a more secure manner (e.g., `/etc/shadow`).

---


adduser and useradd

![adding user](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/6cca6b4c-137e-49f7-9c2b-f55eaa45d33b)



sudo deluser name - removing user


## VIM/VI editor

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/be55bd0a-d57d-4d4f-baee-f66de91a916e)

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/cebdaa78-2108-48ad-a6c7-a80335f76454)
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/0b404176-9a8f-4ec0-88dc-46c37f79ee79)
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/e8e990bd-f9bd-4ddf-8c5a-6dc22d64d5a1)

## Package Manager

apt advanced package tool 

sudo apt install --- , sudo remove ...

nslookup 
dig

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/3df64cee-7f4a-4809-84da-4ac3b4bf002c)


sudo chmod -R o+wrx folder - regressively addimg permission 
![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/3ab6c755-b6f7-43be-8ece-71d63c08df63)


Change ownership

sudo chown mathew:group file


# grep

grep -i term file.txt 

grep -i term < file.txt   giving input

grep -i term *   looks for all files in current directory 
grep -iR   will look into directory too
grep -R term /etc/*


# less

reader like cat, can use up and down arrow, search
:q quite 

# more
percentage +less

# head 
head -2 file



