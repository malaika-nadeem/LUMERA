#!/usr/bin/env python3
import random
import csv
from pathlib import Path
script_dir = Path(__file__).resolve().parent
csv_file = script_dir / "linux_commands.csv"
from rich.console import Console
from pyfiglet import Figlet

console = Console()

fig = Figlet(font="slant")
console.print(f"[cyan]{fig.renderText('ORBIT')}[/cyan]")
console.print("[bold white]Linux Command Assistant[/bold white]")
console.print("[green]Version 1.0[/green]")
with open(csv_file, "r", encoding="utf-8") as file:
    reader = list(csv.reader(file))

while True:
    command = input("orbit> ").strip().lower()

    if command == "exit":
        console.print("[bold green]Goodbye![/bold green]")
        break

    if not command:
        continue

    found = False

    # Help command
    if command == "help":
        console.print("[bold cyan]Available Commands:[/bold cyan]")
        for row in reader[1:]:  # Skip the header
            console.print(f"• {row[1]}")
        continue

    # Search for the command
    for row in reader[1:]:  # Skip the header
        if row[1].lower() == command:
            found = True
            console.print("[bold green]===========================[/bold green]")
            console.print(f"[yellow]Purpose:[/yellow]\n{row[2]}")
            console.print("[bold green]===========================[/bold green]")
            console.print(f"[yellow]Notes:[/yellow]\n{row[8]}")
            console.print("[bold green]===========================[/bold green]")
            break

    if not found:
        console.print("[bold red]❌ Command not found.[/bold red]")
        console.print("Type [cyan]help[/cyan] to see all available commands.")
     
                 
         

        
