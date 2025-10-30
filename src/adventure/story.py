from adventure.utils import read_events_from_file
import random
from rich import print

def step(choice: str, events):
    random_event = random.choice(events)

    if choice == "left":
        return left_path(random_event)
    elif choice == "right":
        return right_path(random_event)
    else:
        return "[orange4]You stand still, unsure what to do. The forest swallows you. [/orange4]"

def left_path(event):
    return "[purple]You walk left. [/purple]" + event

def right_path(event):
    return "[blue]You walk right. [/blue]" + event

if __name__ == "__main__":
    events = read_events_from_file('events.txt')

    print("[green]You wake up in a dark forest. You can go left or right.[/green]")
    while True:
        choice = input("Which direction do you choose? (left/right/exit): ")
        choice = choice.strip().lower()
        if choice == 'exit':
            break
        
        print(step(choice, events))
