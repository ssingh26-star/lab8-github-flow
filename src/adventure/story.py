from adventure.utils import read_events_from_file
import random
from rich import print
from rich.console import Console

default_message = "[red][bold]You stand still, unsure what to do. The forest swallows you.[/bold][/red]"

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return default_message

def left_path(event):
    return "[cyan][bold]You walk left. [/cyan][/bold]" + event

def right_path(event):
    return "[magenta][bold]You walk right.[/bold] [/magenta]" + event

if __name__ == "__main__":
    console = Console()
    events = read_events_from_file('events.txt')

    print("[green][bold]You wake up in a dark forest. You can go left or right.[/green][/bold]")
    
    while True:
        choice = console.input("[bold]Which direction do you choose?[/bold] (left/right/exit): ")
        choice = choice.strip().lower()
        if choice == 'exit':
            print("[cyan][bold]Goodbye![/bold][/cyan]")
            break
        
        print(step(choice, events))