

## 🧱 THE BIG IDEA: “You added a new hard disk to a computer. Now what?”

Imagine this:

- You have a **computer** (EC2 instance)
- You plug in a **new hard disk** (EBS volume)
- You want to use it: store files, make it survive reboots, maybe even store a database or web content.

This is exactly what's happening when you attach an EBS volume to your EC2 instance. Let’s go step by step — explaining **what** each part is and **why** it matters.

---

## 🧩 LAYER 1: **What is an EBS Volume?**

### What it really is:
- A **network-attached storage device** in AWS.
- Think of it like a detachable USB hard drive for the cloud.
- You can attach it to a VM (EC2), remove it, reattach it elsewhere.
- But once it’s attached, **Linux sees it as a local disk** — just like a hard drive.

---

## 🧩 LAYER 2: **How Linux Sees Disks**

When a disk is attached, Linux creates a special file in `/dev` to represent it.

### Common device files:
| File        | Meaning                       |
|-------------|-------------------------------|
| `/dev/xvda` | Main OS disk (root filesystem)|
| `/dev/xvdd` | Your EBS volume               |
| `/dev/nvme0n1` | Same idea, but newer device name |

**These are not files with text — they are interfaces to hardware.** Linux reads and writes to them like it's using a physical disk.

👉 `lsblk` is the best way to visualize disks:
```bash
lsblk
```

---

## 🧩 LAYER 3: **Partitions vs Raw Disks**

Most disks get **partitioned** — that’s like dividing your hard drive into smaller blocks. You’ll see:

```
xvda    100G
├─xvda1  99G
└─xvda2   1G
```

But with EBS volumes, **we often skip partitioning** and use the full device directly (`/dev/xvdd`) unless we need more control (multiple mount points, etc.).

---

## 🧩 LAYER 4: **Filesystems (ext4, xfs, etc.)**

> Raw disks can’t store files until you put a **filesystem** on them.

### Filesystem = Rules for organizing files & directories.

#### Common ones:
| Type   | When to use it                     |
|--------|------------------------------------|
| `ext4` | Default for Ubuntu — reliable, fast|
| `xfs`  | High performance, large files      |
| `btrfs`, `zfs` | Advanced features (snapshots, RAID, etc.) |

🧪 Check if your disk has a filesystem:
```bash
sudo file -s /dev/xvdd
```

💿 If it says "data", it's unformatted — so format it:
```bash
sudo mkfs -t ext4 /dev/xvdd
```

---

## 🧩 LAYER 5: **Mount Points**

> Linux doesn’t mount disks automatically. You have to tell it where.

### Mounting = Attaching a disk to a folder path.

For example:
```bash
sudo mkdir /mnt/data
sudo mount /dev/xvdd /mnt/data
```

Now anything written to `/mnt/data` goes to your EBS volume.

👉 `df -h` shows mounted filesystems:
```bash
df -h
```

---

## 🧩 LAYER 6: **UUIDs & Disk Identity**

> `/dev/xvdd` is just a name. It can change after reboot. Not reliable.

Each filesystem has a **UUID** — a unique ID that doesn’t change.

Get it like this:
```bash
sudo blkid /dev/xvdd
```

You'll see something like:
```
UUID="abc123-456def" TYPE="ext4"
```

---

## 🧩 LAYER 7: **fstab (Persistent Mounts)**

> Mounting manually disappears after a reboot. You need to automate it.

`/etc/fstab` is a config file that tells Linux:
> "Mount this disk here at every boot."

**Use UUID instead of `/dev/xvdd`** to avoid name issues.

Example entry:
```
UUID=abc123-456def  /mnt/data  ext4  defaults,nofail  0  2
```

| Field       | Meaning                                         |
|-------------|-------------------------------------------------|
| UUID=...    | Which disk                                      |
| /mnt/data   | Where to mount                                  |
| ext4        | Filesystem type                                 |
| defaults    | Standard settings                               |
| nofail      | Don’t crash boot if the disk isn’t there        |
| 0 2         | Disk check order (you can ignore this for now)  |

⏳ Test before rebooting:
```bash
sudo mount -a
```

---

## 🧩 LAYER 8: **Ownership & Permissions**

By default, only root can write to new mounts.

To give your user access:
```bash
sudo chown ubuntu:ubuntu /mnt/data
```

Now you can create files freely.

---

## 🧩 LAYER 9: **Best Practices & Tips**

- **Naming conventions**: AWS may show `/dev/sdf`, Linux might show it as `/dev/xvdd`. That’s normal.
- **Unmount before detaching**: Always `sudo umount /mnt/data` before detaching the volume from EC2.
- **Mount to meaningful paths**: Like `/data`, `/mnt/app-storage`, or `/var/www/data`.

---

## 🚀 Summary: End-to-End Flow

| Step | Command | Meaning |
|------|---------|---------|
| 1. See disks | `lsblk` | See attached volumes |
| 2. Check format | `sudo file -s /dev/xvdd` | Check if unformatted |
| 3. Format | `sudo mkfs -t ext4 /dev/xvdd` | Add filesystem |
| 4. Mount | `sudo mount /dev/xvdd /mnt/data` | Make it usable |
| 5. Check UUID | `sudo blkid /dev/xvdd` | Get permanent ID |
| 6. Edit fstab | `sudo vi /etc/fstab` | Automate mount |
| 7. Test | `sudo mount -a` | Make sure no typos |
| 8. Permissions | `sudo chown ubuntu:ubuntu /mnt/data` | Access for your user |

---
