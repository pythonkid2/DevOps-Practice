  # 🛠️ `sed` Command in Linux – Stream Editor

`sed` stands for **Stream EDitor**, a powerful Linux utility used to:
- Filter and transform text
- Perform basic text transformations on an input stream (files or input from a pipeline)
- Make substitutions, insertions, deletions, and more using **regular expressions**


## 🔹 Basic Syntax

```
sed [options] 'command' file_name
````

### Components:

* **`command`**: The sed action to perform (e.g., `s`, `d`, `i`, `a`)
* **`file_name`**: The target file (can also come from stdin)
* **Options**:

  * `-n` : Suppress automatic printing of pattern space
  * `-i` : Edit file **in-place** (modifies the original file)

---

## 🔸 Commonly Used `sed` Commands

| Command                  | Description                         |
| ------------------------ | ----------------------------------- |
| `s/pattern/replacement/` | Substitute pattern with replacement |
| `d`                      | Delete the pattern space (line)     |
| `p`                      | Print the pattern space             |
| `i\ text`                | Insert text **before** matched line |
| `a\ text`                | Append text **after** matched line  |
| `c\ text`                | Replace matched line with text      |
| `=`                      | Print line number                   |
| `q`                      | Quit sed after a specific condition |

---

## 🔸 Examples of `sed` Usage

### 🔁 Substitution (s)

```
sed 's/apple/orange/' file.txt
```

Replaces the **first** occurrence of “apple” with “orange” in each line.

```
sed 's/apple/orange/g' file.txt
```

Replaces **all** occurrences of “apple” in each line.

### ✍️ In-place Edit

```
sed -i 's/foo/bar/g' file.txt
```

Replaces “foo” with “bar” in-place (edits the actual file).

### 🚫 Deleting Lines

```
sed '2d' file.txt
```

Deletes line 2.

```
sed '/error/d' file.txt
```

Deletes all lines that contain “error”.

### 📌 Printing Specific Lines

```
sed -n '3p' file.txt
```

Prints only the 3rd line.

```
sed -n '/server/p' file.txt
```

Prints lines that contain “server”.

### ➕ Inserting and Appending Text

```
sed '2i\This is a new line' file.txt
```

Inserts a line **before** line 2.

```
sed '2a\This is an appended line' file.txt
```

Appends a line **after** line 2.

### 🔄 Replace Entire Line

```
sed '3c\This is the new content' file.txt
```

Changes line 3 to the given content.

### 🧾 Line Numbering

```
sed '=' file.txt
```

Displays line numbers along with content.

---

## 🔹 Range of Lines

```
sed '1,3d' file.txt
```

Deletes lines 1 through 3.

```
sed '/start/,/end/d' file.txt
```

Deletes lines between the lines containing “start” and “end”.

---

## 🔹 Multiple Commands

### Using `-e`:

```
sed -e 's/foo/bar/' -e 's/baz/qux/' file.txt
```

### Using `{}`:

```
sed '{
s/foo/bar/
s/baz/qux/
}' file.txt
```

---

## 🔹 Using Sed with Pipelines

```
cat file.txt | sed 's/error/ERROR/g'
```

```
grep "http" access.log | sed 's/200/OK/g'
```

---

## 🔹 Escape Characters

Some characters like `/`, `&`, and `\` need to be escaped.

### Example:

```
sed 's/\/usr\/local/\/usr\/bin/' file.txt
```

Or use a different delimiter:

```
sed 's|/usr/local|/usr/bin|' file.txt
```

---

## 🔹 Save Changes to a New File

```
sed 's/foo/bar/g' file.txt > new_file.txt
```

---

## 🔹 Advanced: Using Regular Expressions

```
sed -n '/^a.*z$/p' file.txt
```

Prints lines that start with "a" and end with "z".

---

## 🧪 Test Before Applying In-Place

Always test `sed` commands **without** `-i` first to avoid accidental data loss.

---

## 📚 Useful Resources

* [phoenixNAP – sed Overview](https://phoenixnap.com/kb/linux-sed)
* [IBM AIX sed docs](https://www.ibm.com/docs/en/aix/7.2.0?topic=s-sed-command)
* [GeeksforGeeks – sed Examples](https://www.geeksforgeeks.org/linux-unix/sed-command-in-linux-unix-with-examples/)
* [DigitalOcean sed Tutorial](https://www.digitalocean.com/community/tutorials/linux-sed-command)

---

## ✅ Summary

| Task             | Command                  |
| ---------------- | ------------------------ |
| Replace text     | `sed 's/old/new/' file`  |
| Replace globally | `sed 's/old/new/g' file` |
| Delete line      | `sed 'Nd' file`          |
| Insert before    | `sed 'Ni\text' file`     |
| Append after     | `sed 'Na\text' file`     |
| In-place edit    | `sed -i 's/x/y/' file`   |

```



````
# 🛠️ `sed` Practice Test – Full Coverage

## 📄 Sample Input File: `sample.txt`

```
apple is tasty
banana is yellow
foo is replaced
this is a test line
another foo test
user123 logged in
line with error
INFO: system boot
INFO: config loaded
start block
line inside block
end block
/home/user/docs
/home/user/photos

````

---

## ❓ Questions

### 🟦 Basic Substitution

1. Replace the **first occurrence** of `foo` with `bar` in each line.
2. Replace **all occurrences** of `is` with `was`.
3. Replace `user123` with `admin` only on **line 6**.

---

### 🟨 Line Deletion and Filtering

4. Delete the **third line**.
5. Delete all lines that contain the word `error`.
6. Delete **blank lines** from the file.

---

### 🟩 Selective Printing

7. Print **only line 4**.
8. Print all lines that contain `INFO`.
9. Print all lines between `start block` and `end block`.

---

### 🟪 Insertion and Appending

10. Insert the line `FRUIT HEADER` before every line that contains `apple` or `banana`.
11. Append the line `FOOTER` after every line containing `test`.

---

### 🟥 Change and Replace Lines

12. Replace line 2 entirely with `BANANA LINE`.
13. Change lines 10 to 12 to `BLOCK REMOVED`.

---

### 🟫 Advanced: Multiple Commands and Escaping

14. Use `sed` to replace both:

    * `apple` with `mango`
    * `banana` with `grapes`

15. Replace `/home/user` with `/mnt/data` using a different delimiter.

---

## ✅ Answers

### 1.

```
sed 's/foo/bar/' sample.txt
```

### 2.

```
sed 's/is/was/g' sample.txt
```

### 3.

```
sed '6s/user123/admin/' sample.txt
```

### 4.

```
sed '3d' sample.txt
```

### 5.

```
sed '/error/d' sample.txt
```

### 6.

```
sed '/^$/d' sample.txt
```

### 7.

```
sed -n '4p' sample.txt
```

### 8.

```
sed -n '/INFO/p' sample.txt
```

### 9.

```
sed -n '/start block/,/end block/p' sample.txt
```

### 10.

```
sed '/apple\|banana/i\FRUIT HEADER' sample.txt
```

### 11.

```
sed '/test/a\FOOTER' sample.txt
```

### 12.

```
sed '2c\BANANA LINE' sample.txt
```

### 13.

```
sed '10,12c\BLOCK REMOVED' sample.txt
```

### 14.

```
sed -e 's/apple/mango/g' -e 's/banana/grapes/g' sample.txt
```

### 15.

```
sed 's|/home/user|/mnt/data|g' sample.txt
```

---

## 🎯 Bonus: Multi-command One-Liner

```
sed -e '/^$/d' -e '/error/d' -e 's/^start.*/&\n#END/' -e 's/INFO/NOTICE/g' sample.txt
```

---
