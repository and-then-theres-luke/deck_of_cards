from classes.player import Player
from classes.deck import Deck
from classes.game import Game




luke = Player("Luke")
hutch = Player("Hutch")
turn_counter = False
new_game = Game()
program_running = True

print("Welcome! Here's a list of games you can play.")
print("Go Fish")

while program_running == True:
    selection = input("Type the name of the game you want to play")
    if selection == "Go Fish":
        new_game.go_fish(luke, hutch)
        program_running = new_game.continue_or_exit()
    elif selection == "exit":
        program_running = False
    else:
        print("Invalid selection, try again.")
