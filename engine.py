import os
from itertools import zip_longest

from dictionary import Dictionary
from validator import Validator
from stats import Stats


class Engine:

    def __init__(self) -> None:
        self.dictionary = Dictionary()

        while True:
            cmd = input("1 - New game\n2 - Game rules\n3 - Exit\n")

            if cmd == "3":
                break

            elif cmd == "2":
                print("""Guess the word...""")
                print()
            
            elif cmd == "1":
                self.new_game()
                print("-------------------------------------------------")


    def new_game(self, tries: int = 10) -> None:
        word_to_guess = self.dictionary.get_word().upper()

        for try_ in range(tries):
            guess = input(f"Try {try_}: ").upper()

            if not Validator.is_isogram(guess):
                print(f"{guess} is not an isogram!")
                continue

            res = Engine.check_guess(word_to_guess, guess)

            if res.bulls == len(word_to_guess):
                print(f"Congratulations! You guessed the word {word_to_guess}")
                return

            print(f"Cows: {res.cows} | Bulls: {res.bulls}")

        print(f"You loose! The word was: {word_to_guess}")


    
    def check_guess(word_to_guess: str, guess: str) -> Stats:
        bulls, cows = 0, 0
        checked_letters = []
        for l1, l2 in zip_longest(word_to_guess, guess):
            if not l1:
                return Stats(bulls=bulls, cows=cows)

            if l1 == l2 and l2 not in checked_letters:
                checked_letters.append(l2)
                bulls += 1
            elif l1 == l2 and l2 in checked_letters:
                bulls += 1
                cows -= 1
            elif l1 != l2 and l2 in word_to_guess and l2 not in checked_letters:
                checked_letters.append(l2)
                cows += 1
        return Stats(bulls=bulls, cows=cows)