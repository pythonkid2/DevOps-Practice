

````markdown
# 🛠️ `sed` Command in Linux – Stream Editor

`sed` stands for **Stream EDitor**, a powerful Linux utility used to:
- Filter and transform text
- Perform basic text transformations on an input stream (files or input from a pipeline)
- Make substitutions, insertions, deletions, and more using **regular expressions**

---

## 🔹 Basic Syntax

```bash
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

```bash
sed 's/apple/orange/' file.txt
```

Replaces the **first** occurrence of “apple” with “orange” in each line.

```bash
sed 's/apple/orange/g' file.txt
```

Replaces **all** occurrences of “apple” in each line.

### ✍️ In-place Edit

```bash
sed -i 's/foo/bar/g' file.txt
```

Replaces “foo” with “bar” in-place (edits the actual file).

### 🚫 Deleting Lines

```bash
sed '2d' file.txt
```

Deletes line 2.

```bash
sed '/error/d' file.txt
```

Deletes all lines that contain “error”.

### 📌 Printing Specific Lines

```bash
sed -n '3p' file.txt
```

Prints only the 3rd line.

```bash
sed -n '/server/p' file.txt
```

Prints lines that contain “server”.

### ➕ Inserting and Appending Text

```bash
sed '2i\This is a new line' file.txt
```

Inserts a line **before** line 2.

```bash
sed '2a\This is an appended line' file.txt
```

Appends a line **after** line 2.

### 🔄 Replace Entire Line

```bash
sed '3c\This is the new content' file.txt
```

Changes line 3 to the given content.

### 🧾 Line Numbering

```bash
sed '=' file.txt
```

Displays line numbers along with content.

---

## 🔹 Range of Lines

```bash
sed '1,3d' file.txt
```

Deletes lines 1 through 3.

```bash
sed '/start/,/end/d' file.txt
```

Deletes lines between the lines containing “start” and “end”.

---

## 🔹 Multiple Commands

### Using `-e`:

```bash
sed -e 's/foo/bar/' -e 's/baz/qux/' file.txt
```

### Using `{}`:

```bash
sed '{
s/foo/bar/
s/baz/qux/
}' file.txt
```

---

## 🔹 Using Sed with Pipelines

```bash
cat file.txt | sed 's/error/ERROR/g'
```

```bash
grep "http" access.log | sed 's/200/OK/g'
```

---

## 🔹 Escape Characters

Some characters like `/`, `&`, and `\` need to be escaped.

### Example:

```bash
sed 's/\/usr\/local/\/usr\/bin/' file.txt
```

Or use a different delimiter:

```bash
sed 's|/usr/local|/usr/bin|' file.txt
```

---

## 🔹 Save Changes to a New File

```bash
sed 's/foo/bar/g' file.txt > new_file.txt
```

---

## 🔹 Advanced: Using Regular Expressions

```bash
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
