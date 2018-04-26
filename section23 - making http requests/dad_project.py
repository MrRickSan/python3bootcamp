from pyfiglet import figlet_format
from termcolor import colored
from colorama import init
from random import choice
import requests

init()


def print_art():
    ascii_art = figlet_format("DAD JOKE 3000")
    colored_ascii = colored(ascii_art, color="magenta")
    print(colored_ascii)

def main():
    print_art()
    joke = input("Let me tell you a joke! Give me a topic: ")
    response = get_jokes(joke)
    num_of_jokes = len(response['results'])
    if num_of_jokes == 1:
        print(f"I've got {num_of_jokes} joke about {joke}. Here it is: ")
        response = choice(response['results'])
        print(response['joke'])
    elif num_of_jokes > 1:
        print(f"I've got {num_of_jokes} jokes about {joke}. Here's one: ")
        response = choice(response['results'])
        print(response['joke'])
    else:
        print(f"Sorry, I don't have any jokes about {joke}! Please try again.")
        


def get_jokes(joke):
    url = "https://icanhazdadjoke.com/search"

    response = requests.get(
        url, 
        headers={"Accept": "application/json"},
        params={"term": joke}
    )

    data = response.json()
    return data
    


main()