from rich.console import Console
from rich.table import Table
from rich import print
import sys


def hash_checker():
    # NOTE: If you want a differnt directory, put the whole path!
	file_check = input("Enter the file that you want to check the hash on: ")
	with open(file_check) as file:
		file = file.readlines()

	for i in file:
		i = i.split(" ")
	hash = i[0]

	with open("hash_list.txt") as hash_list:
		hash_list = hash_list.readlines()

	vuln = []
	for i in hash_list:
		if hash in i:
			vuln.append(hash)

	if vuln:
		print(f"File is vulnerable")
	else:
		print(f"File is not vulnerable")



def check(test):
    if test == "2":
        return test
    if test == "1":
        sys.exit()
    sel = ["1", "2"]
    while test not in sel:
            console.log("Please enter either 1 or 2")
            test = console.input("[bold red]Select 1 to exit |""[bold green]| Select 2 to continue: ")
    return test


# Main
test = ""
while test != "1":
    print()
    table = Table(title="Hash Checker Command")
    table.add_column("NUM", style="green")
    table.add_column("TASK", style="red")
    table.add_column("Description", style="blue")
    table.add_row("1", "hash_checker", "This will check a file of your choice against known vulnerable hashes.")
    console = Console()
    console.print(table)
    print()
    selection = input("enter a number to execute the command: ")
    if selection == "1":
        hash_checker()
    else:
        console.log("[bold red]Please enter a valid choice!")
    print()
    test = console.input("[bold red]Select 1 to exit |""[bold green]| Select 2 to continue: ")
    if test != "1":
        x = check(test)
        if x == "1":
            sys.exit()
