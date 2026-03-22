# 🚀 GitHub Task Agent

A lightweight Python agent for managing tasks using GitHub Issues.

---

## 📌 Overview

This project provides a simple abstraction over the GitHub REST API to treat issues as tasks. It supports creating, retrieving, and completing tasks programmatically.

---

## ✨ Features

- ✅ Create tasks (GitHub Issues)
- 📋 Fetch tasks from a repository
- ✔️ Mark tasks as completed (close issues)
- 🧩 Modular and reusable design

---


## ⚙️ Requirements

- Python 3.8+
- GitHub Personal Access Token

---

## 🛠️ Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/github-task-agent.git
cd github-task-agent/backend
````

### 2️⃣ Install dependencies

```bash
pip install requests python-dotenv
```

### 3️⃣ Create a `.env` file

```env
GITHUB_TOKEN=your_github_token
GITHUB_USERNAME=your_username
DEFAULT_REPO=your_repository
```

---

## ▶️ Usage

Run the application:

```bash
python app.py
```

### 💡 Example actions

* Create a task
* List tasks
* Complete a task

---

## 🔗 API Mapping

| Action        | GitHub Endpoint                                   |
| ------------- | ------------------------------------------------- |
| Create Task   | POST /repos/{owner}/{repo}/issues                 |
| Get Tasks     | GET /repos/{owner}/{repo}/issues                  |
| Complete Task | PATCH /repos/{owner}/{repo}/issues/{issue_number} |

---

## 🎯 Use Cases

This agent can be used as a building block for:

* 🤖 AI-driven productivity tools
* 📊 Task automation systems
* 👨‍💻 Developer workflow management

---

## 👩‍💻 Author

**Meghana**

---

