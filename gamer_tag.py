# Jason Schriner
# Assignment 2.2
# 10/25/24

import random
import sys
# This program adds a random adjective to a random noun to create a gamer tags

adj = ["red", "blue", "green", "yellow", "orange", "purple", "hot", "cold", "warm", "cool"]
noun = ["dog", "cat", "bird", "fish", "hamster", "turtle", "lizard", "panda", "snake", "monkey"]

def main():
    while True:
        adj_int = random.randint(0, len(adj)-1)
        noun_int = random.randint(0, len(noun)-1)
        print("Your gamertag is: " + adj[adj_int] + noun[noun_int])
        print(" ")
        if input("Would you like another gamertag? (y/n) ") == "n":
            sys.exit()
        else:
            print(" ")
            main()

if __name__ == "__main__":
    main()