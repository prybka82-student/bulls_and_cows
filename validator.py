class Validator:

    def is_isogram(word: str) -> bool:
        return len(word) == len(set(word))
