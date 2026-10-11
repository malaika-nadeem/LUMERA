# 🪐 Orbit

**Orbit** is a lightweight Linux terminal assistant that helps you explore and learn Linux commands without leaving your terminal.

Type a command name and Orbit shows you what it does, how to use it, an example, and which commands are related to it.

Orbit is the first project of **LUMERA**, an open-source umbrella for AI, cybersecurity, automation and software projects.

---

## ✨ Features

- 🐧 Terminal-based Linux assistant
- 📚 500+ commands across 64 categories (files, git, docker, networking, security tools, kernel, scripting and more)
- 🎨 Colorful terminal interface built with Rich, with an ASCII `ORBIT` banner
- 🧾 Each command shows: Purpose, Syntax, Example, Notes, Reference keywords and Related commands
- 🏷️ Every command has a Category and a Difficulty level
- 📄 Uses a structured CSV command database that is easy to extend
- 🧑‍💻 Beginner-friendly learning tool

---

## 📂 Project Structure

```
Orbit/
│
├── V1.0/
│   ├── lumera_orbit.py      # Main program
│   ├── linux_commands.csv   # Command database
│   └── README.md
│
└── README.md
```

---

## 🧰 Requirements

- Linux (built and tested on Ubuntu)
- Python 3
- Python packages: `rich` and `pyfiglet`

---

## 🚀 How to Run Orbit

### 1. Clone the Repository

```bash
git clone https://github.com/malaika-nadeem/LUMERA.git
```

### 2. Navigate to Orbit

```bash
cd LUMERA/Orbit/V1.0
```

### 3. Install Dependencies

```bash
pip install rich pyfiglet
```

> On Ubuntu, if pip shows an "externally managed environment" error, use:
>
> ```bash
> sudo apt install python3-rich python3-pyfiglet
> ```
>
> or create a virtual environment first.

### 4. Make Orbit Executable

```bash
chmod +x lumera_orbit.py
```

### 5. Run Orbit

```bash
./lumera_orbit.py
```

---

## 🔗 Run Orbit as a Terminal Command (Optional)

From inside `LUMERA/Orbit/V1.0`, install Orbit as a system command:

```bash
sudo ln -sf "$(pwd)/lumera_orbit.py" /usr/local/bin/orbit
```

Now Orbit can be launched from anywhere:

```bash
orbit
```

---

## 🖼️ Example

```
   ____  ____  ____  ____________
  / __ \/ __ \/ __ )/  _/_  __/
 / / / / /_/ / __  |/ /  / /
/ /_/ / _, _/ /_/ // /  / /
\____/_/ |_/_____/___/ /_/

Enter a Linux command:

> ls

╭────────────────── ls ──────────────────╮
│ Purpose: Lists files and directories.   │
│                                         │
│ Syntax: ls [options] [directory]        │
│                                         │
│ Example: ls -la                         │
│ ...                                     │
╰────────────── Files · Beginner ─────────╯
```

> 📸 Tip: replace this block with a real screenshot of Orbit running in your terminal.

---

## 🗄️ Command Database

Commands live in `linux_commands.csv`. To add a new command, add a new row with these columns:

| Column | Meaning |
|--------|---------|
| Chapter | Group the command belongs to |
| Command | Command name (what the user types) |
| Purpose | What the command does |
| Syntax | General usage pattern |
| Example | A real example |
| Options | Common flags |
| Category | Topic area |
| Difficulty | Beginner, Intermediate or Advanced |
| Notes | Extra tips |
| Keywords | Search and reference words |
| Related | Related commands |

---

## 🤝 Contributing

Ideas, bug reports and new commands are welcome. Open an issue or send a pull request on the [LUMERA repository](https://github.com/malaika-nadeem/LUMERA).

---

## 👩‍💻 Author

**Malaika Nadeem**
GitHub: [malaika-nadeem](https://github.com/malaika-nadeem)

Built as part of **LUMERA** 🌙
