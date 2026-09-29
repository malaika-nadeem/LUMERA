#!/usr/bin/env python3
import csv
import difflib
from pathlib import Path
>>>>>>> f61eb32 (Update Orbit code, dataset, and README)
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from pyfiglet import Figlet

console = Console()
csv_file = Path(__file__).resolve().parent / "linux_commands.csv"

with open(csv_file, encoding="utf-8") as f:
    commands = {row["Command"].lower(): row for row in csv.DictReader(f)}

def show(row):
    body = (
        f"[yellow]Purpose:[/yellow] {row['Purpose']}\n\n"
        f"[yellow]Syntax:[/yellow] {row['Syntax']}\n"
        f"[yellow]Example:[/yellow] {row['Example']}\n\n"
        f"[yellow]Notes:[/yellow] {row['Notes']}\n\n"
        f"[yellow]Reference:[/yellow] {row['Keywords']}\n\n"
        f"[yellow]Related:[/yellow] {row['Related']}"
    )
    console.print(Panel(body, title=row["Command"],
                        subtitle=f"{row['Category']} · {row['Difficulty']}",
                        border_style="green"))

def list_commands(filter_text=""):
    table = Table(title="Commands")
    for col in ("Command", "Category", "Difficulty"):
        table.add_column(col)
    for name, row in commands.items():
        if filter_text in (row["Category"] + row["Difficulty"]).lower():
            table.add_row(row["Command"], row["Category"], row["Difficulty"])
    console.print(table)

console.print(f"[cyan]{Figlet(font='slant').renderText('ORBIT')}[/cyan]")
console.print("[bold white]Linux Command Assistant[/bold white]  [green]v1.1[/green]")

while True:
    query = input("orbit> ").strip().lower()
    if not query:
        continue
    if query == "exit":
        console.print("[bold green]Goodbye![/bold green]")
        break
    if query.startswith("list"):
        list_commands(query[4:].strip())
    elif query in commands:
        show(commands[query])
    else:
        close = difflib.get_close_matches(query, commands.keys(), n=3)
        console.print("[bold red]❌ Not found.[/bold red]")
        if close:
            console.print(f"Did you mean: [cyan]{', '.join(close)}[/cyan]?")