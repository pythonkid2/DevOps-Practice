![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/bb92da1f-49df-4587-9093-4a006f604c84)


save script as filename.sh 
chmod +x filename.sh
execute this command - ./filename.sh

#!/bin/bash

#! - shebang

if we not mentioning shebang we can execute it as -

![image](https://github.com/pythonkid2/DevOps-Practice/assets/100591950/b6a4bf2f-5b23-44af-bfd5-6463d7620e24)

+++

![image](https://github.com/user-attachments/assets/2ea84312-d6a8-46e9-9b98-1124ae274756)



### Basic Search and Replace:
- **`:%s/old/new/g`**  
  This replaces all occurrences of "old" with "new" in the entire file without confirmation.

### Search and Replace with Confirmation:
- **`:%s/old/new/gc`**  
  Adds the `c` flag for confirmation before each replacement. You can confirm with `y` (yes), `n` (no), `a` (all), `q` (quit), `l` (last), or `Ctrl-E` and `Ctrl-Y` to scroll while confirming.

### Limit Replacement to a Specific Range:
- **`:10,20s/old/new/g`**  
  Replaces all occurrences of "old" with "new" only in lines 10 through 20.

- **`:'<,'>s/old/new/g`**  
  If text is selected in visual mode, this replaces all occurrences in the selected area.

### Replace Only the First Occurrence in Each Line:
- **`:%s/old/new/`**  
  Omits the `g` flag, so only the first occurrence of "old" is replaced on each line.

### Case-Insensitive Search and Replace:
- **`:%s/old/new/gI`**  
  Adds the `I` flag to ignore case while searching for "old".

### Replacing Whole Words Only:
- **`:%s/\<old\>/new/g`**  
  This replaces only whole words "old" with "new", preventing partial matches (e.g., it will not replace "folder" if searching for "old").

### Reuse the Last Search Pattern:
- **`:%s//new/g`**  
  Skips specifying the "old" pattern and reuses the last search pattern for replacement.

### Use a Different Delimiter:
- **`:%s#old#new#g`**  
  Uses `#` as the delimiter instead of `/`, which can be useful when replacing strings that contain `/`.

These commands enhance flexibility and efficiency when using search and replace in `vim`.






practice-

---

Update the script to use 2 command line variables $1 and $2 for country and capital respectively. When the script is executed it should now print the country and its 
capital using the values passed in as command line arguments.


eg: ./print-capital.sh Nigeria Abuja should print Capital city of Nigeria is Abuja


echo "Capital city of $1 is $2"

---

/home/bob/backup-file.sh to create a backup of any given file. Update the script to use command line argument $1 for the filename to be backed up instead of the hard-coded filename.


eg: ./backup-file.sh create-and-launch-rocket should backup create-and-launch-rocket to create-and-launch-rocket_bkp

```
# This script creates a backup of a given file by creating a copy as bkp
# For example some-file is backed up as some-file_bkp
set -e

file_name=$1

cp $file_name ${file_name}_bkp

echo "Done"
```
             
