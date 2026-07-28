# 💽 DiskArchive Pro

> Professional disk inventory, analysis, search and reporting software for Windows.

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![PySide6](https://img.shields.io/badge/PySide6-Qt6-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![License](https://img.shields.io/badge/License-MIT-orange)

---

## 📖 Overview

DiskArchive Pro is a professional desktop application developed with **Python**, **PySide6** and **SQLite**.

It scans disks, folders and files, stores the results in a local database and provides powerful analysis, search and reporting features.

Designed for:

- 💼 IT Administrators
- 🖥 System Engineers
- 📂 Archive Management
- 💾 Backup Verification
- 🏢 Enterprise Inventory

---

## ✨ Features

### ✔ Scan Engine

- Fast recursive scanning
- Folder size calculation
- File statistics
- Multi-thread scanning
- Progress reporting

### ✔ Database

- SQLite storage
- Repository Pattern
- Persistent inventory
- Fast queries

### ✔ Dashboard

- Disk statistics
- Largest folders
- Largest files
- Extension statistics
- Empty folders
- Empty files

### ✔ Search

- File search
- Extension filtering
- Size filtering
- Date filtering

### ✔ Reports

- Statistics
- Analysis
- Charts
- Export ready

---

## 🖼 Screenshots

### Dashboard

![Dashboard](screenshots/dashboard.png)

### Search

![Search](screenshots/search.png)

### Statistics

![Statistics](screenshots/statistics.png)

---

## 📁 Project Structure

```
DiskArchivePro
│
├── app
│   ├── config
│   ├── database
│   ├── gui
│   ├── models
│   ├── repository
│   ├── scanner
│   ├── services
│   ├── workers
│   └── utils
│
├── requirements.txt
├── main.py
└── README.md
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yusufyakici/DiskArchivePro.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

---

## 🚀 Roadmap

### Version 2.x

- [x] Dashboard
- [x] Repository Pattern
- [x] SQLite Database
- [x] Scan Engine
- [x] Reports
- [x] Search
- [x] Multi Thread Scan

### Coming Soon

- [ ] Scan History
- [ ] Duplicate Finder
- [ ] SHA256 / MD5 Hash
- [ ] HTML Reports
- [ ] PDF Reports
- [ ] Excel Export
- [ ] Compare Scans
- [ ] Dark Theme
- [ ] Plugin System

---

## 🛠 Technologies

- Python
- PySide6
- SQLite
- Qt Charts
- ReportLab
- OpenPyXL

---

## 🤝 Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

MIT License

---

## 👨‍💻 Author

**Yusuf YAKICI**

System Specialist

GitHub

https://github.com/yusufyakici
