# Made by Venkata Ramana Panigrahi!!
# I implemented the Hunt The Wumpus game but with a little special spicy masala!!! I is not a defined board game but I made it as a dynamic board game, execute it to play the game and to know what changes i made to the Game!!!

import random
class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.player_position = (0, 0)
        self.wumpus_positions = [(2, 0), (1, 1)]
        self.pit_positions = [(3, 0), (2, 2)]
        self.gold_position = (3, 2)
        self.moves_counter = 0
        self.is_game_over = False

    def generate_random_position(self):
        return random.randint(0, self.size - 1), random.randint(0, self.size - 1)

    def display_world(self):
        for row in range(self.size):
            for col in range(self.size):
                position = (row, col)
                if position == self.player_position:
                    print("A", end=" ")
                elif position in self.wumpus_positions:
                    print("W", end=" ")
                elif position == self.gold_position:
                    print("G", end=" ")
                elif position in self.pit_positions:
                    print("P", end=" ")
                else:
                    print("-", end=" ")
                print("|", end=" ") if col < self.size - 1 else None
            print("\n" + "-" * (4 * self.size - 1)) if row < self.size - 1 else None

    def check_adjacent(self, position1, position2):
        return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1]) == 1

    def move_player(self, direction):
        new_position = self.player_position

        if direction == "U" and self.player_position[0] > 0:
            new_position = (self.player_position[0] - 1, self.player_position[1])
        elif direction == "D" and self.player_position[0] < self.size - 1:
            new_position = (self.player_position[0] + 1, self.player_position[1])
        elif direction == "L" and self.player_position[1] > 0:
            new_position = (self.player_position[0], self.player_position[1] - 1)
        elif direction == "R" and self.player_position[1] < self.size - 1:
            new_position = (self.player_position[0], self.player_position[1] + 1)
        else:
            print("Ouch! You bumped into a wall.")
            return

        self.player_position = new_position

        # Change Wumpus positions after every two moves
        if self.moves_counter % 2 == 0:
            self.wumpus_positions = [self.generate_random_position(), self.generate_random_position()]

        if self.check_adjacent(self.player_position, self.gold_position):
            print("I can see gold light.")
        elif any(self.check_adjacent(self.player_position, wumpus_position) for wumpus_position in self.wumpus_positions):
            print("You smell a dirty stench.")

        for pit_position in self.pit_positions:
            if self.player_position == pit_position:
                print("Game Over! You fell into a pit.")
                self.is_game_over = True

        for wumpus_position in self.wumpus_positions:
            if self.player_position == wumpus_position:
                print("The WUMPUS got you!!!")
                self.is_game_over = True

        if self.player_position == self.gold_position:
            print("\nCongratulations! You found the gold. Here's a gift!\n")
            self.is_game_over = True

        self.moves_counter += 1
# The code starts executing from here!!
    def print_welcome_message(self):
        print("\nSwasthik and Vishal, on a vacation, discovered a mysterious cave with a maze of rooms.")
        print("\nLegends spoke of hidden gold guarded by the mythical Wumpus in that cave.")
        print("Armed with a map, they navigated through dark chambers, avoiding pits and deciphering coded warnings.")
        print("\nEvery move brought them closer to victory or danger.")
        print("The cave became a battleground of wits, and only time would reveal their fate.")
        print("\nSwasthik's magical power grants him glimpses of the Wumpus and pits, guiding their way through the mysterious cave in search of hidden treasure.")
        print("\nWill they conquer the maze, or will the Wumpus claim its intruders? ")
        #_Main_
if __name__ == "__main__":
    wumpus_game = WumpusWorld()
    wumpus_game.print_welcome_message()

    print("\nNow you are Swasthik, are you ready to help Vishal") # Do not take any double meanings!! Used Swasthik as it is some sanskrit symbol and people can easily admit if he has magical powers!!
    choice = input("Enter 'yes' or 'no': ")

    if choice.lower() == 'yes':
        print("------------------------------------------Let the Quest for Gold being!!---------------------------------------------------")
        print("\nThe 'A' represents Vishal's current location, and Swasthik(you) has the ability to identify Pits (P), Wumpus (W), and Gold (G) in the maze.\n\nSwasthik, you have the opportunity to guide Vishal by specifying directions. \n\nThe Wumpus roams freely through the chambers, so exercise caution! If it approaches the Gold room, try changing your position to avoid detection.\n Sometimes Vishaland Wumpus may come to same position, so be careful.\nYou can choose from four directions: 'U' for UP, 'D' for DOWN, 'L' for LEFT, and 'R' for RIGHT.\n")
        while not wumpus_game.is_game_over:
            wumpus_game.display_world()
            wumpus_game.move_player(input("\n\n\nEnter your move Swasthik!! (U/D/L/R): ").upper())

        print("Game Over. Thanks for playing!")
    else:
        print("Try again!!")
        
# HAPPY CODING!!!