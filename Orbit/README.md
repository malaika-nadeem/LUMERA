# Lumera Orbit🪐

**Lumera Orbit** is the first project developed under the Lumera ecosystem.

Orbit is a terminal-based Linux assistant written in Python that helps users learn Linux commands through a simple interactive interface.

---

## Current Features

- Interactive terminal interface
- Linux command lookup
- Displays the purpose of commands
- Displays command notes
- Built-in `help` command
- Built-in `exit` command
- CSV-based command database

---

## Technologies

- Python 3
- CSV
- pathlib

---

## Project Structure

```
Orbit/
└── V1.0/
    ├── orbit.py
    ├── linux_commands.csv
    └── README.md
```

---
How to Run Orbit
1. Clone the Repository
git clone https://github.com/yourusername/LUMERA.git
2. Navigate to Orbit
cd LUMERA/Orbit/V1.0
3. Make Orbit Executable
chmod +x lumera_orbit.py
4. Run Orbit
./lumera_orbit.py

Orbit will start running in your terminal.

🔗 Run Orbit as a Terminal Command (Optional)

You can install Orbit as a system command:

sudo ln -s $(pwd)/lumera_orbit.py /usr/local/bin/orbit

Now you can launch Orbit from anywhere:

orbit
🖥 Example
$ orbit

Welcome to Orbit 🌌

Enter a Linux command:
> ls

Command: ls

Description:
Lists files and directories.

Usage:
ls [options] [directory]

## Future Development

Planned improvements include:

- Natural language command search
- AI-powered explanations
- Command examples
- Search by category
- Favorites system
- Command history
- Safe command execution
- Plugin architecture

---

## Current Version

**Version:** V1.0

This release represents the foundation of Orbit.

---

## Author

Malaika Nadeem

Part of the **Lumera** ecosystem.
