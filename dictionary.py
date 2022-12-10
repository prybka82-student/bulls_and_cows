from random import choice
from validator import Validator

class Dictionary:
    
    words = []
    
    def __init__(self, dict_file="dictionary.txt") -> None:
        with open(dict_file, "rt", encoding="UTF-8") as file:
            for line in file.readlines():
                line = line.strip().upper()
                if Validator.is_isogram(line):
                    self.words.append(line)
                else:
                    print(f">{line}< is not an isogram!")


    def get_word(self) -> str:
        return choice(self.words)