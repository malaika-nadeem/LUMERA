# 🪐 Orbit

**Orbit** is a lightweight Linux terminal assistant that helps users explore and learn Linux commands directly from their terminal.

Orbit provides a simple command-line interface where users can search for Linux commands, understand their purpose, and learn basic usage without leaving the terminal.

---

## ✨ Features

- 🐧 Terminal-based Linux assistant
- 📚 Quick Linux command lookup
- ⚡ Lightweight and fast
- 📄 Uses a structured CSV command database
- 🧑‍💻 Beginner-friendly Linux learning tool
- 🔍 Simple command search system

---

## 📂 Project Structure

```
Orbit/
│
├── V1.0/
│   ├── lumera_orbit.py
│   ├── linux_commands.csv
│
└── README.md
```

---

# 🛠 Requirements

Before running Orbit, make sure you have:

- Linux operating system
- Python 3.x installed
- Terminal access

Check Python version:

```bash
python3 --version
```

---

# 🚀 How to Run Orbit

## 1. Clone the Repository

```bash
git clone https://github.com/malaika-nadeem/LUMERA.git
```

---

## 2. Navigate to Orbit

```bash
cd LUMERA/Orbit/V1.0
```

---

## 3. Make Orbit Executable

```bash
chmod +x lumera_orbit.py
```

---

## 4. Run Orbit

```bash
./lumera_orbit.py
```

Orbit will now start running in your terminal.

---

# 🔗 Run Orbit as a Terminal Command (Optional)

You can install Orbit as a system command:

```bash
sudo ln -s $(pwd)/lumera_orbit.py /usr/local/bin/orbit
```

Now Orbit can be launched from anywhere:

```bash
orbit
```

---

# 🖥 Example

```
Welcome to Orbit 🌌

Enter a Linux command:

> ls

Command: ls

Description:
Lists files and directories.

Usage:
ls [options] [directory]
```

---

# 🧠 Why Orbit?

Linux contains hundreds of powerful commands, but remembering them all can be difficult for beginners.

Orbit aims to make Linux command discovery easier by providing a simple assistant that lives inside the terminal.

---

# 🔮 Future Development

Planned improvements:

- More Linux commands
- Better search functionality
- Interactive Linux learning mode
- Command explanations with examples
- Additional terminal utilities

---

# 👩‍💻 Author

Built by **Malaika Nadeem**

A learning project exploring:

- Python
- Linux
- Terminal tools
- Command-line applications

---

⭐ If you find Orbit useful, consider starring the repository.
