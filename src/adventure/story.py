from adventure.utils import read_events_from_file
import random
from rich import print
from rich.prompt import Prompt
from rich.panel import Panel

default_message = "You stand still, unsure what to do. The forest swallows you."

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[red]You stand still, unsure what to do. The forest swallows you.[/red]"

def left_path(event):
    return "[cyan]You walk left. [/cyan]" + event

def right_path(event):
    return "[magenta]You walk right. [/magenta]" + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    print("[green]You wake up in a dark forest. You can go left or right.[/green]")
    
    while True:
        # Show choices as suggestion text instead of validation
        choice = Prompt.ask(
            "[blue][bold]Which direction do you choose? (left/right/exit)[/bold][/blue]"
        ).strip().lower()
        
        if choice == 'exit':
            break
        
        result = step(choice, events)
        print(Panel(result, style="bold"))