#!/usr/bin/env python3
import random
import csv
from pathlib import Path
script_dir = Path(__file__).resolve().parent
csv_file = script_dir / "linux_commands.csv"
print("========================OrbitV1.0========================")
while True:
 command = input("Enter a command:")
 print(f" You entered: {command}")
 if command == "exit":
    print("Goodbye!!!!!")
    break

# Open the file securely using a context manager
 with open(csv_file, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    found = False
    # Optional: Skip the header row if you only want the data
    header = next(reader) 
    # Loop through each row
    for row in reader: 
        if row[1] == command:
            found = True
            print(f"===========================\nThe Purpose of command is:\n{row[2]}")
            print(f"===========================\nNotes:\n{row[8]}\n=========================")
        if command == "help":
         found = True
         print("=============================\n", row[1])    
     
 if found == False:
            print("Command is not found :(")            
 
     
                 
         

        
