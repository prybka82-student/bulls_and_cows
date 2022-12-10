class Validator:

    def is_isogram(word: str) -> bool:
        for letter in word:
            if word.count(letter) > 1:
                return False
        return True
